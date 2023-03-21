.. _codesign_template_usage:

Templates
=========

.. note::
    Refer to :ref:`authentication` for ways to authenticate to the TPP WebSDK.

Managing Templates
------------------

.. code-block:: python

    from pyvenafi.tpp import Authenticate, Features
    from pyvenafi.tpp.api.websdk.enums.config import CodeSign
    from pyvenafi.tpp.api.websdk.models.codesign import (
        InfoValue,
        Items,
    )

    api = Authenticate(...)
    features = Features(api)

    #### CREATE ####

    template = features.codesign.template.create(
        name='My Certificate Template',
        template_type=CodeSign.TemplateType.certificate_template,
    )

    #### UPDATE ####

    # Make changes to template object
    template.certificate_authority_dn = InfoValue(
        info=1,
        value=Items(
            items=[
                r'\VED\Policy\Code Signing\Certificate Authority Templates\My Microsoft CA'
            ]
        )
    )
    template.key_algorithm = InfoValue(
        info=1,
        value=Items(
            items=[
                'RSA1024',
                'RSA2048',
                'RSA3072',
                'RSA4096'
            ]
        )
    )
    template.target_policy_dn = r'\VED\Policy\Code Signing\Certificates'

    features.codesign.template.update(template=template)

    #### DELETE ####

    features.codesign.template.delete(template=template, force=True)

Getting & Enumerating Templates
-------------------------------

.. code-block:: python

    from pyvenafi.tpp import Authenticate, Features

    api = Authenticate(...)
    features = Features(api)

    #### GET ####

    template = features.codesign.template.get(dn=r'\VED\Code Signing\Environment Templates\My Certificate Template')

    #### ENUMERATE ####

    templates = features.codesign.template.enumerate()

