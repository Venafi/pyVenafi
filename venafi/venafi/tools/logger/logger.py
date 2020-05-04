from typing import List, Callable, Any
import os
import sys
import traceback
import inspect
from datetime import datetime
import jsonpickle
import re
import threading
from pathlib import Path
from contextlib import contextmanager
from venafi.tools.logger.config import LogTag, LogTags
from venafi.tools.logger.generators import HtmlLogGenerator
from venafi.tools.logger.sqlite.dal import LoggerSql

jsonpickle.set_encoder_options('json', sort_keys=True, indent=4)
logger_lock = threading.Lock()


class _LogThread:
    def __init__(self, depth: int = -1, sql: LoggerSql = None, blacklist_function: Callable = None,
                 mode: str = 'all'):
        self.depth = depth
        self.sql = sql
        self._mode = mode
        self.persistence_enabled = mode in {'all', 'persistence'}
        self.console_enabled = mode in {'all', 'console'}
        self.blacklist_function = blacklist_function

    @property
    def mode(self):
        return self._mode

    @mode.setter
    def mode(self, value: str):
        if value not in (values := {'all', 'persistence', 'console'}):
            raise ValueError(f'Cannot set mode to "{value}" because it is invalid.\n'
                             f'Valid modes are {values}')
        self._mode = value
        self.persistence_enabled = value in {'all', 'persistence'}
        self.console_enabled = value in {'all', 'console'}


def singleton(cls):
    instances = {}

    def _singleton(*args, **kwargs):
        if cls not in instances:
            instances[cls] = cls(*args, **kwargs)
        return instances[cls]

    return _singleton


