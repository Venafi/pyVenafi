from enums.config import ConfigClass, CertificateAuthorityAttributes
from features.bases.feature_base import FeatureBase, FeatureError, ApiPreferences, feature


class _CertificateAuthorityBase(FeatureBase):
    def __init__(self, auth):
        super().__init__(auth=auth)

    def delete(self, object_dn: str):
        self._config_delete(object_dn=object_dn)


@feature()
class MSCA(_CertificateAuthorityBase):
    def __init__(self, auth):
        super().__init__(auth=auth)

    def create(self, name: str, container: str, hostname: str, service_name: str, credential_dn: str, template: str, attributes: dict = None):
        attributes = attributes or {}
        attributes.update({
            CertificateAuthorityAttributes.MSCA.host: hostname,
            CertificateAuthorityAttributes.MSCA.given_name: service_name,
            CertificateAuthorityAttributes.MSCA.credential: credential_dn,
            CertificateAuthorityAttributes.MSCA.template: template
        })
        return self._config_create(
            name=name,
            container=container,
            config_class=ConfigClass.msca,
            attributes=attributes
        )


@feature()
class SelfSigned(_CertificateAuthorityBase):
    def __init__(self, auth):
        super().__init__(auth=auth)

    def create(self, name: str, container: str, attributes: dict = None):
        return self._config_create(
            name=name,
            container=container,
            config_class=ConfigClass.self_signed,
            attributes=attributes
        )
