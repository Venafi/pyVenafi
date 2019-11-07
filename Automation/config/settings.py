import os
from datetime import datetime
from tools.logger.log_resources import LogLevels


LOG_LEVEL = os.getenv('LOG_LEVEL', LogLevels.api)
LOG_TIMESTAMP = datetime.now().strftime('%Y%m%d%H%M%S')
LOG_TO_JSON = True  # If this is False, then OPEN_HTML_ON_FINISH will not be evaluated.
OPEN_HTML_ON_FINISH = True


TPP_HOST = os.getenv('TPP_HOST', '192.168.7.157')
# TPP_HOST = os.getenv('TPP_HOST', '10.1.91.101')
