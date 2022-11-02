.. _tpp-requirements:

Requirements
============

* Python >= 3.8
* Access to an OAuth API Application Integration. You can create a customized API Application Integration in Aperture for the |TPP Module|,
  which is documented
  `here <https://docs.venafi.com/Docs/current/TopNav/Content/API-ApplicationIntegration/t-APIAppIntegrations-creatingNew-Aperture.php>`_.
  Here is an example JSON that can be uploaded when creating a new API Application Integration in Aperture:

.. code-block:: json

    {
        "id"         : "pyVenafi",
        "name"       : "Venafi Python SDK",
        "vendor"     : "Venafi, Inc.",
        "description": "Application Integration for pyVenafi.",
        "scope"      : "certificate:approve,delete,discover,manage,read,revoke;ssh:approve,delete,discover,manage,read;codesign:delete,manage,read;configuration:delete,manage,read;restricted:delete,manage,read;security:delete,manage,read;statistics:read;agent:delete,read"
    }

.. note::
    Most features in this package require the *configuration:manage* scope to be included in the OAuth Application definition.
