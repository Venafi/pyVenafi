Custom Fields
=============

Creating Custom Fields
----------------------

There are many options when creating custom fields. Refer to the *POST Metadata/DefineItem* API in the |Doc Home Page|
to get more info on possible inputs.

.. code-block:: python

    from pytpp import Authenticate, Features, Attributes, AttributeValues

    api = Authenticate(...)
    features = Features(api)

    custom_field = features.custom_fields.create(
        label='MyCustomFieldLabel',
        name='MyCustomFieldName',
        classes=[Attributes.certificate.__config_class__],
        data_type=AttributeValues.CustomField.Type.text_string,
        allowed_values=[
            'Option 1',
            'Option 2'
        ],
        default_values=['Option 1'],
        error_message='You can only choose from these valid options: "Option 1", "Option 2".',
        help_text='Choose from "Option 1" or "Option 2".',
        mandatory=True,
        policyable=True,
        regular_expression='^[a-zA-Z0-9\s]*$',
        render_hidden=False,
        render_read_only=False,
        single=True
    )

Reading Custom Fields
---------------------

.. rubric:: Read Custom Field From An Object

.. code-block:: python

    from pytpp import Authenticate, Features

    api = Authenticate(...)
    features = Features(api)

    result = features.custom_fields.read(
        obj=r'\VED\Policy\Certificates\MyTeam\my-cert.com',
        custom_field='Team Name'
    )
    if not 'West Region Team' in result.values:
        print('This is not my team, hence not my certificate to manage.')

.. rubric:: Read Custom Field From A Policy

.. code-block:: python

    from pytpp import Authenticate, Features, Attributes

    api = Authenticate(...)
    features = Features(api)

    result = features.custom_fields.read_policy(
        folder=r'\VED\Policy\Certificates\MyTeam',
        custom_field='Team Name',
        class_name=Attributes.device.__config_class__
    )
    if not result.locked:
        # Change it to locked here.
        ...

Writing Custom Fields
---------------------

.. rubric:: Write Custom Field To An Object

.. code-block:: python

    from pytpp import Authenticate, Features

    api = Authenticate(...)
    features = Features(api)

    features.custom_fields.write(
        obj=r'\VED\Policy\Certificates\MyTeam\my-cert.com',
        custom_field='Team Name',
        values=['West Region Team']
    )


.. rubric:: Write Custom Field To A Policy

.. code-block:: python

    from pytpp import Authenticate, Features, Attributes

    api = Authenticate(...)
    features = Features(api)

    features.custom_fields.write_policy(
        folder=r'\VED\Policy\Certificates\MyTeam',
        custom_field='Team Name',
        class_name=Attributes.device.__config_class__,
        values=['West Region Team'],
        locked=True
    )
