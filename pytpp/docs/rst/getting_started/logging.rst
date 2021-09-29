.. _using_the_logger:

To use the logger, call ``from pytpp import logger`` and then ``logger.start()``. If enabled,
the logger can persist logs in a local SQLite database and even create an HTML file showing
the logs (it is thread safe!). To enable persistent logging, see this `example <https://gitlab.com/tspens/logboss/-/blob/master/examples/test.py>`_.

This module uses `logboss <https://pypi.org/project/logboss>`_. Click the
link for details on how it works.

Using The Logger
================

.. automodule:: pytpp.logger
   :members:
   :undoc-members:
   :show-inheritance:

