import json
from apilibs.base import API, response_property
from apilibs.session import WEBSDK_URL
from enums.certificate import CertificateAttributes, CertificateStatus, OptionalFields
from enums.resultcodes import ResultCodes
from objects.response_objects.certificate import Certificate


class _Certificates(API):
    def __init__(self, session, api_type):
        super().__init__(
            session=session,
            api_type=api_type,
            url=WEBSDK_URL + '/Certificates',
            valid_return_codes=[200]
        )
        self.Associate = self._Associate(session, api_type)
        self.CheckPolicy = self._CheckPolicy(session, api_type)

    @property
    @response_property()
    def links(self):
        lnks = self.response.json()['_links']
        lnks = [Certificate.Link(lnk, self._api_type) for lnk in lnks]
        self.logger.log('_links object created.')
        return lnks

    @property
    @response_property()
    def x_record_count(self):
        xrc = self.response.headers.get('X-Record-Count')
        self.logger.log('Certificates X-Record-Count: %s' % xrc)
        return xrc

    @property
    @response_property()
    def certificates(self):
        certs = self.response.json()['Certificates']
        certs = [Certificate.Certificate(cert, self._api_type) for cert in certs]
        self.logger.log('Certificate objects created.')
        return certs

    @property
    @response_property()
    def data_range(self):
        dr = self.response.json()['DataRange']
        self.logger.log('Certificates DataRange: %s' % dr)
        return dr

    @property
    @response_property()
    def total_count(self):
        tc = self.response.json()['TotalCount']
        self.logger.log('Certificates TotalCount: %s' % tc)
        return tc

    def get(self, limit: int = None, offset: int = None, optional_fields: list = None, filters: dict = None):
        if optional_fields:
            if not isinstance(optional_fields, list):
                optional_fields = [optional_fields]

            if not set(optional_fields).issubset(set(OptionalFields.__dict__.values())):
                raise AssertionError('Invalid option fields. Expected one of {e}, but got {a}. Try importing "enums/certificate.py::OptionalFields".'.format(
                    e=OptionalFields.__dict__.keys(),
                    a=optional_fields
                ))
            optional_fields = ",".join(optional_fields)

        if filters:
            if not (isinstance(filters, dict) and set(filters.keys()).issubset(set(CertificateStatus.__dict__.values()) | set(CertificateAttributes.__dict__.values()))):
                raise TypeError('Filters must be of type dict with keys that map to one or more combinations of certificate attribute filters or '
                                'certificate status filters. Try importing "CertificateStatus" and "CertificateAttributes" from "enums/certificate.py".')

        params = {
            'Limit': limit,
            'Offset': offset,
            'OptionalFields': optional_fields
        }

        params.update(filters)

        self.response = self._session.get(url=self._url, params=params)

        return self

    class _Associate(API):
        def __init__(self, session, api_type):
            super().__init__(
                session=session,
                api_type=api_type,
                url=WEBSDK_URL + '/Certificates/Associate',
                valid_return_codes=[200]
            )

        @property
        @response_property()
        def success(self):
            result = self.response.json()['Success']
            if result is False:
                raise ValueError('Associating certificate failed.')
            return result

        def post(self, application_dn: str, certificate_dn: str, push_to_new: bool):
            body = json.dumps({
                'CertiicateDN': certificate_dn,
                'ApplicationDN': application_dn,
                'PushToNew': push_to_new
            })

            self.response = self._session.post(url=self._url, data=body)
            return self

    class _CheckPolicy(API):
        def __init__(self, session, api_type):
            super().__init__(
                session=session,
                api_type=api_type,
                url=WEBSDK_URL + '/Certificates/CheckPolicy',
                valid_return_codes=[200]
            )

        @property
        @response_property()
        def csr(self):
            c = Certificate.CSR(self.response.json()['CSR'], self._api_type)
            self.logger.log('CSR object created successfully.')
            return c

        @property
        @response_property()
        def policy(self):
            p = Certificate.Policy(self.response.json()['Policy'], self._api_type)
            self.logger.log('Certificate Policy object created successfully.')
            return p

        def post(self, policy_dn: str, pkcs10: str = None):
            body = json.dumps({
                'PolicyDN': policy_dn,
                'PKSC10': pkcs10
            })

            self.response = self._session.post(url=self._url, data=body)

            return self

    class _Dissociate(API):
        def __init__(self, session, api_type):
            super().__init__(
                session=session,
                api_type=api_type,
                url=WEBSDK_URL + '/Certificates/Dissociate',
                valid_return_codes=[200]
            )

        @property
        @response_property()
        def success(self):
            result = self.response.json()['Success']
            if result is False:
                raise ValueError('Dissociating certificate failed.')
            return result

        def post(self, certificate_dn: str, application_dn: list, delete_orphans: bool = False):
            body = json.dumps({
                'CertificateDN': certificate_dn,
                'ApplicationDN': application_dn,
                'DeleteOrphans': delete_orphans
            })

            self.response = self._session.post(url=self._url, data=body)
            return self
