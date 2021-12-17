Object Management
=================

.. note::
    See :ref:`authentication` for authentication details.

.. note::
    In all of the examples having ``obj`` parameters a DN may be substituted by a ``Config.Object`` and
    vice versa.

Getting And Validating Config Objects
-------------------------------------

.. rubric:: Getting Config Objects By DN Or GUID
.. code-block:: python

    from pytpp import Authenticate, Features

    api = Authenticate(...)
    features = Features(api)

    certificate = features.objects.get(object_dn=r'\VED\Policy\Certificates\my-cert.com')
    print(certificate.dn)

    same_certificate = features.objects.get(object_guid=certificate.guid)
    print(certificate.guid == same_certificate.guid)  # prints "True"

.. rubric:: Handling Objects That May Not Exist
.. code-block:: python

    from pytpp import Authenticate, Features
    from pytpp.features.definitions.exceptions import ObjectDoesNotExist

    api = Authenticate(...)
    features = Features(api)

    certificate_dn = r'\VED\Policy\Certificates\my-cert.com'

    # Using get() and try/except
    try:
        certificate = features.objects.get(object_dn=certificate_dn)
    except ObjectDoesNotExist:
        print(f'Cannot find {certificate_dn}.')

    # Using get() and suppressing the exception
    certificate = features.objects.get(
        object_dn=certificate_dn,
        raise_error_if_not_exists=False  # The default is True
    )
    if not certifiate.dn:
        print(f'Cannot find {certificate_dn}.')

    # Using exists() to validate the existence of a DN.
    if not features.objects.exists(object_dn=certificate_dn):
        print(f'Cannot find {certificate_dn}.')

.. _read_attributes:

Reading Attributes
------------------

.. note::
    To read policy attributes for a particular class use :ref:`read_policy_attributes`.

.. rubric:: Reading A Single Value
.. code-block:: python

    from pytpp import Authenticate, Features, Attributes

    api = Authenticate(...)
    features = Features(api)

    certiifcate_authority = features.objects.read(
        obj=r'\VED\Policy\Certificates\my-cert.com',
        attribute_name=Attributes.certificate.certificate_authority,
        include_policy_values=True  # If False, only the explicit attribute on this object is read.
    )

.. rubric:: Reading All Values
.. code-block:: python

    from pytpp import Authenticate, Features, Attributes

    api = Authenticate(...)
    features = Features(api)

    attributes = features.objects.read_all(obj=r'\VED\Policy\Certificates\my-cert.com')
    certificate_authority = [attr.values[0] for attr in attributes if attr.name == Attributes.certificate.certificate_authority]

Writing Attributes
------------------

.. note::
    To write policy attributes for a particular class use :ref:`write_policy_attributes`.

.. warning::
    Writing attributes will override the existing value(s) for that particular attribute. To append to a list of
    attributes that may already exist, first read those values and then append the new values.

.. rubric:: Write An Attribute Value
.. code-block:: python

    from pytpp import Authenticate, Features, Attributes

    api = Authenticate(...)
    features = Features(api)

    features.objects.write(
        obj=r'\VED\Policy\Certificates\my-cert.com',
        attributes={
            Attributes.certificate.consumers: [r'\VED\Policy\Installations\MyDevice\MyApplication'],
            Attributes.certificate.management_type: AttributeValues.Certificate.ManagementType.provisioning
        }
    )

Waiting For Attribute Values
----------------------------

Sometimes an operation is occurring that will create or update an attribute value on an object. For example, renewing a
certificate will cause the *Stage* and *Status* attributes to populate. This is useful when you are expecting a value
to be assigned to an attribute in some interval of time.

.. code-block:: python

    from pytpp import Authenticate, Features, Attributes

    api = Authenticate(...)
    features = Features(api)

    # Do some operation here.

    # Well, there is a certificate feature for this, but this is how it does it!
    features.objects.wait_for(
        obj=r'\VED\Policy\Certificates\my-cert.com',
        attribute_name=Attributes.certificate.stage,
        attribute_value='500'
    )

Renaming Objects
----------------

.. code-block:: python

    from pytpp import Authenticate, Features, Attributes

    api = Authenticate(...)
    features = Features(api)

    # This is used for renaming and/or moving objects.
    features.objects.rename(
        obj=r'\VED\Policy\Certificates\my-cert.com',
        new_object_dn=r'\VED\Policy\Certificates\SomeNewFolder\my-cert.com'
    )
