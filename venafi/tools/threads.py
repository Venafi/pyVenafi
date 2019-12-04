from queue import Queue
import threading
from tools.logger.logger import Logger, LogLevels


class _LogThread(threading.Thread):
    """LogThread should always e used in preference to threading.Thread.

    The interface provided by LogThread is identical to that of threading.Thread,
    however, if an exception occurs in the thread the error will be logged
    (using logging.exception) rather than printed to stderr.

    This is important in daemon style applications where stderr is redirected
    to /dev/null.
    """
    def __init__(self, **kwargs):
        threading.Thread.__init__(self, **kwargs)
        self._logger = Logger(LogLevels.feature)
        self._real_run = self.run
        self.run = self._wrap_run
        self.exc_raised = False

    def _wrap_run(self):
        try:
            self._real_run()
        except Exception as e:
            self._logger.log_exception(skip_console=False)
            self.exc_raised = True


class Thread:
    _queue = Queue()

    @classmethod
    def create_thread(cls, func, *args, **kwargs):
        temp_func = lambda q, *args, **kwargs: q.put(func(*args, **kwargs))
        return _LogThread(target=temp_func, args=(cls._queue,) + args, kwargs=kwargs)

    @classmethod
    def run_threads(cls, threads):
        for thread in threads:
            thread.start()

        for thread in threads:
            thread.join()

        for thread in threads:
            if thread.exc_raised:
                raise AssertionError('Not all threads executed properly.')

        result = []
        while not cls._queue.empty():
            result.append(cls._queue.get())
        return result