@singleton
class Logger:
    def __init__(self):
        self._disabled = True
        self._date_format = '%Y/%m/%d %H:%M:%S'
        self._timestamp = lambda: datetime.now().strftime(self._date_format)
        self._persistent_logging = False
        self._log_path = None
        self._log_tags = LogTags
        self._sql = None
        self._main_thread = threading.current_thread()
        self._threads = {self._main_thread.ident: _LogThread(depth=0)}

    @property
    def log_path(self):
        return self._log_path

    @log_path.setter
    def log_path(self, path: str):
        if self._log_path is not None or not isinstance(path, str) or self._persistent_logging:
            raise ValueError(f'Cannot set log path to "{path}" because it is already set to "{path}".')
        if not path.endswith('.db'):
            path += '.db'
        self._log_path = Path(path)
        self._persistent_logging = True

    @property
    def log_tags(self):
        return self._log_tags

    @log_tags.setter
    def log_tags(self, value):
        if not hasattr(value, 'default'):
            raise AttributeError(f'The custom logger must have a <default> LogTag attribute defined.')
        elif not hasattr(value, 'critical'):
            raise AttributeError(f'The custom logger must have a <critical> LogTag attribute defined.')
        self._log_tags = value

    @property
    def date_format(self):
        return self._date_format

    @date_format.setter
    def date_format(self, format: str):
        self._date_format = format

    def start(self):
        self._disabled = False
        if self.log_path:
            self._sql = LoggerSql(db_file_name=self._log_path)
            self._threads = {
                self._main_thread.ident: _LogThread(
                    depth=0,
                )
            }

            self._sql.create_database()
            for ll in self._log_tags.get_all():
                self._sql.log_tags.insert(
                    name=ll.name, value=ll.value, color=ll.html_color
                )

    @contextmanager
    def generate(self, format_generator: str, **kwargs):
        if self._disabled:
            self.start()
        if self._persistent_logging:
            generators = {
                'html': HtmlLogGenerator
            }
            generator = generators[format_generator]()
            if not self._log_path:
                raise ValueError('Cannot generate persisting logs without a log path.\n'
                                 'Please instantiate the logger with a log path.')
            try:
                if not os.path.exists(self._log_path.parent):
                    file_path = ''
                    for path in self._log_path.parts:
                        file_path += path + os.sep
                        if not os.path.exists(file_path):
                            os.mkdir(file_path)
                yield
            except:
                self.log_exception()
                raise
            finally:
                generator.generate(log_file=self._log_path, **kwargs)
        else:
            try:
                yield
            except:
                self.log_exception()

    def set_rule(self, mode: str = 'all', log_tag: LogTag = None, min_tag_value: int = None,
                 blacklist_tag_names: List[str] = None, blacklist_function: Callable = None,
                 reset: bool = False, why: str = ''):
        if self._disabled:
            return
        log_tag = log_tag or self._log_tags.default
        msg = f'Setting log mode to "{mode}". '
        if blacklist_function:
            msg += f'A function has been defined to decide what is logged.'
        elif min_tag_value:
            if isinstance(min_tag_value, LogTag):
                min_tag_value = min_tag_value.value
            blacklist_function = lambda x: x.value < min_tag_value
            msg += f'Only tag values greater than or equal to {min_tag_value} will be logged.'
        elif blacklist_tag_names:
            blacklist_function = lambda x: x.name in blacklist_tag_names
            msg += f'These tag names are will not be logged: {blacklist_tag_names}'
        elif reset:
            blacklist_function = lambda x: False
            msg += f'Resetting rule. There are no restrictions to logging in this rule.'
        else:
            blacklist_function = lambda x: False
            msg += f'No rule defined. There are no restrictions to logging in this rule.'
        self.log(f'{msg}\n{why}', log_tag=log_tag, num_prev_callers=1)

        thread = threading.current_thread()
        if thread.ident == self._main_thread.ident:
            for thread in self._threads.values():
                thread.mode = mode
                thread.blacklist_function = blacklist_function
        elif lt := self._threads.get(thread.ident):
            lt.mode = mode
            lt.blacklist_function = blacklist_function
        else:
            self._threads[thread.ident] = _LogThread(
                depth=self._threads[self._main_thread.ident].depth,
                blacklist_function=blacklist_function,
                mode=mode
            )

    def wrap_class(self, log_tag: LogTag = None, func_regex_exclude: str = '', mask_input_regexes: List = None,
                   mask_output: bool = False):
        log_tag = log_tag or self._log_tags.default

        def _wrap(cls):
            if self._disabled:
                return cls
            for attr, fn in inspect.getmembers(cls, inspect.isroutine):
                if callable(getattr(cls, attr)) and not fn.__name__.startswith('__'):
                    if func_regex_exclude:
                        matches = re.findall(pattern=func_regex_exclude, string=fn.__name__, flags=re.IGNORECASE)
                        if fn.__name__ in matches:
                            continue

                    if type(cls.__dict__.get(fn.__name__)) in {staticmethod, classmethod}:
                        setattr(cls, attr, self.wrap_func(
                            log_tag=log_tag,
                            is_static_or_classmethod=True,
                            mask_input_regexes=mask_input_regexes,
                            mask_output=mask_output
                        )(getattr(cls, attr)))
                    else:
                        setattr(cls, attr, self.wrap_func(
                            log_tag=log_tag,
                            mask_input_regexes=mask_input_regexes,
                            mask_output=mask_output
                        )(getattr(cls, attr)))
            return cls

        return _wrap

    def wrap_func(self, log_tag: LogTag = None, mask_input_regexes: List = None, mask_output: bool = False,
                  is_static_or_classmethod: bool = False):
        log_tag = log_tag or self._log_tags.default

        def __wrap(func):
            def __wrapper(*args, **kwargs):
                if self._disabled:
                    return func(*args, **kwargs)

                thread = threading.current_thread()
                if not self._threads.get(thread.ident):
                    mt = self._threads.get(self._main_thread.ident, _LogThread())
                    self._threads[thread.ident] = _LogThread(
                        depth=mt.depth,
                        blacklist_function=mt.blacklist_function,
                        mode=mt.mode
                    )

                # Before the function is called.
                try:
                    if is_static_or_classmethod:
                        args = args[1:]
                    params = dict(inspect.signature(func).bind(*args, **kwargs).arguments)  # type: dict
                except TypeError as e:
                    self.log(
                        msg='\n'.join(e.args),
                        log_tag=self._log_tags.critical.value,
                        num_prev_callers=2
                    )
                    raise TypeError(e)

                before_string = 'Called ' + func.__qualname__
                if params:
                    if mask_input_regexes:
                        in_regexes = "(" + ")|(".join(mask_input_regexes) + ")"
                        for key in params.keys():
                            if re.match(pattern=in_regexes, string=key, flags=re.IGNORECASE):
                                params[key] = '********'
                    before_string += '\nArguments:\n' + jsonpickle.dumps(params, max_depth=3, unpicklable=False)
                self.log_method(func=func, msg=before_string, log_tag=log_tag, returning=False)
                self._threads[thread.ident].depth += 1
                try:
                    result = func(*args, **kwargs)

                    # After the function returns.
                    after_string = f'{func.__qualname__} returned.'
                    if result is not None:
                        if mask_output:
                            after_string += ' Output is masked.'
                        else:
                            ret_vals = jsonpickle.dumps(result, max_depth=3, unpicklable=False)
                            after_string += f'\nReturn Values: {ret_vals}'
                    self.log_method(func=func, msg=after_string, log_tag=log_tag, returning=True)

                    return result
                except:
                    self.log_exception()
                    raise
                finally:
                    if self._persistent_logging:
                        self._threads[thread.ident].depth -= 1

            return __wrapper

        return __wrap

    def _commit_log(self, msg: Any, log_tag: LogTag, file_path: str, line_num: int, func: str = None):
        thread = threading.current_thread()
        if (mt := self._threads.get(thread.ident)) is None:
            mt = self._threads.get(self._main_thread.ident, _LogThread())
            self._threads[thread.ident] = _LogThread(
                depth=mt.depth,
                blacklist_function=mt.blacklist_function,
                mode=mt.mode
            )

        if mt.console_enabled:
            print(f'[{log_tag.name}]{self._timestamp()}: {msg}')

        if self._persistent_logging and mt.persistence_enabled:
            with logger_lock:
                self._sql.log_entries.insert(
                    file_path=file_path,
                    function_name=func,
                    line_num=line_num,
                    msg=msg,
                    tag_name=log_tag.name,
                    depth=self._threads[thread.ident].depth,
                    thread_id=thread.ident,
                    thread_name=thread.name,
                    is_main_thread=(thread.ident == self._main_thread.ident)
                )

    def log(self, msg: Any, log_tag: LogTag = None, num_prev_callers: int = 0):
        if self._disabled:
            return
        log_tag = log_tag or self._log_tags.default
        thread = threading.current_thread()
        if lt := self._threads.get(thread.ident):
            if isinstance(lt.blacklist_function, Callable) and lt.blacklist_function(log_tag) is True:
                return

        with logger_lock:
            frame = inspect.currentframe()
        outer_frames = inspect.getouterframes(frame)[num_prev_callers + 1]
        if outer_frames.function == '<module>':
            func = inspect.getmodulename(outer_frames.filename)
        else:
            if (class_name := outer_frames[0].f_locals.get('self')) is not None:
                func = f'{class_name.__class__.__qualname__}.{outer_frames.function}'
            else:
                func = outer_frames.function
        self._commit_log(msg=msg, log_tag=log_tag, file_path=outer_frames[1], line_num=outer_frames[2],
                         func=func)

    def log_exception(self):
        if self._disabled:
            return
        with logger_lock:
            tb = sys.exc_info()[2]

        while True:
            if tb.tb_next is None:
                break
            tb = tb.tb_next
        frame = tb.tb_frame
        outer_frames = inspect.getouterframes(frame)[0]
        source_code, line_num_start = inspect.getsourcelines(outer_frames[0])
        line_num_start = max(line_num_start, 1)
        if outer_frames.function == '<module>':
            func = inspect.getmodulename(outer_frames.filename)
        else:
            if (class_name := outer_frames[0].f_locals.get('self')) is not None:
                func = f'{class_name.__class__.__qualname__}.{outer_frames.function}'
            else:
                func = outer_frames.function
        msg = traceback.format_exc()
        self._commit_log(msg=msg, log_tag=self._log_tags.critical, file_path=outer_frames[1], line_num=outer_frames[2],
                         func=func)

    def log_method(self, func: callable, msg: Any, log_tag: LogTag = None, returning: bool = False):
        if self._disabled:
            return
        log_tag = log_tag or self._log_tags.default
        thread = threading.current_thread()
        if lt := self._threads.get(thread.ident):
            if isinstance(lt.blacklist_function, Callable) and lt.blacklist_function(log_tag) is True:
                return

        source_code, line_num_start = inspect.getsourcelines(func)
        file_path = inspect.getfile(func)
        line_num = line_num_start + len(source_code) - 1 if returning else line_num_start
        self._commit_log(msg=msg, log_tag=log_tag, file_path=file_path, line_num=line_num, func=func.__qualname__)
