import base64
from typing import List
from datetime import datetime
from venafi.properties.config import WorkflowClassNames, WorkflowAttributes, WorkflowAttributeValues
from venafi.features.bases.feature_base import FeatureBase, FeatureError, ApiPreferences, feature
from venafi.properties.secret_store import KeyNames, Namespaces, VaultTypes


class _WorkflowBase(FeatureBase):
    def __init__(self, auth):
        super().__init__(auth=auth)

    def delete(self, workflow_dn: str):
        self._secret_store_delete(object_dn=workflow_dn)
        self._config_delete(object_dn=workflow_dn)

    def _create(self, name: str, parent_folder_dn: str, is_adaptable: bool, stage: int, injection_command: str = None,
                application_class_name: str = None, approvers: str = None, reason_code: int = None):
        if self._auth.preference == ApiPreferences.aperture:
            self._log_not_implemented_warning(ApiPreferences.aperture)

        workflow = self._config_create(
            name=name,
            parent_folder_dn=parent_folder_dn,
            config_class=WorkflowClassNames.workflow if not is_adaptable else WorkflowClassNames.adaptable_workflow
        )

        if is_adaptable:
            driver_str = '037Venafi.Drivers.AdaptableWFApplication'
        else:
            driver_str = '028Venafi.Drivers.WFApplication'
        if application_class_name:
            stage_str = f'B&{len(str(stage)):03d}{stage}D-{len(application_class_name):03d}{application_class_name}'
        else:
            stage_str = f'B-{len(str(stage)):03d}{stage}'

        injection_command_str = f'B&{len(injection_command):03d}{injection_command}' if injection_command else ''
        approvers_str = f'C-{"0" * (3 - len(str(len(approvers))))}{str(len(approvers))}{approvers}'
        reason_code_str = f'{"0" * (3 - len(str(reason_code)))}{reason_code}'

        rule = f'{driver_str}{stage_str}{injection_command_str}{approvers_str}{reason_code_str}'.encode('utf-8')
        rule = base64.b64encode(rule)

        vault_id = self._auth.websdk.SecretStore.Add.post(
            base_64_data=rule.decode('utf-8'),
            vault_type=VaultTypes.blob,
            owner=workflow.dn,
            keyname=KeyNames.software_default,
            namespace=Namespaces.config
        ).vault_id

        self._auth.websdk.Config.AddValue.post(
            object_dn=workflow.dn,
            attribute_name=WorkflowAttributes.rule_vault_id,
            value=vault_id
        )

        return workflow


@feature()
class ResultCode(FeatureBase):
    def __init__(self, auth):
        super().__init__(auth=auth)

        self._workflow_dn = r'\VED\Workflow Tickets'

    def create(self, code: int, name: str, description: str):
        if self._auth.preference == ApiPreferences.aperture:
            self._log_not_implemented_warning(ApiPreferences.aperture)

        result = self._auth.websdk.Config.AddValue.post(
            object_dn=self._workflow_dn,
            attribute_name=WorkflowAttributes.Standard.approval_reason,
            value=f'{code},{name},{description}'
        )
        result.assert_valid_response()

        return [code, name, description]

    def delete(self, code: int, name: str = None):
        if self._auth.preference == ApiPreferences.aperture:
            self._log_not_implemented_warning(ApiPreferences.aperture)

        result_codes = self._auth.websdk.Config.ReadDn.post(
            object_dn=self._workflow_dn,
            attribute_name=WorkflowAttributes.Standard.approval_reason
        ).values

        if not result_codes:
            return

        search_string = f'{code},{name}' if name else f'{code}'
        for rc in result_codes:
            if search_string in rc:
                result = self._auth.websdk.Config.RemoveDnValue.post(
                    object_dn=self._workflow_dn,
                    attribute_name=WorkflowAttributes.Standard.approval_reason,
                    value=rc
                )
                result.assert_valid_response()


@feature()
class AdaptableWorkflow(_WorkflowBase):
    def __init__(self, auth):
        super().__init__(auth=auth)

    def create(self, name: str, parent_folder_dn: str, stage: int, powershell_script_name: str, powershell_script_hash: str,
               approver_guids: List[str] = None, reason_code: int = None, use_approvers_from_powershell_script: bool = False):
        if self._auth.preference == ApiPreferences.aperture:
            self._log_not_implemented_warning(ApiPreferences.aperture)

        if approver_guids:
            approvers = ','.join(approver_guids)
        elif use_approvers_from_powershell_script:
            approvers = "$CONFIG[$SELFDN$,'Adaptable Workflow Approvers']$"
        else:
            approvers = ''

        workflow = self._create(
            name=name,
            parent_folder_dn=parent_folder_dn,
            is_adaptable=True,
            stage=stage,
            approvers=approvers,
            reason_code=reason_code
        )

        add_value = lambda x, y, z: self._auth.websdk.Config.AddValue.post(object_dn=x, attribute_name=y, value=z)
        add_value(workflow.dn, WorkflowAttributes.Adaptable.powershell_script, powershell_script_name)

        vault_id = self._auth.websdk.SecretStore.Add.post(
            base_64_data=powershell_script_hash,
            keyname=KeyNames.software_default,
            vault_type=VaultTypes.blob,
            namespace=Namespaces.config,
            owner=workflow.dn
        ).vault_id

        self._auth.websdk.Config.WriteDn.post(
            object_dn=workflow.dn,
            attribute_name=WorkflowAttributes.Adaptable.powershell_script_hash_vault_id,
            values=[vault_id]
        )

        return workflow


