from dblogging.logger import Logger
from dblogging.config import LogTag, LogTagTemplate


class LogTags(LogTagTemplate):
    """
    API: 10
    """
    api = LogTag(
        name='API',
        value=10,
        html_color='palegoldenrod'
    )
    #: Name=Feature
    #: Value=20
    feature = LogTag(
        name='Feature',
        value=20,
        html_color='lightcyan'
    )
    #: Name=Main
    #: Value=30
    default = LogTag(
        name='Main',
        value=30,
        html_color='hotpink'
    )
    #: Name=Critical
    #: Value=40
    critical = LogTag(
        name='Critical',
        value=90,
        html_color='red'
    )


logger = Logger()
logger.log_tags = LogTags
