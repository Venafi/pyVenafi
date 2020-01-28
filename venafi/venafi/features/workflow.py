import base64
import hashlib
from typing import List
from datetime import datetime
from venafi.properties.config import WorkflowClassNames, WorkflowAttributes, WorkflowAttributeValues
from venafi.features.bases.feature_base import FeatureBase, FeatureError, ApiPreferences, feature
from venafi.properties.secret_store import KeyNames, Namespaces, VaultTypes


class _WorkflowBase(FeatureBase):
    def __init__(self, auth):
        super().__init__(auth=auth)

    def delete(self, workflow_dn: str):
        """
        Deletes a workflow.

        Args:
            workflow_dn: Absolute path to the workflow object.
        """
        self._secret_store_delete(object_dn=workflow_dn)
        self._config_delete(object_dn=workflow_dn)

    def _create(self, name: str, parent_folder_dn: str, is_adaptable: bool, stage: int, injection_command: str = None,
                application_class_name: str = None, approvers: str = None, reason_code: int = None, attributes: dict = None):
        if self._auth.preference == ApiPreferences.aperture:
            self._log_not_implemented_warning(ApiPreferences.aperture)

        workflow = self._config_create(
            name=name,
            parent_folder_dn=parent_folder_dn,
            config_class=WorkflowClassNames.workflow if not is_adaptable else WorkflowClassNames.adaptable_workflow,
            attributes=attributes
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
class AdaptableWorkflow(_WorkflowBase):
    def __init__(self, auth):
        super().__init__(auth=auth)

    def create(self, name: str, parent_folder_dn: str, stage: int, powershell_script_name: str, powershell_script_content: bytes,
               approver_guids: List[str] = None, reason_code: int = None, use_approvers_from_powershell_script: bool = False,
               attributes: dict = None):
        """
        Creates an Adaptable Workflow object. The ``powershell_script_name`` must be the name of an actual PowerShell script
        located on the TPP server(s) that will process this workflow. The ``powershell_script_content`` is the content of the
        PowerShell script as bytes. This is required to create the Base64 hash of the SHA256 hash of the UTF-32LE-encoded
        PowerShell script. Without the PowerShell script hash TPP cannot trust using the Adaptable Workflow until the hash
        is verified.

         Examples:
            .. code-block::python

                from venafi import Authenticate, Features

                api = Authenticate(...)  # ... is short-hand for the parameters
                features = Features(api)

                with open('./local/path/to/SuperAwesomeScript.ps1', 'rb') as f:
                    content = f.read()

                adaptable_workflow = features.workflow.adaptable.create(
                    ...,
                    powershell_script_name='SuperAwesomeScript',
                    powershell_script_content=content
                    ...
                )

        If a list of user GUIDS, or prefixed universal GUIDS, is provided, the will be added to the workflow as dedicated
        approvers of the workflow. If the approvers should come from the PowerShell script, do not supply this parameter.
        Instead, set ``use_approvers_from_powershell_script = True``. If the approvers should come from the object requiring
        the workflow, such as the certificate object, then do not supply ``approver_guids`` or
        ``use_approvers_from_powershell_script``.

        Args:
            name: Name of the workflow object.
            parent_folder_dn: Absolute path to the parent folder of the workflow object.
            stage: One of the valid stages that represent the certificate lifecycle.
            powershell_script_name: Name (not path) of the actual PowerShell script on the TPP server.
            powershell_script_content: Contents of the PowerShell script as bytes.
            approver_guids: List of prefixed universal GUIDS for each approver identity.
            reason_code: Integer reason code.
            use_approvers_from_powershell_script: If ``True`` and no ``approver_guids`` is supplied, then set the
                workflow to use the approvers defined by the script.
            attributes: Additional attributes to apply to the workflow object.
        Returns:
            Config Object of the workflow.
        """
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
            reason_code=reason_code,
            attributes=attributes
        )

        add_value = lambda x, y, z: self._auth.websdk.Config.AddValue.post(object_dn=x, attribute_name=y, value=z)
        add_value(workflow.dn, WorkflowAttributes.Adaptable.powershell_script, powershell_script_name)

        vault_id = self._auth.websdk.SecretStore.Add.post(
            base_64_data=self._calculate_hash(powershell_script_content),
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

    @staticmethod
    def _calculate_hash(script_content: bytes):
        """
        Calculates the hash of the Adaptable Workflow script that TPP would store. This is useful when creating or modifying
        an Adaptable Workflow script.

        Examples:
            .. code-block::python

                from venafi import Authenticate, Features

                api = Authenticate(...)  # ... is short-hand for the parameters
                features = Features(api)

                with open('./local/path/to/script.ps1', 'rb') as f:
                    content = f.read()

                hash = features.workflow.adaptable.calculate_hash(script_content=content)
                adaptable_workflow = features.workflow.adaptable.create(
                    ...,
                    powershell_script_hash=hash,
                    ...
                )

        Args:
            script_content: The raw content of the Adaptable Workflow script as bytes.

        Returns:
            Base64 data of the SHA 256 hash of the UTF-32LE encoded script.
        """
        return base64.b64encode(
            hashlib.sha256(
                script_content.decode().encode('utf-32-le')
            ).hexdigest().encode()
        ).decode()


@feature()
class ReasonCode(FeatureBase):
    def __init__(self, auth):
        super().__init__(auth=auth)

        self._workflow_dn = r'\VED\Workflow Tickets'

    def create(self, code: int, name: str, description: str):
        """
        Creates a workflow result code.

        Args:
            code: An integer code.
            name: Name of the result code.
            description: Purpose of the result code.

        Returns:
            List of ``code``, ``name``, and ``description``.
        """
        if self._auth.preference == ApiPreferences.aperture:
            self._log_not_implemented_warning(ApiPreferences.aperture)

        result = self._auth.websdk.Config.AddValue.post(
            object_dn=self._workflow_dn,
            attribute_name=WorkflowAttributes.Standard.approval_reason,
            value=f'{code},{name},{description}'
        )
        result.assert_valid_response()

        class RC:
            def __init__(self):
                self.code = code
                self.name = name
                self.description = description

        return RC()

    def delete(self, code: int, name: str = None):
        """
        Deletes a result code. ``name`` is not required, but when supplied, in the
        event that multiple codes exist with the same integer value, only the ones
        having ``name`` will be deleted.

        Args:
            code: An integer code.
            name: Name of the result code.
        """
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
class StandardWorkflow(_WorkflowBase):
    def __init__(self, auth):
        super().__init__(auth=auth)

    def create(self, name: str, parent_folder_dn: str, stage: int, injection_command: str = None, application_class_name: str = None,
               approver_guids: List[str] = None, macro: str = None, reason_code: int = None, attributes: dict = None):
        """
        Creates a Standard Workflow object.

        TPP requires that one of ``injection_command`` or ``approver_guids`` be supplied.

        If a list of user GUIDS, or prefixed universal GUIDS, is provided, the will be added to the workflow as dedicated
        approvers of the workflow. If the approvers should come from the object requiring the workflow, such as the certificate
        object, then do not supply ``approver_guids``. If the approvers come from a TPP Macro, then supply ``macro`` with the
        desired macro.

        If an ``injection_command`` is supplied, then that command will be invoked during the workflow.

        If an ``application_class_name`` is supplied, then the workflow will only apply to application objects of this class.
        Otherwise all applications are subject to this workflow.

        Args:
            name: Name of the workflow object.
            parent_folder_dn: Absolute path to the parent folder of the workflow object.
            stage: One of the valid stages that represent the certificate lifecycle.
            injection_command: Command to be invoked on the target application.
            application_class_name: Application Class Name to trigger this workflow.
            approver_guids: List of prefixed universal GUIDS for each approver identity.
            macro: TPP Approver Macro.
            reason_code: Integer reason code.
            attributes: Additional attributes to apply to the workflow object.
        Returns:
            Config Object of the workflow.
        """
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
            reason_code=reason_code,
            attributes=attributes
        )

        return workflow


