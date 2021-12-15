Object Management
=================

.. note::
    See :ref:`authentication` for authentication details.

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


Reading Attributes
------------------

.. note::
    To read policy attributes for a particular class use :ref:`read_policy_attributes`.


.. rubric:: Reading A Single Value
.. code-block:: python

    from pytpp import Authenticate, Features, Attributes

    api = Authenticate(...)
    features = Features(api)

    certificate = features.certificate.get(certificate_dn=r'\VED\Policy\Certificates\my-cert.com')
    certiifcate_authority = features.objects.read(
        obj=certificate,
        attribute_name=Attributes.certificate.certificate_authority,
        include_policy_values=True  # If False, only the explicit attribute on this object is read.
    )

.. rubric:: Reading All Values
.. code-block:: python

    from pytpp import Authenticate, Features, Attributes

    api = Authenticate(...)
    features = Features(api)

    certificate = features.certificate.get(certificate_dn=r'\VED\Policy\Certificates\my-cert.com')
    attributes = features.objects.read_all(obj=certificate)
    certificate_authority = [attr.values[0] for attr in attributes if attr.name == Attributes.certificate.certificate_authority]

Writing Attributes
------------------

.. note::
    To write policy attributes for a particular class use :ref:`write_policy_attributes`.

.. rubric:: Write An Attribute Value



Waiting For Attribute Values
----------------------------

Renaming Objects
----------------

