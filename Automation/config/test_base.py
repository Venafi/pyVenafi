from datetime import datetime
from tools.logger.logger import Logger, LogLevels


class TestBase:
    logger = Logger(LogLevels.test)
    timestamp = datetime.now().strftime('%Y%m%d%H%M%S')