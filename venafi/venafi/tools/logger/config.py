import os
from venafi.tools.logger.log_resources import LogLevels


# >>>>>>>>>> LOGGING VARIABLES <<<<<<<<<< #
LOGGING_ENABLED = eval(str(os.getenv('VENAFI_PY_LOGGING_ENABLED', True)).title())
LOG_DIR = os.getenv('VENAFI_PY_LOG_DIR', '.')
LOG_FILENAME = os.getenv('VENAFI_PY_LOG_FILENAME', 'venafi_py_logfile')
LOG_LEVEL = int(os.getenv('VENAFI_PY_LOG_LEVEL', LogLevels.low.level))
LOG_TO_JSON = eval(str(os.getenv('VENAFI_PY_LOG_TO_JSON', True)).title())  # If this is False, then OPEN_HTML_ON_FINISH will not be evaluated.
OPEN_HTML_ON_FINISH = eval(str(os.getenv('VENAFI_PY_OPEN_HTML', False)).title())
CUSTOM_LOGLEVEL_PATH = os.getenv('VENAFI_PY_CUSTOM_LOGLEVEL_PATH', None)
MASK_REGEX_EXPRS = os.getenv('VENAFI_PY_MASK_REGEX_EXPRS', []) + [
    'password',
    '.*private.*key.*'
]
