import os
from datetime import datetime
from tools.logger.log_resources import LogLevels, TextStyle, ForegroundColors, BackgroundColors


# >>>>>>>>>> TPP VARIABLES <<<<<<<<<< #
TPP_HOST = os.getenv('TPP_HOST', '0.0.0.0')


# >>>>>>>>>> LOGGING VARIABLES <<<<<<<<<< #
LOG_LEVEL = os.getenv('LOG_LEVEL', LogLevels.api)
LOG_TIMESTAMP = datetime.now().strftime('%Y%m%d%H%M%S')
LOG_TO_JSON = True  # If this is False, then OPEN_HTML_ON_FINISH will not be evaluated.
OPEN_HTML_ON_FINISH = True

# Log color variables require a tuple: (TextStyle, Foreground Color, Background Color)
LOG_API_COLOR = (TextStyle.italics, ForegroundColors.yellow, BackgroundColors.transparent)
LOG_CRITICAL_COLOR = (TextStyle.underline, ForegroundColors.red, BackgroundColors.transparent)
LOG_FEATURE_COLOR = (TextStyle.italics, ForegroundColors.cyan, BackgroundColors.transparent)
LOG_TEST_COLOR = (TextStyle.bold, ForegroundColors.purple, BackgroundColors.transparent)
