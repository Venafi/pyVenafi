from tools.logger.logger import LogLevels, Logger


class _Logger:
    def __init__(self):
        self.main_logger = Logger(LogLevels.main)
        self.feature_logger = Logger(LogLevels.feature)
        self.api_logger = Logger(LogLevels.api)

    def disable_all_logging(self):
        self.main_logger.log('Disabling all logging.')
        self.main_logger.disable_all_logging()
        self.feature_logger.disable_all_logging()
        self.api_logger.disable_all_logging()

    def enable_all_logging(self):
        self.main_logger.enable_all_logging()
        self.feature_logger.enable_all_logging()
        self.api_logger.enable_all_logging()
        self.main_logger.log('Enabling all logging.')


logger = _Logger()