@feature()
class Ticket(FeatureBase):
    def __init__(self, auth):
        super().__init__(auth=auth)
        self._workflow_ticket_dn = r'\VED\Workflow Tickets'

    @staticmethod
    def _validate_result_code(result):
        if result.code != 1:
            raise FeatureError.InvalidResultCode(code=result.code, code_description=result.workflow_result)

    def create(self, object_dn: str, workflow_dn: str, approver_guids: List[str], reason: str, user_data: str = None):
        """
        Creates a workflow ticket on ``object_dn`` if the object is in a state to received a workflow ticket.

        Args:
            object_dn: Absolute path to the object requiring a workflow ticket.
            workflow_dn: Absolute path to the Workflow object DN that blocks the workflow.
            approver_guids: List of approver identities by prefixed universal GUID.
            reason: Integer reason code.
            user_data: User data.

        Returns:
            Workflow ticket name.
        """
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

    def delete(self, ticket_name: str):
        """
        Deletes a workflow ticket.

        Args:
            ticket_name: Name of the workflow ticket.
        """
        if self._auth.preference == ApiPreferences.aperture:
            self._log_not_implemented_warning(ApiPreferences.aperture)

        result = self._auth.websdk.Workflow.Ticket.Delete.post(guid=ticket_name).result
        self._validate_result_code(result)

    def details(self, ticket_name: str):
        """
        Returns the details of a ticket request.

        Args:
            ticket_name: Name of the workflow ticket.

        Returns:
            Ticket Details object.
        """
        if self._auth.preference == ApiPreferences.aperture:
            self._log_not_implemented_warning(ApiPreferences.aperture)

        response = self._auth.websdk.Workflow.Ticket.Details.post(guid=ticket_name)
        self._validate_result_code(result=response.result)
        return response.details

    def exists(self, ticket_name: str):
        """
        Returns ``True`` when a particular workflow exists, otherwise ``False``.

        Args:
            ticket_name: Name of the workflow ticket.

        Returns:
            ``True`` when a particular workflow exists, otherwise ``False``.
        """
        if self._auth.preference == ApiPreferences.aperture:
            self._log_not_implemented_warning(ApiPreferences.aperture)

        result = self._auth.websdk.Workflow.Ticket.Exists.post(guid=ticket_name).result
        return result.code == 1

    def get(self, object_dn: str, user_data: str = None, expected_num_tickets: int = 1, timeout: int = 10):
        """
        Gets all tickets associated to ``object_dn``. If the minimum expected number of tickets do not
        appear on the ``object_dn``, then a warning is logged and whatever was found is returned and no
        error is raised.

        An optional ``timeout`` parameter can be used to wait for the above to be ``True``.

        Args:
            object_dn: Absolute path to the object with a workflow ticket issued to it.
            user_data: The string to filter results using the User Data attribute of the
                workflow ticket.
            expected_num_tickets: Minimum number of tickets expected to be written for the certificate.
            timeout: Time in seconds to wait for a ticket DN value. Default is 10 seconds.

        Returns:
            List of Config Objects
        """
        if self._auth.preference == ApiPreferences.aperture:
            self._log_not_implemented_warning(ApiPreferences.aperture)

        def get_tickets():
            ticket_names = self._auth.websdk.Workflow.Ticket.Enumerate.post(
                object_dn=object_dn,
                user_data=user_data
            ).guids

            return [
                self._auth.websdk.Config.IsValid.post(
                    object_dn=f'{self._workflow_ticket_dn}\\{ticket_name}'
                ).object
                for ticket_name in ticket_names
            ]

        if timeout:
            tickets = []
            with self._Timeout(timeout=timeout) as to:
                while not to.is_expired():
                    tickets = get_tickets()
                    if len(tickets) >= expected_num_tickets:
                        return tickets

            self._log_warning_message(
                msg=f'The expected number of tickets on {object_dn} was '
                    f'{expected_num_tickets}, but {len(tickets)} tickets were '
                    f'found instead.'
            )
            return tickets
        else:
            tickets = get_tickets()
            if len(tickets) < expected_num_tickets:
                self._log_warning_message(
                    msg=f'The expected number of tickets on {object_dn} was '
                        f'{expected_num_tickets}, but {len(tickets)} tickets were '
                        f'found instead.'
                )
            return tickets

    def status(self, ticket_name: str):
        """
        Returns the current status of a workflow ticket.

        Args:
            ticket_name: Name of the workflow ticket.

        Returns:
            The current status of a workflow ticket.
        """
        if self._auth.preference == ApiPreferences.aperture:
            self._log_not_implemented_warning(ApiPreferences.aperture)

        response = self._auth.websdk.Workflow.Ticket.Status.post(guid=ticket_name)
        self._validate_result_code(result=response.result)
        return response.status

    def update_status(self, ticket_name: str, status: str, explanation: str = None, scheduled_start: datetime = None,
                      scheduled_stop: datetime = None):
        """
        Updates the status of a workflow ticket with the optional explanations and scheduled approvals. Marking a
        ticket as "Approved" will automatically delete the ticket.

        Args:
            ticket_name: Name of the workflow ticket.
            status: The new status of the workflow ticket.
            explanation: Reason for the new status.
            scheduled_start: Date/time to continue the approval process.
            scheduled_stop:  Date/time to expire the approval process.
        """
        if self._auth.preference == ApiPreferences.aperture:
            self._log_not_implemented_warning(ApiPreferences.aperture)

        result = self._auth.websdk.Workflow.Ticket.UpdateStatus.post(
            guid=ticket_name,
            status=status,
            explanation=explanation,
            scheduled_start=scheduled_start.isoformat() if scheduled_start else None,
            scheduled_stop=scheduled_stop.isoformat() if scheduled_stop else None
        ).result
        self._validate_result_code(result)
