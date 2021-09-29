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
    logger.add_log_tags(CustomLogTags)
    logger.start()

Refer to the logboss documentation for further customization.

"""
from logboss import Logger, LogTagTypes
from logboss.logger import _LoggerPickler

MASKED_REGEXES = [
    '.*password.*',
    '.*token.*',
    '.*private.*key.*',
    'self',
    'cls',
    'apikey',
]

class LogTags:
    api = LogTagTypes.Debug(name='API')
    feature = LogTagTypes.Info(name='Feature')


logger = Logger()
logger.add_log_tags(LogTags)
_LoggerPickler.MASKED_REGEXES = MASKED_REGEXES
