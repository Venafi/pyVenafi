import base64
import hashlib
from typing import List
from datetime import datetime
from pytpp.vtypes import Config, Identity
from pytpp.properties.config import WorkflowClassNames, WorkflowAttributes, WorkflowAttributeValues
from pytpp.features.bases.feature_base import FeatureBase, FeatureError, feature
from pytpp.properties.secret_store import KeyNames, Namespaces, VaultTypes


class _WorkflowBase(FeatureBase):
    def __init__(self, api):
        super().__init__(api=api)

    def delete(self, workflow: 'Config.Object'):
        """
        Deletes a workflow.

        Args:
            workflow: Config object of the workflow object.
        """
        self._secret_store_delete(object_dn=workflow.dn)
        self._config_delete(object_dn=workflow.dn)

    def _create(self, name: str, parent_folder_dn: str, is_adaptable: bool, stage: int, injection_command: str = None,
                application_class_name: str = None, approvers: str = None, reason_code: int = None, attributes: dict = None):
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

        vault_id = self._api.websdk.SecretStore.Add.post(
            base_64_data=rule.decode('utf-8'),
            vault_type=VaultTypes.blob,
            owner=workflow.dn,
            keyname=KeyNames.software_default,
            namespace=Namespaces.config
        ).vault_id

        self._api.websdk.Config.AddValue.post(
            object_dn=workflow.dn,
            attribute_name=WorkflowAttributes.rule_vault_id,
            value=vault_id
        )

        return workflow


