from typing import List
import os
import sys
import traceback
import inspect
from datetime import datetime
import webbrowser
import json
import jsonpickle
import re
from venafi.tools.logger.log_resources import console_log_color
from venafi.tools.logger.config import LOG_TO_JSON, OPEN_HTML_ON_FINISH, \
    LOG_LEVEL, LOG_DIR, LOG_FILENAME, LOGGING_ENABLED, CUSTOM_LOGLEVEL_PATH, \
    MASK_REGEX_EXPRS

if CUSTOM_LOGLEVEL_PATH is not None:
    import importlib.util
    import os

    spec = importlib.util.spec_from_file_location('LogLevelModule', CUSTOM_LOGLEVEL_PATH)
    _LogLevelModule = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(_LogLevelModule)
    LogLevels = _LogLevelModule.LogLevels
else:
    from venafi.tools.logger.log_resources import LogLevels

jsonpickle.set_encoder_options('json', sort_keys=True, indent=4)

LOG_TIMESTAMP = datetime.now().strftime('%Y%m%d%H%M%S')

LOG_DIRECTORY = LOG_DIR or '%s/logs' % os.path.split(__file__)[0]
LOG_FILE_WITHOUT_EXT = '%s/%s_%s' % (LOG_DIRECTORY, LOG_FILENAME, LOG_TIMESTAMP)
if LOGGING_ENABLED and not os.path.exists(LOG_DIRECTORY):
    file_path = ''
    for path in LOG_DIRECTORY.split(os.sep):
        file_path += path + os.sep
        if not os.path.exists(file_path):
            os.mkdir(file_path)


def singleton(cls):
    instances = {}

    def _singleton(*args, **kwargs):
        if cls not in instances:
            instances[cls] = cls(*args, **kwargs)
        return instances[cls]

    return _singleton


def initialize_logger(cls, *args, **kwargs):
    def decorate():
        if not LOGGING_ENABLED:
            def _disable_everything(func):
                def __disable_everything(self, *args, **kwargs):
                    return

                return __disable_everything

            for attr, fn in inspect.getmembers(cls, inspect.isroutine):
                if callable(getattr(cls, attr)) and not fn.__name__.startswith('__'):
                    setattr(cls, attr, _disable_everything(getattr(cls, attr)))
        return cls(*args, **kwargs)

    return decorate


