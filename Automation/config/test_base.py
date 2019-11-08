from datetime import datetime
from tools.logger.logger import Logger
from tools.logger.log_resources import LogLevels


class TestBase:
    logger = Logger(LogLevels.test)
    timestamp = datetime.now().strftime('%Y%m%d%H%M%S')