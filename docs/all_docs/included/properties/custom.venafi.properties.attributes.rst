Attribute Classes
=================

.. toctree::

   venafi.properties.certificate
   venafi.properties.config
   venafi.properties.config_schema
   venafi.properties.metadata
   venafi.properties.permissions
   venafi.properties.resultcodes
   venafi.properties.secret_store
   venafi.properties.ssh

Attribute classes are classes having properties that map to strings recognized by TPP. For example,
in order to set a `description` on a folder, the WebSDK API request body should look like this:

.. code-block:: json

    {
        "ObjectDN": "\\VED\\Policy\\SomeNewFolder",
        "Class": "Policy",
        "NameAttributeList": {
            "Name": "Description",
            "Value": "My fancy description."
        }
    }

The equivalent code using this framework should look like this:

.. code-block:: python

    from venafi.api import Authenticate
    from venafi.features import Features, Attributes

    api = Authenticate(...)  # ... represents the required parameters
    features = Features(api)

    # Create the attributes
    folder_attributes = {
        Attributes.Folder.description: 'My fancy description.'
    }
    # Create the folder
    folder = features.folder.create(name='SomeNewFolder', container='\\VED\\Policy', attributes=folder_attributes)

