.. _using_the_logger:

To use the logger, call ``from pytpp import logger`` and then ``logger.start()``. If enabled,
the logger can persist logs in a local SQLite database and even create an HTML file showing
the logs (it is thread safe!). To enable persistent logging, see this `example <https://gitlab.com/tspens/dblogging/-/blob/master/examples/test.py>`_.

This module uses `dblogging <https://pypi.org/project/dblogging>`_. Click the
link for details on how it works.

Using The Logger
================

.. automodule:: pytpp.logger
   :members:
   :undoc-members:
   :show-inheritance:

