from datetime import datetime
from typing import List
from properties.response_objects.dataclasses import ssh
from pytpp.api.api_base import API, APIResponse, ResponseFactory, ResponseField


class _SSH:
    def __init__(self, api_obj):
        self.AddAuthorizedKey = self._AddAuthorizedKey(api_obj=api_obj)
        self.AddHostPrivateKey = self._AddHostPrivateKey(api_obj=api_obj)
        self.AddKnownHostKey = self._AddKnownHostKey(api_obj=api_obj)
        self.AddSelfServiceAuthorizedKey = self._AddSelfServiceAuthorizedKey(api_obj=api_obj)
        self.AddSelfServicePrivateKey = self._AddSelfServicePrivateKey(api_obj=api_obj)
        self.AddUserPrivateKey = self._AddUserPrivateKey(api_obj=api_obj)
        self.ApproveKeyOperation = self._ApproveKeyOperation(api_obj=api_obj)
        self.CancelKeyOperation = self._CancelKeyOperation(api_obj=api_obj)
        self.CancelRotation = self._CancelRotation(api_obj=api_obj)
        self.ChangePrivateKeyPassphrase = self._ChangePrivateKeyPassphrase(api_obj=api_obj)
        self.ConfirmSelfServiceKeyInstallation = self._ConfirmSelfServiceKeyInstallation(api_obj=api_obj)
        self.DeleteUnmatchedKeyset = self._DeleteUnmatchedKeyset(api_obj=api_obj)
        self.Devices = self._Devices(api_obj=api_obj)
        self.EditKeyOptions = self._EditKeyOptions(api_obj=api_obj)
        self.EditSelfServiceAuthorizedKey = self._EditSelfServiceAuthorizedKey(api_obj=api_obj)
        self.ExportSelfServiceAuthorizedKey = self._ExportSelfServiceAuthorizedKey(api_obj=api_obj)
        self.ExportSelfServicePrivateKey = self._ExportSelfServicePrivateKey(api_obj=api_obj)
        self.ImportAuthorizedKey = self._ImportAuthorizedKey(api_obj=api_obj)
        self.ImportKeyUsageData = self._ImportKeyUsageData(api_obj=api_obj)
        self.ImportPrivateKey = self._ImportPrivateKey(api_obj=api_obj)
        self.KeyDetails = self._KeyDetails(api_obj=api_obj)
        self.KeysetDetails = self._KeysetDetails(api_obj=api_obj)
        self.KeyUsage = self._KeyUsage(api_obj=api_obj)
        self.MoveKeysetsToPolicy = self._MoveKeysetsToPolicy(api_obj=api_obj)
        self.RejectKeyOperation = self._RejectKeyOperation(api_obj=api_obj)
        self.RemoveKey = self._RemoveKey(api_obj=api_obj)
        self.RetryKeyOperation = self._RetryKeyOperation(api_obj=api_obj)
        self.RetryRotation = self._RetryRotation(api_obj=api_obj)
        self.Rotate = self._Rotate(api_obj=api_obj)
        self.SetUnmatchedKeysetPassPhrase = self._SetUnmatchedKeysetPassPhrase(api_obj=api_obj)
        self.SkipKeyRotation = self._SkipKeyRotation(api_obj=api_obj)
        self.TestDeviceConnection = self._TestDeviceConnection(api_obj=api_obj)
        self.Widget = self._Widget(api_obj=api_obj)

    class _AddAuthorizedKey(API):
        def __init__(self, api_obj):
            super().__init__(api_obj=api_obj, url='/SSH/AddAuthorizedKey')

        # noinspection ALL
        def post(self, device_guid: str, filepath: str, keyset_id: str, username: str, allowed_source_restriction: list = None,
                 denied_source_restriction: list = None, forced_command: str = None, format: str = None, options: list = None):
            body = {
                'AllowedSourceRestriction': allowed_source_restriction,
                'DeniedSourceRestriction': denied_source_restriction,
                'DeviceGuid': device_guid,
                'Filepath': filepath,
                'ForcedCommand': forced_command,
                'Format': format,
                'KeysetId': keyset_id,
                'Options': options,
                'Username': username
            }

            class Response(APIResponse):
                key_id: int = ResponseField(alias='KeyId')
                response: ssh.Response = ResponseField(alias='Response')

            return ResponseFactory(response_cls=Response, response=self._post(data=body))

    class _AddHostPrivateKey(API):
        def __init__(self, api_obj):
            super().__init__(api_obj=api_obj, url='/SSH/AddHostPrivateKey')

        # noinspection ALL
        def post(self, device_guid: str, filepath: str, username: str, format: str = None, policy_dn: str = None):
            body = {
                'DeviceGuid': device_guid,
                'Filepath': filepath,
                'Format': format,
                'Username': username,
                'PolicyDN': policy_dn
            }

            class Response(APIResponse):
                key_id: int = ResponseField(alias='KeyId')
                keyset_id: str = ResponseField(alias='KeysetId')
                response: ssh.Response = ResponseField(alias='Response')

            return ResponseFactory(response_cls=Response, response=self._post(data=body))

    class _AddKnownHostKey(API):
        def __init__(self, api_obj):
            super().__init__(api_obj=api_obj, url='/SSH/AddKnownHostKey')

        # noinspection ALL
        def post(self, device_guid: str, filepath: str, keyset_id: str, username: str, format: str = None):
            body = {
                'DeviceGuid': device_guid,
                'Filepath': filepath,
                'Format': format,
                'KeysetId': keyset_id,
                'Username': username
            }

            class Response(APIResponse):
                key_id: int = ResponseField(alias='KeyId')
                response: ssh.Response = ResponseField(alias='Response')

            return ResponseFactory(response_cls=Response, response=self._post(data=body))

    class _AddSelfServiceAuthorizedKey(API):
        def __init__(self, api_obj):
            super().__init__(api_obj=api_obj, url='/SSH/AddSelfServiceAuthorizedKey')

        def post(self, allowed_source_restriction: list, denied_source_restriction: list, folder_id: str, location: str, notes: str,
                 options: list, owner: str, contact_email: str = None, forced_command: str = None, keyset_id: str = None):
            body = {
                'AllowedSourceRestriction': allowed_source_restriction,
                'ContactEmail': contact_email,
                'DeniedSourceRestriction': denied_source_restriction,
                'FolderId': folder_id,
                'ForcedCommand': forced_command,
                'KeysetId': keyset_id,
                'Location': location,
                'Notes': notes,
                'Options': options,
                'Owner': owner
            }

            class Response(APIResponse):
                key_id: int = ResponseField(alias='KeyId')
                keyset_id: str = ResponseField(alias='KeysetId')
                notes: str = ResponseField(alias='Notes')
                response: ssh.Response = ResponseField(alias='Response')

            return ResponseFactory(response_cls=Response, response=self._post(data=body))

    class _AddSelfServicePrivateKey(API):
        def __init__(self, api_obj):
            super().__init__(api_obj=api_obj, url='/SSH/AddSelfServicePrivateKey')

        def post(self, folder_id: str, location: str, notes: str, owner: str, contact_email: str = None, keyset_id: str = None):
            body = {
                'ContactEmail': contact_email,
                'FolderId': folder_id,
                'KeysetId': keyset_id,
                'Location': location,
                'Notes': notes,
                'Owner': owner
            }

            class Response(APIResponse):
                owner: str = ResponseField(alias='Owner')
                location: str = ResponseField(alias='Location')
                response: ssh.Response = ResponseField(alias='Response')

            return ResponseFactory(response_cls=Response, response=self._post(data=body))

    class _AddUserPrivateKey(API):
        def __init__(self, api_obj):
            super().__init__(api_obj=api_obj, url='/SSH/AddUserPrivateKey')

        # noinspection ALL
        def post(self, device_guid: str, filepath: str, username: str, format: str = None, keyset_id: str = None,
                 passphrase: str = None, policy_dn: str = None):
            body = {
                'DeviceGuid': device_guid,
                'Filepath': filepath,
                'Format': format,
                'KeysetId': keyset_id,
                'Passphrase': passphrase,
                'Username': username,
                'PolicyDN': policy_dn
            }

            class Response(APIResponse):
                key_id: int = ResponseField(alias='KeyId')
                keyset_id: str = ResponseField(alias='KeysetId')
                response: ssh.Response = ResponseField(alias='Response')

            return ResponseFactory(response_cls=Response, response=self._post(data=body))

    class _ApproveKeyOperation(API):
        def __init__(self, api_obj):
            super().__init__(api_obj=api_obj, url='/SSH/ApproveKeyOperation')

        def post(self, key_id: int, comment: str):
            body = {
                'KeyId': key_id,
                'Comment': comment
            }

            class Response(APIResponse):
                response: ssh.Response = ResponseField(alias='Response')

            return ResponseFactory(response_cls=Response, response=self._post(data=body))

    class _CancelKeyOperation(API):
        def __init__(self, api_obj):
            super().__init__(api_obj=api_obj, url='/SSH/CancelKeyOperation')

        def post(self, key_id: int):
            body = {
                'KeyId': key_id
            }

            class Response(APIResponse):
                response: ssh.Response = ResponseField(alias='Response')

            return ResponseFactory(response_cls=Response, response=self._post(data=body))

    class _CancelRotation(API):
        def __init__(self, api_obj):
            super().__init__(api_obj=api_obj, url='/SSH/CancelRotation')

        def post(self, keyset_id: str):
            body = {
                'KeysetId': keyset_id
            }

            class Response(APIResponse):
                response: ssh.Response = ResponseField(alias='Response')

            return ResponseFactory(response_cls=Response, response=self._post(data=body))

    class _ChangePrivateKeyPassphrase(API):
        def __init__(self, api_obj):
            super().__init__(api_obj=api_obj, url='/SSH/ChangePrivateKeyPassphrase')

        def post(self, key_id: int, passphrase: str):
            body = {
                'KeysetId': key_id,
                'Passphrase': passphrase
            }

            class Response(APIResponse):
                response: ssh.Response = ResponseField(alias='Response')

            return ResponseFactory(response_cls=Response, response=self._post(data=body))

    class _ConfirmSelfServiceKeyInstallation(API):
        def __init__(self, api_obj):
            super().__init__(api_obj=api_obj, url='/SSH/ConfirmSelfServiceKeyInstallation')

        def post(self, keyset_id: str):
            body = {
                'KeysetId': keyset_id
            }

            class Response(APIResponse):
                response: ssh.Response = ResponseField(alias='Response')

            return ResponseFactory(response_cls=Response, response=self._post(data=body))

    class _DeleteUnmatchedKeyset(API):
        def __init__(self, api_obj):
            super().__init__(api_obj=api_obj, url='/SSH/DeleteUnmatchedKeyset')

        def post(self, unmatched_trust_id: str):
            body = {
                'UnmatchedTrustId': unmatched_trust_id
            }

            class Response(APIResponse):
                response: ssh.Response = ResponseField(alias='Response')

            return ResponseFactory(response_cls=Response, response=self._post(data=body))

    class _Devices(API):
        def __init__(self, api_obj):
            super().__init__(api_obj=api_obj, url='/SSH/Devices')

        def post(self, page_size: int, offset: int = None, ssh_device_filter: dict = None):
            body = {
                'PageSize': page_size,
                'Offset': offset,
                'SshDeviceFilter': ssh_device_filter
            }

            class Response(APIResponse):
                data: List[ssh.DeviceData] = ResponseField(default_factory=list, alias='Data')

            return ResponseFactory(response_cls=Response, response=self._post(data=body))

    class _EditKeyOptions(API):
        def __init__(self, api_obj):
            super().__init__(api_obj=api_obj, url='/SSH/EditKeyOptions')

        def post(self, key_id: int, allowed_source_restriction: list = None, denied_source_restriction: list = None,
                 forced_command: str = None, options: list = None):
            body = {
                'AllowedSourceRestriction': allowed_source_restriction,
                'DeniedSourceRestriction' : denied_source_restriction,
                'ForcedCommand'           : forced_command,
                'KeyId'                   : key_id,
                'Options'                 : options
            }

            class Response(APIResponse):
                response: ssh.Response = ResponseField(alias='Response')

            return ResponseFactory(response_cls=Response, response=self._post(data=body))

    class _EditSelfServiceAuthorizedKey(API):
        def __init__(self, api_obj):
            super().__init__(api_obj=api_obj, url='/SSH/EditSelfServiceAuthorizedKey')

        def post(self, key_id: int, allowed_source_restriction: list = None,
                 denied_source_restriction: list = None, forced_command: str = None,
                 location: str = None, notes: str = None, options: list = None):
            body = {
                'AllowedSourceRestriction': allowed_source_restriction,
                'DeniedSourceRestriction' : denied_source_restriction,
                'ForcedCommand'           : forced_command,
                'KeyId'                   : key_id,
                'Location'                : location,
                'Notes'                   : notes,
                'Options'                 : options
            }

            class Response(APIResponse):
                response: ssh.Response = ResponseField(alias='Response')

            return ResponseFactory(response_cls=Response, response=self._post(data=body))

    class _ExportSelfServiceAuthorizedKey(API):
        def __init__(self, api_obj):
            super().__init__(api_obj=api_obj, url='/SSH/ExportSelfServiceAuthorizedKey')

        # noinspection ALL
        def post(self, key_id: int, format: str = None):
            body = {
                'KeyId': key_id,
                'Format': format
            }

            class Response(APIResponse):
                key_material: str = ResponseField(alias='KeyMaterial')
                response: ssh.Response = ResponseField(alias='Response')

            return ResponseFactory(response_cls=Response, response=self._post(data=body))

    class _ExportSelfServicePrivateKey(API):
        def __init__(self, api_obj):
            super().__init__(api_obj=api_obj, url='/SSH/ExportSelfServicePrivateKey')

        # noinspection ALL
        def post(self, key_id: int, format: str = None, passphrase: str = None):
            body = {
                'KeyId': key_id,
                'Format': format,
                'Passphrase': passphrase
            }

            class Response(APIResponse):
                key_id: int = ResponseField(alias='KeyId')
                keyset_id: str = ResponseField(alias='KeysetId')
                notes: str = ResponseField(alias='Notes')
                response: ssh.Response = ResponseField(alias='Response')

            return ResponseFactory(response_cls=Response, response=self._post(data=body))

    class _ImportAuthorizedKey(API):
        def __init__(self, api_obj):
            super().__init__(api_obj=api_obj, url='/SSH/ImportAuthorizedKey')

        # noinspection ALL
        def post(self, device_guid: str, filepath: str, format: str, key_content_base_64: str, username: str):
            body = {
                'DeviceGuid': device_guid,
                'Filepath': filepath,
                'Format': format,
                'KeyContentBase64': key_content_base_64,
                'Username': username
            }

            class Response(APIResponse):
                key_id: int = ResponseField(alias='KeyId')
                response: ssh.Response = ResponseField(alias='SshWebResponse')

            return ResponseFactory(response_cls=Response, response=self._post(data=body))

    class _ImportKeyUsageData(API):
        def __init__(self, api_obj):
            super().__init__(api_obj=api_obj, url='/SSH/ImportKeyUsageData')

        def post(self, log_data: list):
            body = {
                'LogData': log_data
            }

            class Response(APIResponse):
                response: ssh.Response = ResponseField(alias='SshWebResponse')

            return ResponseFactory(response_cls=Response, response=self._post(data=body))

    class _ImportPrivateKey(API):
        def __init__(self, api_obj):
            super().__init__(api_obj=api_obj, url='/SSH/ImportPrivateKey')

        # noinspection ALL
        def post(self, device_guid: str, filepath: str, format: str, key_content_base_64: str, username: str,
                 passphrase: str = None):
            body = {
                'DeviceGuid': device_guid,
                'Filepath': filepath,
                'Format': format,
                'KeyContentBase64': key_content_base_64,
                'Passphrase': passphrase,
                'Username': username
            }

            class Response(APIResponse):
                key_id: int = ResponseField(alias='KeyId')
                response: ssh.Response = ResponseField(alias='SshWebResponse')

            return ResponseFactory(response_cls=Response, response=self._post(data=body))

    class _KeyDetails(API):
        def __init__(self, api_obj):
            super().__init__(api_obj=api_obj, url='/SSH/KeyDetails')

        def post(self, key_id: int):
            body = {
                'KeyId': key_id
            }

            class Response(APIResponse):
                key_data: List[ssh.KeyData] = ResponseField(default_factory=list)

            return ResponseFactory(response_cls=Response, response=self._post(data=body), root_field='key_data')

    class _KeysetDetails(API):
        def __init__(self, api_obj):
            super().__init__(api_obj=api_obj, url='/SSH/KeysetDetails')

        def get(self, keyset_id: str, load_key_data: bool = None):
            params = {
                'KeysetId': keyset_id,
                'LoadKeyData': load_key_data
            }

            class Response(APIResponse):
                access: str = ResponseField(alias='Access')
                algorithm: str = ResponseField(alias='Algorithm')
                fingerprint_md5: str = ResponseField(alias='FingerprintMD5')
                fingerprint_sha256: str = ResponseField(alias='FingerprintSHA256')
                keyset_id: str = ResponseField(alias='KeysetId')
                last_rotation_date: datetime = ResponseField(alias='LastRotationDate')
                last_used: datetime = ResponseField(alias='LastUsed')
                length: int = ResponseField(alias='Length')
                private_keys: List[ssh.KeyData] = ResponseField(default_factory=list, alias='PrivateKeys')
                process_status: int = ResponseField(alias='ProcessStatus')
                public_keys: List[ssh.KeyData] = ResponseField(default_factory=list, alias='PublicKeys')
                rotation_stage: int = ResponseField(alias='RotationStage')
                type: str = ResponseField(alias='Type')
                violation_status: List[int] = ResponseField(alias='ViolationStatus')

            return ResponseFactory(response_cls=Response, response=self._get(params=params))

        def post(self, page_size: int, keyset_filter: list = None, load_key_data: bool = None, offset: int = None):
            body = {
                'KeysetFilter': keyset_filter,
                'LoadKeyData': load_key_data,
                'Offset': offset,
                'PageSize': page_size
            }

            class Response(APIResponse):
                data: List[ssh.KeySetData] = ResponseField(default_factory=list, alias='Data')

            return ResponseFactory(response_cls=Response, response=self._post(data=body))

    class _KeyUsage(API):
        def __init__(self, api_obj):
            super().__init__(api_obj=api_obj, url='/SSH/KeyUsage')

        def post(self, ssh_key_usage_filter: list, page_size: int = None, offset: int = None):
            body = {
                'SshKeyUsageFilter': ssh_key_usage_filter,
                'PageSize': page_size,
                'Offset': offset
            }

            class Response(APIResponse):
                data: List[ssh.KeyUsageData] = ResponseField(default_factory=list, alias='Data')

            return ResponseFactory(response_cls=Response, response=self._post(data=body))

    class _MoveKeysetsToPolicy(API):
        def __init__(self, api_obj):
            super().__init__(api_obj=api_obj, url='/SSH/MoveKeysetsToPolicy')

        def post(self, keyset_ids: list, policy_dn: str = None, policy_path: str = None):
            body = {
                'KeysetIds': keyset_ids,
                'PolicyDN': policy_dn,
                'PolicyPath': policy_path
            }

            class Response(APIResponse):
                response: ssh.Response = ResponseField(alias='Response')

            return ResponseFactory(response_cls=Response, response=self._post(data=body))

    class _RejectKeyOperation(API):
        def __init__(self, api_obj):
            super().__init__(api_obj=api_obj, url='/SSH/RejectKeyOperation')

        def post(self, key_id: int, comment: str):
            body = {
                'KeyId': key_id,
                'Comment': comment
            }

            class Response(APIResponse):
                response: ssh.Response = ResponseField(alias='Response')

            return ResponseFactory(response_cls=Response, response=self._post(data=body))

    class _RemoveKey(API):
        def __init__(self, api_obj):
            super().__init__(api_obj=api_obj, url='/SSH/RemoveKey')

        def post(self, key_id: int):
            body = {
                'KeyId': key_id
            }

            class Response(APIResponse):
                response: ssh.Response = ResponseField(alias='Response')

            return ResponseFactory(response_cls=Response, response=self._post(data=body))

    class _RetryKeyOperation(API):
        def __init__(self, api_obj):
            super().__init__(api_obj=api_obj, url='/SSH/RetryKeyOperation')

        def post(self, key_id: int):
            body = {
                'KeyId': key_id
            }

            class Response(APIResponse):
                response: ssh.Response = ResponseField(alias='Response')

            return ResponseFactory(response_cls=Response, response=self._post(data=body))

    class _RetryRotation(API):
        def __init__(self, api_obj):
            super().__init__(api_obj=api_obj, url='/SSH/RetryRotation')

        def post(self, keyset_id: str):
            body = {
                'KeysetId': keyset_id
            }

            class Response(APIResponse):
                response: ssh.Response = ResponseField(alias='Response')

            return ResponseFactory(response_cls=Response, response=self._post(data=body))

    class _Rotate(API):
        def __init__(self, api_obj):
            super().__init__(api_obj=api_obj, url='/SSH/Rotate')

        def post(self, keyset_id: str, options: int = None, allow_skip_on_rotation: bool = None):
            body = {
                'KeysetId': keyset_id,
                'AllowSkipOnRotation': allow_skip_on_rotation,
                'Options': options
            }

            class Response(APIResponse):
                response: ssh.Response = ResponseField(alias='Response')

            return ResponseFactory(response_cls=Response, response=self._post(data=body))

    class _SetUnmatchedKeysetPassPhrase(API):
        def __init__(self, api_obj):
            super().__init__(api_obj=api_obj, url='/SSH/SetUnmatchedKeysetPassPhrase')

        def post(self, passphrase: str, unmatched_trust_id: str):
            body = {
                'Passphrase': passphrase,
                'UnmatchedTrustId': unmatched_trust_id
            }

            class Response(APIResponse):
                response: ssh.Response = ResponseField(alias='Response')

            return ResponseFactory(response_cls=Response, response=self._post(data=body))

    class _SkipKeyRotation(API):
        def __init__(self, api_obj):
            super().__init__(api_obj=api_obj, url='/SSH/SkipKeyRotation')

        def post(self, key_id: int):
            body = {
                'KeyId': key_id
            }

            class Response(APIResponse):
                response: ssh.Response = ResponseField(alias='Response')

            return ResponseFactory(response_cls=Response, response=self._post(data=body))

    class _TestDeviceConnection(API):
        def __init__(self, api_obj):
            super().__init__(api_obj=api_obj, url='SSH/TestDeviceConnection')

        def post(self, device_guids: List[str]):
            body = {
                'deviceGuids': device_guids
            }

            class Response(APIResponse):
                connection_results: List[ssh.ConnectionResult] = ResponseField(default_factory=list)

            return ResponseFactory(response_cls=Response, response=self._post(data=body), root_field='connection_results')

    class _Widget:
        def __init__(self, api_obj):
            self.CriticalAlerts = self._CriticalAlerts(api_obj=api_obj)
            self.PolicyViolations = self._PolicyViolations(api_obj=api_obj)
            self.Stats = self._Stats(api_obj=api_obj)

        class _CriticalAlerts(API):
            def __init__(self, api_obj):
                super().__init__(api_obj=api_obj, url='/SSH/Widget/CriticalAlerts')

            def get(self, min_allowed_key_length: int):
                params = {
                    'minAllowedKeyLength': min_allowed_key_length
                }

                class Response(APIResponse):
                    root_orphans: int = ResponseField(alias='RootOrphans')
                    non_root_orphans: int = ResponseField(alias='NonRootOrphans')
                    accessible_root_accounts: int = ResponseField(alias='AccessibleRootAccounts')
                    shared_private_keys: int = ResponseField(alias='SharedPrivateKeys')
                    non_compliant_duplicate_private_keys: int = ResponseField(alias='NonCompliantDuplicatePrivateKeys')
                    very_small_key: int = ResponseField(alias='VerySmallKey')

                return ResponseFactory(response_cls=Response, response=self._get(params=params))

        class _PolicyViolations(API):
            def __init__(self, api_obj):
                super().__init__(api_obj=api_obj, url='/SSH/Widget/PolicyViolations')

            def get(self):
                class Response(APIResponse):
                    non_compliant_force_command: str = ResponseField(alias='NonCompliantForceCommand')
                    non_compliant_source_restriction: str = ResponseField(alias='NonCompliantSourceRestriction')
                    missing_options: List[str] = ResponseField(alias='MissingOptions')
                    non_compliant_algorithm: str = ResponseField(alias='NonCompliantAlgorithm')
                    vulnerable_protocol: str = ResponseField(alias='VulnerableProtocol')
                    non_compliant_vendor_format: str = ResponseField(alias='NonCompliantVendorFormat')
                    key_older_than_policy: str = ResponseField(alias='KeyOlderThanPolicy')
                    shared_server_account: str = ResponseField(alias='SharedServerAccount')
                    key_smaller_than_policy: str = ResponseField(alias='KeySmallerThanPolicy')
                    duplicate_private_keys: List[str] = ResponseField(alias='DuplicatePrivateKeys')
                    root_access: str = ResponseField(alias='RootAccess')

                return ResponseFactory(response_cls=Response, response=self._get())

        class _Stats(API):
            def __init__(self, api_obj):
                super().__init__(api_obj=api_obj, url='/SSH/Widget/Stats')

            def get(self, group_by: str):
                params = {
                    'GroupBy': group_by
                }

                class Response(APIResponse):
                    name_value_pairs: dict = ResponseField()

                return ResponseFactory(response_cls=Response, response=self._get(params=params), root_field='name_value_pairs')
