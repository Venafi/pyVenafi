"""
Logging is not enabled by default. It must be explicitly enabled by importing it
and calling ``start()`` at the beginning of the program. The logger has
custom-defined log tags:

    * **API:** Only used for WebSDK and Aperture API calls.
    * **Feature:** Only used for feature methods that call the APIs.
    * **Main:** Not used in this code. This is meant to be used by the programmer.
      This value can be overridden.
    * **Critical:** Used during exceptions.

Examples Of Using The Logger
''''''''''''''''''''''''''''

**Using The Logger As Is**

.. code-block:: python

    from pytpp import logger

    logger.log_path = f'{log_dir}/my_logs.db'
    logger.start()

    with logger.generate('html', title = 'My Logs'):
        # Do stuff here. After this context is complete an HTML file is generated
        # with the given title in the same location as the db log file.
        ...


**Customizing Log Tags**

.. code-block:: python

    from pytpp import logger, LogTags, LogTag

    class CustomLogTags(LogTags):
        custom_tag = LogTag(
            name='Custom Tag',
            value=75,
            html_color='#88FF00'
        )

    logger.log_path = f'{log_dir}/my_logs.db'
    logger.log_tags = CustomLogTags
    logger.start()

Refer to the dblogging documentation for further customization.

"""
from dblogging.logger import Logger
from dblogging.config import LogTag, LogTagTemplate


class LogTags(LogTagTemplate):
    #: * **Name** - API
    #: * **Value** - 10
    api = LogTag(
        name='API',
        value=10,
        html_color='palegoldenrod'
    )
    #: * **Name** - Feature
    #: * **Value** - 20
    feature = LogTag(
        name='Feature',
        value=20,
        html_color='lightcyan'
    )
    #: * **Name** - Main
    #: * **Value** - 30
    default = LogTag(
        name='Main',
        value=30,
        html_color='hotpink'
    )
    #: * **Name** - Critical
    #: * **Value** - 40
    critical = LogTag(
        name='Critical',
        value=90,
        html_color='red'
    )


logger = Logger()
logger.log_tags = LogTags
