.. _codesign_auditing_usage:

Auditing
========

.. note::
    Refer to :ref:`authentication` for ways to authenticate to the TPP WebSDK.

Retrieving Archive Entries
--------------------------

.. code-block:: python

    from pyvenafi.tpp import Authenticate, Features
    from pyvenafi.tpp.api.websdk.models.codesign import ArchiveFilter

    api = Authenticate(...)
    features = Features(api)

    archive_results = features.codesign.auditing.retrieve_archive_entries(
        archive_filter=ArchiveFilter(
            client_library_name='pkcs11'
        ),
        page_size=5,
        page=10
    )
