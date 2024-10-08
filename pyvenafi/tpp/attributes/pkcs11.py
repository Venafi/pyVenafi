from __future__ import annotations

from pyvenafi.tpp.attributes._helper import (
    Attribute,
    IterableMeta,
)
from pyvenafi.tpp.attributes.application_base import ApplicationBaseAttributes

class PKCS11Attributes(ApplicationBaseAttributes, metaclass=IterableMeta):
    __config_class__ = "PKCS11"
    file_validation_disabled = Attribute('File Validation Disabled')
    hsm_cblob = Attribute('HSM:CBlob')
    hsm_cka_label_format = Attribute('HSM:CKA LABEL Format')
    hsm_csr_subject_dn = Attribute('HSM:CSR Subject DN')
    hsm_certificate_directory = Attribute('HSM:Certificate Directory')
    hsm_client_tool_path = Attribute('HSM:Client Tool Path')
    hsm_cryptoki_file = Attribute('HSM:Cryptoki File')
    hsm_embed_sans_in_csr = Attribute('HSM:Embed SANs in CSR')
    hsm_ic_cka_label_format = Attribute('HSM:IC CKA LABEL Format')
    hsm_import_certificate = Attribute('HSM:Import Certificate')
    hsm_issued_id = Attribute('HSM:Issued ID')
    hsm_issued_label = Attribute('HSM:Issued Label')
    hsm_issued_usecase = Attribute('HSM:Issued Usecase')
    hsm_kpblob = Attribute('HSM:KPBlob')
    hsm_last_issued_cblob = Attribute('HSM:Last Issued CBlob')
    hsm_last_issued_id = Attribute('HSM:Last Issued ID')
    hsm_last_issued_kpblob = Attribute('HSM:Last Issued KPBlob')
    hsm_last_issued_label = Attribute('HSM:Last Issued Label')
    hsm_last_issued_usecase = Attribute('HSM:Last Issued Usecase')
    hsm_openssl_config_file = Attribute('HSM:Openssl Config File')
    hsm_openssl_path = Attribute('HSM:Openssl Path')
    hsm_openssl_type = Attribute('HSM:Openssl Type')
    hsm_pkcs11attributes = Attribute('HSM:PKCS11Attributes')
    hsm_protection_type = Attribute('HSM:Protection Type')
    hsm_requested_cka_label = Attribute('HSM:Requested CKA LABEL')
    hsm_requested_ecdh = Attribute('HSM:Requested ECDH')
    hsm_requested_usecase = Attribute('HSM:Requested Usecase')
    hsm_reverse_subject_dn = Attribute('HSM:Reverse Subject DN')
    hsm_tmp_issued_cblob = Attribute('HSM:TMP Issued CBlob')
    hsm_tmp_issued_id = Attribute('HSM:TMP Issued ID')
    hsm_tmp_issued_kpblob = Attribute('HSM:TMP Issued KPBlob')
    hsm_token_label = Attribute('HSM:Token Label')
    hsm_token_password = Attribute('HSM:Token Password')
    hsm_utility_timeout = Attribute('HSM:Utility Timeout')
    network_validation_disabled = Attribute('Network Validation Disabled')
