from dblogging.logger import Logger
from dblogging.config import LogTag, LogTagTemplate


class LogTags(LogTagTemplate):
    api = LogTag(
        name='API',
        value=10,
        html_color='palegoldenrod'
    )

    feature = LogTag(
        name='Feature',
        value=20,
        html_color='lightcyan'
    )

    default = LogTag(
        name='Main',
        value=30,
        html_color='hotpink'
    )

    critical = LogTag(
        name='Critical',
        value=90,
        html_color='red'
    )


logger = Logger()
logger.log_tags = LogTags
