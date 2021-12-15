Object Management
=================

.. note::
    See :ref:`authentication` for authentication details.

Get Any Config Object By DN
---------------------------

.. code-block:: python

    from pytpp import Authenticate, Features

    api = Authenticate(...)
    features = Features(api)

    certificate = features.objects.get(object_dn=r'\VED\Policy\Certificate\my-cert.com')
    print(certificate.dn)

    same_certificate = features.objects.get(object_guid=certificate.guid)
    print(certificate.guid == same_certificate.guid)  # prints "True"



Reading Attributes
------------------

Writing Attributes
------------------

.. note::
    To write policyable attributes, use :ref:`write_policy_attributes`. ``Objects`` does not write policyable attributes.

Renaming Objects
----------------

