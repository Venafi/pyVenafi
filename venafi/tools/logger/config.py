import os
from venafi.tools.logger.log_resources import LogLevels, TextStyle, ForegroundColors, BackgroundColors


# >>>>>>>>>> LOGGING VARIABLES <<<<<<<<<< #
LOGGING_ENABLED = eval(str(os.getenv('VENAFI_PY_LOGGING_ENABLED', True)).title())
LOG_DIR = os.getenv('VENAFI_PY_LOG_DIR', '')
LOG_FILENAME = os.getenv('VENAFI_PY_LOG_FILENAME', 'venafi_py_logfile')
LOG_LEVEL = int(os.getenv('VENAFI_PY_LOG_LEVEL', LogLevels.api))
LOG_TO_JSON = eval(str(os.getenv('VENAFI_PY_LOG_TO_JSON', True)).title())  # If this is False, then OPEN_HTML_ON_FINISH will not be evaluated.
OPEN_HTML_ON_FINISH = eval(str(os.getenv('VENAFI_PY_OPEN_HTML', False)).title())

# Log color variables require a tuple: (TextStyle, Foreground Color, Background Color)
LOG_API_COLOR = (TextStyle.italics, ForegroundColors.yellow, BackgroundColors.transparent)
LOG_CRITICAL_COLOR = (TextStyle.underline, ForegroundColors.red, BackgroundColors.transparent)
LOG_FEATURE_COLOR = (TextStyle.italics, ForegroundColors.cyan, BackgroundColors.transparent)
LOG_TEST_COLOR = (TextStyle.bold, ForegroundColors.purple, BackgroundColors.transparent)
