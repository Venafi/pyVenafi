"""
The Venafi Logger is a singleton class that enforces all callers to use the same
instance of the logger. This allows this logger to affect all logging everywhere,
so be responsible when using it.

Must-Know Methods
-----------------

``log()``
'''''''''
Logs the given message with the given level. The level defaults to main
and should only be changed if either the message is critical or an API or Feature
log is being written. If the message is critical, use
``logger.log(msg=msg, level=LogLevels.critical)``

``log_exception()``
'''''''''''''''''''
Logs exceptions caught in Python. This MUST be used wherever the
main file exists in a try/except clause. This is because it is not designed to listen
to the program for exceptions. It is, instead, designed to explicitly log errors. Here
is an example:

.. code-block:: python

    from venafi.logger import logger, LOG_TO_JSON
    # Other imports here

    def main():
        # Execute stuff here.
        return

    if __name__ == '__main__':
        try:
            main()
        except Exception as e:
            # No need to pass e because log_exception() uses `inspect` to find the
            # exception in the stack trace.
            logger.log_exception()
            raise
        finally:
            # Create the html file from the JSON log file.
            logger.log_to_html()

``enable_all_logging()``
''''''''''''''''''''''''
Enables all logging given that the directive was given at a higher log level then the directive
given to disable the logging in the first place. For example, if logging was disabled at the
Feature level, then it cannot be enabled at the API level because it is a lower level then the
Feature level. Only the Feature level and higher (such as Main and Critical) can re-enable all
logging. A ``why`` parameter is available to suggested why the call was made to re-enable logging.

``disable_all_logging()``
'''''''''''''''''''''''''
Disable all logging at the level that the directive was given. If the directive is
given at a level lower then the current disabled log level, then it is ignored. All log
methods are converted into "no operations", which when called simply return nothing. A
``why`` parameter is available to suggested why the call was made to re-enable logging.

Must-Know Configurations
------------------------

In order to see a complete list of these configurations, see `venafi/tools/logger/config.py`.

Environment Variables
    * ``VENAFI_PY_LOGGING_ENABLED``
        Defaults to ``True``.
        Must be one of True or False (case insensitive). If disabled, all logging will be disabled
        permanently. This can enhance performance as every log method becomes a "no operation".
    * ``VENAFI_PY_LOG_DIR``
        Defaults to 'venafi/tools/logger/logs'.
        Must be the absolute path to the log directory. If the log directory does not exist, the
        logger will create it.
    * ``VENAFI_PY_LOG_FILENAME``
        Defaults to 'venafi_py_logfile'.
        The logger will always append a timestamp to the name of the log file. This is the name
        of the JSON and HTML log files.
    * ``VENAFI_PY_LOG_LEVEL``
        Defaults to ``LogLevels.api``.
        All message at and above this level are logged to the console. This does not affect logs
        to the JSON file as those can be manually filtered or filtered in the provided HTML generator.
    * ``VENAFI_PY_LOG_TO_JSON``
        Defaults to ``True``.
        Must be one of True or False (case insensitive). If this is False, then VENAFI_PY_OPEN_HTML
        has not effect.
    * ``VENAFI_PY_OPEN_HTML``
        Defaults to ``False``.
        Must be one of True or False (case insensitive). If this is True, the HTML file that is
        generated will automatically open when the main file returns. This should not be set to
        True in cases where the log file is moved after execution.
"""
from venafi.tools.logger.logger import LogLevels, Logger
from venafi.tools.logger.config import *

logger = Logger()