@feature()
class AdaptableWorkflow(_WorkflowBase):
    def __init__(self, api):
        super().__init__(api=api)

    def create(self, name: str, parent_folder_dn: str, stage: int, powershell_script_name: str, powershell_script_content: bytes,
               approvers: 'List[Identity.Identity]' = None, reason_code: int = None,
               use_approvers_from_powershell_script: bool = False, attributes: dict = None):
        """
        Creates an Adaptable Workflow object. The ``powershell_script_name`` must be the name of an actual PowerShell script
        located on the TPP server(s) that will process this workflow. The ``powershell_script_content`` is the content of the
        PowerShell script as bytes. This is required to create the Base64 hash of the SHA256 hash of the UTF-32LE-encoded
        PowerShell script. Without the PowerShell script hash TPP cannot trust using the Adaptable Workflow until the hash
        is verified.

         Examples:
            .. code-block::python

                from pytpp import Authenticate, Features

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

        If a list of approver identity objects is provided, they will be added to the workflow as dedicated
        approvers of the workflow. If the approvers should come from the PowerShell script, do not supply this parameter.
        Instead, set ``use_approvers_from_powershell_script = True``. If the approvers should come from the object requiring
        the workflow, such as the certificate object, then do not supply ``approvers`` or
        ``use_approvers_from_powershell_script``.

        Args:
            name: Name of the workflow object.
            parent_folder_dn: Absolute path to the parent folder of the workflow object.
            stage: One of the valid stages that represent the certificate lifecycle.
            powershell_script_name: Name (not path) of the actual PowerShell script on the TPP server.
            powershell_script_content: Contents of the PowerShell script as bytes.
            approvers: List of identity objects for each approver.
            reason_code: Integer reason code.
            use_approvers_from_powershell_script: If ``True`` and no ``approvers`` is supplied, then set the
                workflow to use the approvers defined by the script.
            attributes: Additional attributes to apply to the workflow object.
        Returns:
            Config Object of the workflow.
        """
        if approvers:
            wf_approvers = ','.join([a.prefixed_universal for a in approvers])
        elif use_approvers_from_powershell_script:
            wf_approvers = "$CONFIG[$SELFDN$,'Adaptable Workflow Approvers']$"
        else:
            wf_approvers = ''

        workflow = self._create(
            name=name,
            parent_folder_dn=parent_folder_dn,
            is_adaptable=True,
            stage=stage,
            approvers=wf_approvers,
            reason_code=reason_code,
            attributes=attributes
        )

        add_value = lambda x, y, z: self._api.websdk.Config.AddValue.post(object_dn=x, attribute_name=y, value=z)
        add_value(workflow.dn, WorkflowAttributes.Adaptable.powershell_script, powershell_script_name)

        vault_id = self._api.websdk.SecretStore.Add.post(
            base_64_data=self._calculate_hash(powershell_script_content),
            keyname=KeyNames.software_default,
            vault_type=VaultTypes.blob,
            namespace=Namespaces.config,
            owner=workflow.dn
        ).vault_id

        self._api.websdk.Config.WriteDn.post(
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

                from pytpp import Authenticate, Features

                api = Authenticate(...)  # ... is short-hand for the parameters
                features = Features(api)

                with open('./local/path/to/script.ps1', 'rb') as f:
                    content = f.read()

                hash = features.workflow.adaptable._calculate_hash(script_content=content)
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


class RC:
    def __init__(self, code, name, description):
        self.code = code
        self.name = name
        self.description = description


@feature()
class ReasonCode(FeatureBase):
    def __init__(self, api):
        super().__init__(api=api)

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
        result = self._api.websdk.Config.AddValue.post(
            object_dn=self._workflow_dn,
            attribute_name=WorkflowAttributes.Standard.approval_reason,
            value=f'{code},{name},{description}'
        )
        result.assert_valid_response()

        return RC(name=name, code=code, description=description)

    def delete(self, code: int, name: str = None):
        """
        Deletes a result code. ``name`` is not required, but when supplied, in the
        event that multiple codes exist with the same integer value, only the ones
        having ``name`` will be deleted.

        Args:
            code: An integer code.
            name: Name of the result code.
        """
        result_codes = self._api.websdk.Config.ReadDn.post(
            object_dn=self._workflow_dn,
            attribute_name=WorkflowAttributes.Standard.approval_reason
        ).values

        if not result_codes:
            return

        search_string = f'{code},{name}' if name else f'{code}'
        for rc in result_codes:
            if search_string in rc:
                result = self._api.websdk.Config.RemoveDnValue.post(
                    object_dn=self._workflow_dn,
                    attribute_name=WorkflowAttributes.Standard.approval_reason,
                    value=rc
                )
                result.assert_valid_response()


@feature()
class StandardWorkflow(_WorkflowBase):
    def __init__(self, api):
        super().__init__(api=api)

    def create(self, name: str, parent_folder_dn: str, stage: int, injection_command: str = None, application_class_name: str = None,
               approvers: 'List[Identity.Identity]' = None, macro: str = None, reason_code: int = None, attributes: dict = None):
        """
        Creates a Standard Workflow object.

        TPP requires that one of ``injection_command`` or ``approvers`` be supplied.

        If a list of approver identity objects is provided, they will be added to the workflow as dedicated approvers of the workflow.
        If the approvers should come from the object requiring the workflow, such as the certificate object, then do not supply
        ``approvers``. If the approvers come from a TPP Macro, then supply ``macro`` with the desired macro.

        If an ``injection_command`` is supplied, then that command will be invoked during the workflow.

        If an ``application_class_name`` is supplied, then the workflow will only apply to application objects of this class.
        Otherwise all applications are subject to this workflow.

        Args:
            name: Name of the workflow object.
            parent_folder_dn: Absolute path to the parent folder of the workflow object.
            stage: One of the valid stages that represent the certificate lifecycle.
            injection_command: Command to be invoked on the target application.
            application_class_name: Application Class Name to trigger this workflow.
            approvers: List of identity objects for each approver.
            macro: TPP Approver Macro.
            reason_code: Integer reason code.
            attributes: Additional attributes to apply to the workflow object.
        Returns:
            Config Object of the workflow.
        """
        if approvers:
            wf_approvers = ','.join([a.prefixed_universal for a in approvers])
        elif macro:
            wf_approvers = macro
        else:
            wf_approvers = ''

        workflow = self._create(
            name=name,
            parent_folder_dn=parent_folder_dn,
            is_adaptable=False,
            stage=stage,
            injection_command=injection_command,
            application_class_name=application_class_name,
            approvers=wf_approvers,
            reason_code=reason_code,
            attributes=attributes
        )

        return workflow


@feature()
class Ticket(FeatureBase):
    def __init__(self, api):
        super().__init__(api=api)
        self._workflow_ticket_dn = r'\VED\Workflow Tickets'

    @staticmethod
    def _validate_result_code(result):
        if result.code != 1:
            raise FeatureError.InvalidResultCode(code=result.code, code_description=result.workflow_result)

    def create(self, obj: 'Config.Object', workflow: 'Config.Object', approvers: 'List[Identity.Identity]', 
               reason: str, user_data: str = None):
        """
        Creates a workflow ticket on ``obj`` if the object is in a state to received a workflow ticket.

        Args:
            obj: Config object of the object requiring a workflow ticket.
            workflow: Config object of the Workflow object DN that blocks the workflow.
            approvers: List of identity objects for each approver.
            reason: Integer reason code.
            user_data: User data.

        Returns:
            Workflow ticket name.
        """
        response = self._api.websdk.Workflow.Ticket.Create.post(
            object_dn=obj.dn,
            workflow_dn=workflow.dn,
            approvers=[
                {'PrefixedName': a.prefixed_name} for a in approvers
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
        result = self._api.websdk.Workflow.Ticket.Delete.post(guid=ticket_name).result
        self._validate_result_code(result)

    def details(self, ticket_name: str):
        """
        Returns the details of a ticket request.

        Args:
            ticket_name: Name of the workflow ticket.

        Returns:
            Ticket Details object.
        """
        response = self._api.websdk.Workflow.Ticket.Details.post(guid=ticket_name)
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
        result = self._api.websdk.Workflow.Ticket.Exists.post(guid=ticket_name).result
        return result.code == 1

    def get(self, obj: 'Config.Object', user_data: str = None, expected_num_tickets: int = 1, timeout: int = 10):
        """
        Gets all tickets associated to ``obj``. If the minimum expected number of tickets do not
        appear on the ``obj``, then a warning is logged and whatever was found is returned and no
        error is raised.

        An optional ``timeout`` parameter can be used to wait for the above to be ``True``.

        Args:
            obj: Config object of the object with a workflow ticket issued to it.
            user_data: The string to filter results using the User Data attribute of the
                workflow ticket.
            expected_num_tickets: Minimum number of tickets expected to be written for the certificate.
            timeout: Time in seconds to wait for a ticket DN value. Default is 10 seconds.

        Returns:
            List of Config Objects
        """
        def get_tickets():
            ticket_names = self._api.websdk.Workflow.Ticket.Enumerate.post(
                object_dn=obj.dn,
                user_data=user_data
            ).guids

            return [
                self._api.websdk.Config.IsValid.post(
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
                msg=f'The expected number of tickets on {obj.dn} was '
                    f'{expected_num_tickets}, but {len(tickets)} tickets were '
                    f'found instead.'
            )
            return tickets
        else:
            tickets = get_tickets()
            if len(tickets) < expected_num_tickets:
                self._log_warning_message(
                    msg=f'The expected number of tickets on {obj.dn} was '
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
        response = self._api.websdk.Workflow.Ticket.Status.post(guid=ticket_name)
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
        result = self._api.websdk.Workflow.Ticket.UpdateStatus.post(
            guid=ticket_name,
            status=status,
            explanation=explanation,
            scheduled_start=scheduled_start.isoformat() if scheduled_start else None,
            scheduled_stop=scheduled_stop.isoformat() if scheduled_stop else None
        ).result
        self._validate_result_code(result)