@feature()
class StandardWorkflow(_WorkflowBase):
    def __init__(self, auth):
        super().__init__(auth=auth)

    def create(self, name: str, parent_folder_dn: str, stage: int, injection_command: str = None, application_class_name: str = None,
               approver_guids: List[str] = None, macro: str = None, reason_code: int = None):
        if self._auth.preference == ApiPreferences.aperture:
            self._log_not_implemented_warning(ApiPreferences.aperture)

        if approver_guids:
            approvers = ','.join(approver_guids)
        elif macro:
            approvers = macro
        else:
            approvers = ''

        workflow = self._create(
            name=name,
            parent_folder_dn=parent_folder_dn,
            is_adaptable=False,
            stage=stage,
            injection_command=injection_command,
            application_class_name=application_class_name,
            approvers=approvers,
            reason_code=reason_code
        )

        return workflow


@feature()
class Ticket(FeatureBase):
    def __init__(self, auth):
        super().__init__(auth=auth)

    @staticmethod
    def _validate_result_code(result):
        if result.code != 1:
            raise FeatureError.InvalidResultCode(code=result.code, code_description=result.workflow_result)

    def create(self, object_dn: str, workflow_dn: str, approver_guids: List[str], reason: str, user_data: str = None):
        if self._auth.preference == ApiPreferences.aperture:
            self._log_not_implemented_warning(ApiPreferences.aperture)

        response = self._auth.websdk.Workflow.Ticket.Create.post(
            object_dn=object_dn,
            workflow_dn=workflow_dn,
            approvers=[
                {'PrefixedName': guid} for guid in approver_guids
            ],
            reason=reason,
            user_data=user_data
        )
        self._validate_result_code(response.result)
        return response.guid

    def delete(self, ticket_guid: str):
        if self._auth.preference == ApiPreferences.aperture:
            self._log_not_implemented_warning(ApiPreferences.aperture)

        result = self._auth.websdk.Workflow.Ticket.Delete.post(guid=ticket_guid).result
        self._validate_result_code(result)

    def details(self, ticket_guid: str):
        if self._auth.preference == ApiPreferences.aperture:
            self._log_not_implemented_warning(ApiPreferences.aperture)

        response = self._auth.websdk.Workflow.Ticket.Details.post(guid=ticket_guid)
        self._validate_result_code(result=response.result)
        return response.details

    def enumerate(self, object_dn: str = None, user_data: str = None):
        if self._auth.preference == ApiPreferences.aperture:
            self._log_not_implemented_warning(ApiPreferences.aperture)

        response = self._auth.websdk.Workflow.Ticket.Enumerate.post(
            object_dn=object_dn,
            user_data=user_data
        )
        self._validate_result_code(result=response.result)
        return response.guids

    def exists(self, ticket_guid: str):
        if self._auth.preference == ApiPreferences.aperture:
            self._log_not_implemented_warning(ApiPreferences.aperture)

        result = self._auth.websdk.Workflow.Ticket.Exists.post(guid=ticket_guid).result
        return result.code == 1

    def status(self, ticket_guid: str):
        if self._auth.preference == ApiPreferences.aperture:
            self._log_not_implemented_warning(ApiPreferences.aperture)

        response = self._auth.websdk.Workflow.Ticket.Status.post(guid=ticket_guid)
        self._validate_result_code(result=response.result)
        return response.status

    def update_status(self, ticket_guid: str, status: str, explanation: str = None, scheduled_start: datetime = None,
                      scheduled_stop: datetime = None):
        if self._auth.preference == ApiPreferences.aperture:
            self._log_not_implemented_warning(ApiPreferences.aperture)

        result = self._auth.websdk.Workflow.Ticket.UpdateStatus.post(
            guid=ticket_guid,
            status=status,
            explanation=explanation,
            scheduled_start=scheduled_start.isoformat() if scheduled_start else None,
            scheduled_stop=scheduled_stop.isoformat() if scheduled_stop else None
        ).result
        self._validate_result_code(result)
