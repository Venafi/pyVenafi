.. _attributes:

Attribute Names And Values
==========================

Every object in TPP has attributes that define the object's state and settings. To maximize the
capabilities of this module, ``AttributeNames`` and ``AttributeValues`` can be imported from the
pytpp module. These classes define most of the  configurable attribute names and values for the
features defined in the module. For a list of all the attribute names and values, refer to the
source code.

Using AttributeNames and AttributeValues
""""""""""""""""""""""""""""""""""""""""

.. tip::
    Use ``AttributeValues`` when the attribute calls for a value from a subset of values, such as
    a Certificate object's *Management Type* attribute.

.. tip::
    Attributes requiring a boolean type argument should be given a "0" or "1" as a string value,
    such as a Certificate Authority object's *SAN Enabled* attribute.

.. code-block:: python

    from pytpp import Authenticate, Features, AttributeNames, AttributeValues

    api = Authenticate(...)
    features = Features(api)

    credential = features.objects.get(object_dn=r'\VED\Policy\Administration\Credentials\SpecialBox')
    ca_folder = features.objects.get(object_dn=r'\VED\Policy\Administration\Certificate Authorities')
    cert_folder = features.objects.get(object_dn=r'\VED\Policy\Certificates')

    special_ca = features.certificate_authority.msca.create(
        name='Special CA',
        parent_folder_dn=ca_folder.dn,
        hostname='special.ca.mycompany.com',
        credential_dn=credential.dn,
        service_name='Special CA Service',
        template='WebServer',
        attributes={
            AttributeNames.CertificateAuthority.MSCA.include_cn_as_san: "1",
            AttributeNames.CertificateAuthority.san_enabled: "1"
        }
    )
    my_cert = features.certificate.create(
        name='special.site.mycompany.com',
        parent_folder_dn=cert_folder.dn,
        attributes={
            AttributeNames.Certificate.management_type: AttributeValues.Certificate.ManagementType.enrollment,
            AttributeNames.Certificate.x509_subject: 'special.site.mycompany.com',
            AttributeNames.Certificate.certificate_authority: special_ca.dn
        }
    )

Reading And Writing Attributes
""""""""""""""""""""""""""""""

Attributes can be read and written using :ref:`objects`. Reading an attributes always returns a list of values.
While it is convenient to be able to write to an object's attribute directly, there are feature functions
available to facilitate writing to objects.

.. code-block:: python

    from pytpp import Authenticate, Features, AttributeNames, AttributeValues

    api = Authenticate(...)
    features = Features(api)

    my_cert = features.objects.get(object_dn=r'\VED\Policy\Certificates\special.site.mycompany.com')
    approvers = features.identity.group.get_members(group_prefixed_name='local:HeadHonchos', resolve_nested=True)

    consumers = features.objects.read(object_dn=my_cert.dn, attribute_name=AttributeNames.Certificate.consumers)
    for consumer in consumers:
        application = features.objects.get(object_dn=consumer)
        features.objects.write(
            object_dn=application.dn,
            attributes={
                AttributeNames.Application.approver: [
                    {'ID': {'PrefixedUniversal': approver.prefixed_universal}}
                    for approver in approvers
                ]
            }
        )

Setting Policy Attributes
"""""""""""""""""""""""""

Policies are established on folder objects in TPP and enforced for specific attributes on object class types.
Having a list of all classes is convenient when managing policies and searching for objects. Search the code
for a list of all classes as they are not documented here.

See :ref:`folders` for an API reference to policy management.

In this example the Management Type and Certificate Authority attributes are being locked on the *Certificates*
folder.

.. code-block:: python

    from pytpp import Authenticate, Features, Classes, AttributeNames, AttributeValues

    api = Authenticate(...)
    features = Features(api)

    certificates_folder = features.objects.get(object_dn=r'\VED\Policy\Certificates')
    certificate_authority = features.objects.get(
        object_dn=r'\VED\Policy\Administration\Certificate Authorities\Special CA - WebServer'
    )
    features.folder.write_policy(
        folder_dn=certificates_folder.dn,
        class_name=Classes.Certificate.x509_certificate,
        locked=True,
        attributes={
            AttributeNames.Certificate.management_type: AttributeValues.Certificate.ManagementType.enrollment,
            AttributeNames.Certificate.certificate_authority: certificate_authority.dn
        }
    )
