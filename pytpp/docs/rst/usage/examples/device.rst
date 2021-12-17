.. _device:

Device
======

Creating a device
-----------------
Make sure you are authenticated, see: :ref:`authentication`

.. code-block:: python

    from pytpp import Attributes, Authenticate, Features

    api = Authenticate(...)
    features = Features(api)

    device = features.device.create(
        name='name_of_device',
        parent_folder_dn='\\VED\\Policy\\PLACEMENT_FOLDER',
        attributes={
            Attributes.device.host       : '192.168.1.128',
            Attributes.device.port       : '22',
            Attributes.device.credential : '\\VED\\Policy\\Administration\\Credentials\\root',
            Attributes.device.description: 'Some description about the object'
    })

.. note::
    1. The parent_folder_dn is a path to a folder in the Policy Tree to place the device in
    2. The device attributes listed here are for example only

Deleting a device
-----------------
.. code-block:: python

    from pytpp import Authenticate, Features

    api = Authenticate(...)
    features = Features(api)

    device = features.device.create(
        name='name_of_device',
        parent_folder='\\VED\\Policy\\PLACEMENT_FOLDER'
    )

    features.device.delete(device=device)

Get a device
------------
.. code-block:: python

    from pytpp import Authenticate, Features

    api = Authenticate(...)
    features = Features(api)

    # This will raise an error if it doesn't exist
    device = features.device.get(device_dn='\\VED\\Policy\\Devices\\test_device')

    # This will not raise an error if it doesn't exist
    device = features.device.get(device_dn='\\VED\\Policy\\Devices\\test_device', raise_error_if_not_exists=False)

Scan a device for ssh keys
--------------------------
.. code-block:: python

    from pytpp import Authenticate, Features

    api = Authenticate(...)
    features = Features(api)

    # You can submit with the device as an object
    device = features.device.create(device_dn='\\VED\\Policy\\Devices\\test_device')
    features.device.scan_for_ssh_keys(device=device)

    # You can also submit with the device as a DN
    features.device.scan_for_ssh_keys(device='\\VED\\Policy\\Devices\\test_device')

    # You can also submit with the GUID of the device
    features.device.scan_for_ssh_keys(device='{552363ad-08d3-42f9-83a1-f28422bcbced}')
.. note::
    1. The device must be in a group setup with ssh discovery work enabled
    2. The device must be in a folder where agentless disovery and remediation is enabled (if the group type is agentless)
