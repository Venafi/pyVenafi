import json
from apilibs.base import API, response_property
from apilibs.session import WEBSDK_URL
from enums.certificate import CertificateAttributes, CertificateStatus, OptionalFields
from enums.resultcodes import ResultCodes


class _Certificates(API):
    def __init__(self, session, api_type):
        super().__init__(
            session=session,
            api_type=api_type,
            url=WEBSDK_URL + '/Certificates',
            valid_return_codes=[200]
        )

    @property
    @response_property()
    def x_record_count(self):
        return

    @property
    @response_property()
    def certificates(self):
        return

    @property
    @response_property()
    def date_range(self):
        return

    @property
    @response_property()
    def total_count(self):
        return

    def get(self, limit=None, offset=None, optional_fields=None, filters=None):
        """
        :type limit: int
        :type offset: int
        :type optional_fields: list
        :type filters: dict
        """
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

        url_args = {
            'Limit': limit,
            'Offset': offset,
            'OptionalFields': optional_fields
        }

        url_args.update(filters)

        url = self._url + "?" + "&".join(["%s=%s" % (k, v) for k, v in url_args.items()])
        self.response = self._session.get(url=self._url, params=url_args)

        return self