@initialize_logger
@singleton
class Logger:
    def __init__(self):
        self.log = self._log
        self.log_method = self._log_method
        self.log_exception = self._log_exception

        self._disabled_at_level = -1
        self._depth = []

    def no_op(self, *args, **kwargs):
        pass

    def disable_all_logging(self, level: int = LogLevels.high.level, why: str = '', func_obj=None, reference_lastlineno: bool = False):
        if level < self._disabled_at_level:
            return

        self._disabled_at_level = level
        if func_obj:
            self._log_method(func_obj=func_obj, msg=why, level=level, reference_lastlineno=reference_lastlineno)
        else:
            self._log(f'Disabling all logging. {why}', level=level, prev_frames=2)
        self.log = self.no_op
        self.log_method = self.no_op
        self.log_exception = self.no_op

    def enable_all_logging(self, level: int = LogLevels.high.level, why: str = '', func_obj=None, reference_lastlineno: bool = False):
        if self._disabled_at_level > level:
            return

        self.log = self._log
        self.log_method = self._log_method
        self.log_exception = self._log_exception
        self._disabled_at_level = -1
        if func_obj:
            self._log_method(func_obj=func_obj, msg=why, level=level, reference_lastlineno=reference_lastlineno)
        else:
            self._log(f'Enabling all logging. {why}', level=level, prev_frames=2)

    def wrap(self, level: int = LogLevels.high.level, masked_variables: List = []):
        def _wrap(func):
            def __wrapper(*args, **kwargs):
                func_id = id(func)

                def truncate_depth():
                    indexes = [i for i, e in enumerate(self._depth) if e == func_id]
                    if indexes:
                        self._depth = self._depth[:indexes[-1]]

                # Before the function is called.
                try:
                    params = dict(inspect.signature(func).bind(*args, **kwargs).arguments)
                except TypeError as e:
                    self.log(
                        msg='\n'.join(e.args),
                        level=LogLevels.critical.level,
                        prev_frames=2
                    )
                    raise TypeError(e)

                if 'self' in params.keys():
                    del params['self']
                before_string = 'Called ' + func.__qualname__
                if params:
                    for key in params.keys():
                        regexes = "(" + ")|(".join(set(MASK_REGEX_EXPRS + masked_variables)) + ")"
                        if re.match(pattern=regexes, string=key, flags=re.IGNORECASE):
                            params[key] = '********'
                    before_string += '\nArguments:\n' + jsonpickle.dumps(params, max_depth=3, unpicklable=False)
                self.log_method(func_obj=func, msg=before_string, level=level, reference_lastlineno=False)

                truncate_depth()
                self._depth.append(func_id)

                try:
                    result = func(*args, **kwargs)

                    # After the function returns.
                    after_string = f'{func.__qualname__} returned.'
                    if result is not None:
                        ret_vals = jsonpickle.dumps(result, max_depth=3, unpicklable=False)
                        after_string += f'\nReturn Values: {ret_vals}'
                    self.log_method(func_obj=func, msg=after_string, level=level, reference_lastlineno=True)

                    return result
                except:
                    self.log_exception()
                    raise
                finally:
                    truncate_depth()

            return __wrapper

        return _wrap

    @staticmethod
    def log_to_html():
        if not LOGGING_ENABLED:
            print(f'Cannot open log file because LOGGING_ENABLED = False.')
            return

        json_file = f'{LOG_FILE_WITHOUT_EXT}.json'
        if not os.path.exists(json_file):
            print(f'Cannot open "{json_file}" because it does not exist.')
            return

        log_item_counter = 0
        json_output = []
        with open(json_file, 'r') as f:
            for line in f.readlines():
                json_output.append(dict(json.loads(line)))

        if not isinstance(json_output, list):
            json_output = [json_output]

        def add_legend_item(id, value, text, fgcolor, bgcolor, checked='checked'):
            return """
            <div class='legend-item'>    
                <label class='checkbox-label'>
                    <input id='{id}' class='filter' value={value} type='checkbox' {checked} onchange='filterLogs()'>
                    <span class='checkbox-custom rectangular' style='cursor: pointer;'></span>
                </label>
                <div class='input-title' style='background-color: {bgcolor}; color: {fgcolor}; cursor: default; width: auto'>{text}</div>
            </div>    
            """.format(id=id, value=value, text=text, fgcolor=fgcolor, bgcolor=bgcolor, checked=checked)

        legend = ''
        for key, value in LogLevels.as_dictionary().items():
            legend += add_legend_item(id='log-level-{level}-cb'.format(level=value.level), value=value.level, text=value.name,
                                      fgcolor='black', bgcolor=value.colors.html)
        legend += add_legend_item(id='pin-cb', value='-1', text='Pin Only', fgcolor='white', bgcolor='#0077FF', checked='')

        node_value = 0
        rows = ''
        for index, output in enumerate(json_output):
            file_text_color = LogLevels.as_dictionary().get(output['log_level'])
            file_text_color = 'orange' if not file_text_color else file_text_color.colors.html

            if index + 1 < len(json_output) and json_output[index + 1]['depth'] > output['depth']:
                node_value += 1
                node = f"""
                <span 
                    id='node-{node_value}' 
                    class='log-item node ellipsis' 
                    value={node_value}
                    onClick=toggleNodes({node_value})
                ></span>"""

                rows += f"<div class='node-container-{node_value}'>" * (json_output[index + 1]['depth'] - output['depth'])
            else:
                node = ''

            rows += """
            <div 
                class='log-item-container log-level-{log_level}' 
                value='{log_level}'
                style="position: relative; width: calc(100% - (25px * {depth})); left: calc(25px * {depth})" 
            >
                <div id='log-{counter}' class='log-item-row-1'>
                    {node}
                    <span id='exp-{counter}' class='log-item exp' onClick=togglePlusMinus({counter})>+</span>
                    <span id='pin-{counter}' class='log-item pin unpinned' onClick='toggleMark(this.id, {counter})'>Pin</span>
                    <span class='log-item line-info' style='background-color: {ftc};'>{filename}: {lineno}</span>
                    <span id='log-text-{counter}' class='log-item log-text' style='white-space: nowrap'>{text}</span>
                </div>
                <div id='source-{counter}' class='log-item-row-2' style='display: none'>
                    <span class='source-code'>{source}</span>
                </div>
            </div>
            """.format(counter=str(log_item_counter), path=output['path'], filename=output['filename'], lineno=output['lineno'],
                       text=output['text'], source=output['source'], ftc=file_text_color, log_level=output['log_level'],
                       depth=output['depth'], node=node)

            if index + 1 < len(json_output) and json_output[index + 1]['depth'] < output['depth']:
                rows += "</div>" * (output['depth'] - json_output[index + 1]['depth'])
            log_item_counter += 1

        f = open('%s.html' % LOG_FILE_WITHOUT_EXT, 'w')

        message = """
        <html>
            <head>
                <script>
                    function toggleAllNodes() {{
                        var nodes = document.querySelectorAll('.node');
                        for(var i=0; i < nodes.length; i++) {{
                            nodes[i].onclick.apply(nodes[i]);
                        }}
                    }}

                    function initialize_document() {{
                        // Collapse all logs
                        toggleAllNodes();

                        // Expand all logs with critical logs.
                        critical_logs = document.querySelectorAll('.log-level-90');
                        for(var i=0; i<critical_logs.length; i++) {{
                            parent = critical_logs[i].parentElement;
                            if(parent.id == "log-container") {{
                                continue;
                            }}
                            node = parent.firstElementChild.querySelector('.node');
                            if(node === null) {{
                                continue;
                            }}
                            node.onclick.apply(node);
                        }}
                    }}

                    function toggleNodes(node_value) {{
                        node_id = document.querySelector("#node-"+node_value);

                        node_id.classList.toggle('arrow-up');
                        node_id.classList.toggle('ellipsis');

                        node_container = node_id.closest(".node-container-"+node_value).firstElementChild;
                        for(var child=node_container.nextElementSibling; child!==null; child=child.nextElementSibling) {{
                            child.classList.toggle('hide');
                        }}
                    }}

                    function togglePlusMinus(counter) {{
                        exp_el = document.getElementById('exp-'+counter);
                        text = document.getElementById('log-text-'+counter);
                        source = document.getElementById('source-'+counter);
                        log = document.getElementById('log-'+counter);
                        sign = exp_el.innerHTML;
                        if(sign === '+') {{
                            text.style.whiteSpace = 'pre-wrap';
                            text.style.overflowWrap = 'break-word';
                            text.style.wordWrap = 'break-word';
                            text.style.overflowY = 'auto';
                            source.style.display = 'flex';
                            log.style.borderRadius = '5px 5px 0px 0px';
                            exp_el.innerHTML = '-';
                            exp_el.style.background = 'linear-gradient(-45deg, #07D, transparent)';
                        }}
                        else {{
                            text.style.whiteSpace = 'nowrap';
                            text.style.overflowWrap = 'unset';
                            text.style.wordWrap = 'unset';
                            text.style.overflowY = 'hidden';
                            source.style.display = 'none';
                            log.style.borderRadius = '5px';
                            exp_el.innerHTML = '+';
                            exp_el.style.background = 'none';
                        }}                    
                    }}

                    function filterLogs() {{
                        let filters = document.querySelectorAll('.filter');
                        let all_logs = document.querySelectorAll('.log-item-container');
                        let display_filters = []
                        for(var i=0; i < filters.length; i++) {{
                            if(filters[i].checked) {{
                                display_filters.push(filters[i].value);
                            }}
                        }}

                        // Pinned filter overrides all other filters.
                        if(display_filters.includes('-1')) {{
                            // Disable other filters.
                            legend_items = document.querySelectorAll('.legend-item');
                            for(var i=0; i < legend_items.length; i++) {{
                                if(legend_items[i].querySelector('.filter').value != -1) {{
                                    legend_items[i].style.opacity = 0.5;
                                    legend_items[i].style.pointerEvents = 'none';
                                }}
                            }}

                            // Filter logs.
                            for(var i=0; i < all_logs.length; i++) {{
                                is_filtered = !(all_logs[i].querySelectorAll('.unpinned').length == 0);

                                if(is_filtered) {{
                                    if(!all_logs[i].classList.contains('filtered')) {{
                                        all_logs[i].classList.add('filtered');
                                    }}
                                }} else {{
                                    if(all_logs[i].classList.contains('filtered')) {{
                                        all_logs[i].classList.remove('filtered');
                                    }}
                                }}
                            }}

                        }} else {{ // All other filters.
                            // Enable all filters.
                            legend_items = document.querySelectorAll('.legend-item');
                            for(var i=0; i < legend_items.length; i++) {{
                                legend_items[i].style.opacity = 1;
                                legend_items[i].style.pointerEvents = 'all';
                            }}

                            // Filter logs.
                            for(var i=0; i < all_logs.length; i++) {{
                                is_filtered = !display_filters.includes(all_logs[i].getAttribute('value'));

                                if(is_filtered) {{
                                    if(!all_logs[i].classList.contains('filtered')) {{
                                        all_logs[i].classList.add('filtered');
                                    }}
                                }} else {{
                                    if(all_logs[i].classList.contains('filtered')) {{
                                        all_logs[i].classList.remove('filtered');
                                    }}
                                }}
                            }}
                        }}
                    }}

                    function toggleMark(id, counter) {{
                        h = document.getElementById(id);
                        h.classList.toggle('unpinned')
                    }}
                </script>
                <style>
                    .hide {{
                        display: none;
                    }}

                    .filtered {{
                        display: none;
                    }}

                    .ellipsis:after {{
                        content: '\\2026'
                    }}

                    .arrow-up:after {{
                        content: '\\21E7'
                    }}

                    .btn {{
                        height: 25px;
                        border-radius: 5px;
                        border: outset lightgrey 2px;
                        color: #4d4d4d;
                        font-weight: 600;
                        font-size: 0.8em;
                        min-width: 125px !important;
                    }}

                    #controls-container {{    
                        width: 100%;
                        min-height: 50px;
                        display: flex;
                        align-items: center;
                    }}

                    body {{
                        width: 90%;
                        margin: 0 auto;
                    }}

                    #page-title {{
                        color: grey;
                        text-align: center;
                    }}

                    #log-container {{
                        width: 100%;
                        font-size: medium;
                    }}

                    .log-item-row-1 {{
                        height: auto;
                        display: flex;
                        border: solid lightgrey 2px;
                        border-radius: 5px;
                        margin: 2px 2px 0px 2px;
                    }}

                    .log-item-row-2 {{
                        margin: 0px 2px 0px 2px;
                        white-space: pre-wrap;
                        display: flex;
                        justify-content: center;
                        border: solid lightgrey;
                        border-width: 0px 2px 2px 2px;
                        border-radius: 0px 0px 5px 5px;
                        background-color: whitesmoke;
                        padding: 30px;
                        max-height: 500px;
                        overflow: auto;
                    }}

                    .log-item {{
                        display: inline-flex;
                        align-items: center;
                        justify-content: center;
                    }}

                    .node {{
                        min-width: 40px !important;
                        border-right: solid lightgrey 2px;
                        text-align: center;
                        cursor: pointer;
                        font-size: small;
                        color: slategrey;
                    }}

                    .exp {{
                        min-width: 40px !important;
                        border-right: solid lightgrey 2px;
                        text-align: center;
                        cursor: pointer;
                    }}

                    .pin {{
                        min-width: 40px !important;
                        border-right: solid lightgrey 2px;
                        text-align: center;
                        cursor: pointer;
                        background-color: #0077FF;
                        opacity: 1;
                        color: white;
                    }}

                    .unpinned {{
                        background-color: inherit;
                        opacity: 0.5;
                        color: black;
                    }}

                    .line-info {{
                        text-align: center;
                        padding-left: 10px;
                        padding-right: 10px;
                        border-right: solid lightgrey 2px;
                        min-width: 200px !important;
                    }}

                    .log-text {{
                        display: inline-block;
                        max-height: 500px;
                        width: 100%;
                        padding-left: 10px;
                        text-overflow: ellipsis;
                        overflow-x: hidden;
                    }}

                    .source-code {{
                        width: 100%;
                    }}

                    /* Styling Checkbox Starts */
                    #legend-title {{
                        text-align: center;
                        width: 100%;
                        margin: auto;
                        margin-bottom: 10px;
                        color: #444;
                    }}

                    #legend-container {{
                        width: 90%;
                        margin: 0 auto;
                    }}

                    #legend {{
                        border-radius: 5px;
                        display: flex;
                        flex-wrap: wrap;
                        justify-content: space-evenly;
                        width: 75%;
                        margin: 30px auto;
                        border: solid lightgrey 2px;
                        padding: 10px;
                    }}

                    .legend-item {{
                        height: 45px;
                        width: auto;
                        display: block;
                    }}

                    .input-title {{
                        display: inline-block;
                        width: 50%;
                        text-align: center;
                        margin-left: 6px;
                        font-size: medium; 
                    }}

                    .checkbox-label {{
                        display: inline-block;
                        position: relative;
                        height: 24px;
                        width: 24px;
                        clear: both;
                        top: 4px;
                    }}

                    .checkbox-label input {{
                        position: absolute;
                        opacity: 0;
                        cursor: pointer;
                    }}

                    .checkbox-label .checkbox-custom {{
                        position: absolute;
                        top: 0px;
                        left: 0px;
                        height: 24px;
                        width: 24px;
                        background-color: transparent;
                        border-radius: 5px;
                        transition: all 0.3s ease-out;
                        -webkit-transition: all 0.3s ease-out;
                        -moz-transition: all 0.3s ease-out;
                        -ms-transition: all 0.3s ease-out;
                        -o-transition: all 0.3s ease-out;
                        border: 2px solid #888;
                    }}


                    .checkbox-label input:checked ~ .checkbox-custom {{
                        background-color: #FFFFFF;
                        border-radius: 5px;
                        -webkit-transform: rotate(0deg) scale(1);
                        -ms-transform: rotate(0deg) scale(1);
                        transform: rotate(0deg) scale(1);
                        opacity:1;
                        border: 2px solid #888;
                    }}


                    .checkbox-label .checkbox-custom::after {{
                        position: absolute;
                        content: '';
                        left: 12px;
                        top: 12px;
                        height: 0px;
                        width: 0px;
                        border-radius: 5px;
                        border: solid #009BFF;
                        border-width: 0 3px 3px 0;
                        -webkit-transform: rotate(0deg) scale(0);
                        -ms-transform: rotate(0deg) scale(0);
                        transform: rotate(0deg) scale(0);
                        opacity:1;
                        transition: all 0.3s ease-out;
                        -webkit-transition: all 0.3s ease-out;
                        -moz-transition: all 0.3s ease-out;
                        -ms-transition: all 0.3s ease-out;
                        -o-transition: all 0.3s ease-out;
                    }}


                    .checkbox-label input:checked ~ .checkbox-custom::after {{
                      -webkit-transform: rotate(45deg) scale(1);
                      -ms-transform: rotate(45deg) scale(1);
                      transform: rotate(45deg) scale(1);
                      opacity:1;
                      left: 8px;
                      top: 3px;
                      width: 6px;
                      height: 12px;
                      border: solid #009BFF;
                      border-width: 0 2px 2px 0;
                      background-color: transparent;
                      border-radius: 0;
                    }}



                    /* For Ripple Effect */
                    .checkbox-label .checkbox-custom::before {{
                        position: absolute;
                        content: '';
                        left: 10px;
                        top: 10px;
                        width: 0px;
                        height: 0px;
                        border-radius: 5px;
                        border: 2px solid #888;
                        -webkit-transform: scale(0);
                        -ms-transform: scale(0);
                        transform: scale(0);    
                    }}

                    .checkbox-label input:checked ~ .checkbox-custom::before {{
                        left: -3px;
                        top: -3px;
                        width: 24px;
                        height: 24px;
                        border-radius: 5px;
                        -webkit-transform: scale(3);
                        -ms-transform: scale(3);
                        transform: scale(3);
                        opacity:0;
                        z-index: 999;
                        transition: all 0.3s ease-out;
                        -webkit-transition: all 0.3s ease-out;
                        -moz-transition: all 0.3s ease-out;
                        -ms-transition: all 0.3s ease-out;
                        -o-transition: all 0.3s ease-out;
                    }}

                </style>
                <title>Testing Log</title>
            </head>
            <body onload="initialize_document();">
                <h1 id='page-title'>TESTING LOG</h1>
                <div id='legend-container'>
                    <div id='legend'>
                        <h3 id='legend-title'>Log Filter</h3>
                        {legend}
                    </div>
                </div>
                <div id='controls-container'>
                    <button id='expand-btn' class='btn' onclick="toggleAllNodes();">Toggle All Logs</button>
                </div>
                <div id='log-container'>
                    {rows}
                </div>
            </body>
            {empty_spaces}
        </html>
        """.format(legend=legend, rows=rows, empty_spaces='<br/>' * 12)

        f.write(message)
        f.close()

        if OPEN_HTML_ON_FINISH is True:
            webbrowser.open_new_tab('file://%s.html' % LOG_FILE_WITHOUT_EXT)

    def _create_log(self, msg: str, level: int, outerframes: inspect.FrameInfo = None, skip_console: bool = False,
                    html_formatted_msg: str = None, func_obj=None, reference_lastlineno: bool = False):
        if outerframes:
            source, startlineno = inspect.getsourcelines(outerframes[0])
            path, lineno = outerframes[1], str(outerframes[2])
            filepath, filename = os.path.split(path)

        elif func_obj:
            source, startlineno = inspect.getsourcelines(func_obj)
            path = inspect.getfile(func_obj)
            lineno = startlineno + len(source) - 1 if reference_lastlineno else startlineno
            filepath, filename = os.path.split(path)

        else:
            raise ValueError('Must supply either "outerframes" or "func_obj".')

        if not skip_console and level >= LOG_LEVEL:
            file_text_color = LogLevels.as_dictionary().get(level)
            if not file_text_color:
                file_text_color = LogLevels.high.colors.console
            else:
                file_text_color = file_text_color.colors.console

            file_text = '{color}File "{path}", line {lineno}{end}'.format(
                color=file_text_color, path=path, lineno=lineno, end=console_log_color(0, 0, 0)
            )
            print(file_text + str(msg))

        if LOG_TO_JSON is True:
            json_msg = html_formatted_msg or msg
            source = ''.join(['%s:\t%s' % (x + startlineno, y) for x, y in enumerate(source)])
            with open('%s.json' % LOG_FILE_WITHOUT_EXT, 'a+') as f:
                json.dump({
                    "path": path,
                    "filename": filename,
                    "lineno": lineno,
                    "text": str(json_msg),
                    "source": source,
                    "log_level": level,
                    "depth": len(self._depth)
                }, f)
                f.write('\n')

    def _log(self, msg: str, level: int = LogLevels.high.level, critical: bool = False, prev_frames: int = 1):
        frame = inspect.currentframe()
        outerframes = inspect.getouterframes(frame)[prev_frames]
        self._create_log(msg=msg, outerframes=outerframes, level=level if not critical else LogLevels.critical.level)

    def _log_exception(self, skip_console=True):
        tb = sys.exc_info()[2]
        while True:
            if tb.tb_next is None:
                break
            tb = tb.tb_next
        frame = tb.tb_frame
        outerframes = inspect.getouterframes(frame)[0]
        msg = traceback.format_exc()
        html_msg = '<span style="white-space: pre-wrap; color: red">%s</span>' % msg
        self._create_log(msg=msg, outerframes=outerframes, level=LogLevels.critical.level,
                         skip_console=skip_console, html_formatted_msg=html_msg)

    def _log_method(self, func_obj, msg: str, level: int = LogLevels.high.level, reference_lastlineno: bool = False):
        self._create_log(msg=msg, func_obj=func_obj, level=level, reference_lastlineno=reference_lastlineno)
