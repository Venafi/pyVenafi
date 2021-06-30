from typing import Union
from pytpp.vtypes import Config
from pytpp.features.bases.feature_base import FeatureBase, FeatureError, feature
from pytpp.properties.config import ClientGroupsAttributeValues, ClientGroupsAttributes, ClientGroupsClassNames


@feature()
class ClientGroups(FeatureBase):
    def __init__(self, api):
        super().__init__(api)

        self._group_base_dn = r'\VED\Clients\Groups'
        self._work_base_dn = r'\VED\Clients\Work'

    def assign_work(self, group: Union['Config.Object', str], work_name: str):
        """
        Assigns work to the client group

        Args:
            group: The Config.Object or name of the client group.
            work_name: The name of the work
        """
        group_dn = self._get_dn(group, parent_dn=self._group_base_dn)
        response = self._api.websdk.Config.Write.post(
            object_dn=group_dn,
            attribute_data=self._name_value_list({
                ClientGroupsAttributes.assigned_work: [fr'{self._work_base_dn}\{work_name}']
            })
        )

        if response.result.code != 1:
            raise FeatureError.InvalidResultCode(code=response.result.code,
                                                 code_description=response.result.credential_result)

    def create(self, name: str, agent_type: str = ClientGroupsAttributeValues.AgentType.agentless,
               get_if_already_exists: bool = True):
        """
        Creates a client group

        Args:
            name: The name of the client group.
            agent_type: The type of the client group
            get_if_already_exists: If the objects already exists, just return it as is.

        Returns:
            Config object representing the client group.
        """
        if agent_type == ClientGroupsAttributeValues.AgentType.agent_installed:
            attributes = {
                ClientGroupsAttributes.created_by: ClientGroupsAttributeValues.CreatedBy.websdk,
                ClientGroupsAttributes.agent_type: ClientGroupsAttributeValues.AgentType.agent_installed,
                ClientGroupsAttributes.rule      : ClientGroupsAttributeValues.DefaultRules.agent_installed
            }
        elif agent_type == ClientGroupsAttributeValues.AgentType.agentless:
            attributes = {
                ClientGroupsAttributes.created_by: ClientGroupsAttributeValues.CreatedBy.websdk,
                ClientGroupsAttributes.agent_type: ClientGroupsAttributeValues.AgentType.agentless,
                ClientGroupsAttributes.rule      : ClientGroupsAttributeValues.DefaultRules.agentless
            }
        elif agent_type == ClientGroupsAttributeValues.AgentType.deploy_user_and_device_certificates:
            attributes = {
                ClientGroupsAttributes.created_by: ClientGroupsAttributeValues.CreatedBy.websdk,
                ClientGroupsAttributes.agent_type: ClientGroupsAttributeValues.AgentType.deploy_user_and_device_certificates,
                ClientGroupsAttributes.rule      : ClientGroupsAttributeValues.DefaultRules.deploy_user_and_device_certificates
            }
        elif agent_type == ClientGroupsAttributeValues.AgentType.certificate_enrollment:
            attributes = {
                ClientGroupsAttributes.created_by: ClientGroupsAttributeValues.CreatedBy.websdk,
                ClientGroupsAttributes.agent_type: ClientGroupsAttributeValues.AgentType.certificate_enrollment,
                ClientGroupsAttributes.rule      : ClientGroupsAttributeValues.DefaultRules.certificate_enrollment
            }
        else:
            raise FeatureError.UnexpectedValue(
                f"Invalid input for parameter: 'agent_type', unknown value: {agent_type}")

        return self._config_create(
            name=name,
            parent_folder_dn=self._group_base_dn,
            config_class=ClientGroupsClassNames.group,
            attributes=attributes,
            get_if_already_exists=get_if_already_exists
        )

    def delete(self, group: Union['Config.Object', str]):
        """
        Deletes a client group

        Args:
            group: The Config.Object or name of the client group.
        """
        group_dn = self._get_dn(group, parent_dn=self._group_base_dn)
        self._config_delete(object_dn=group_dn)

    def get(self, name: str):
        """
        Gets a client group by name and returns a config object

        Args:
            name: The name of the client group.

        Returns:
            Config object representing the client group.
        """
        return self._get_config_object(object_dn=fr'{self._group_base_dn}\{name}')

    def list(self):
        """
        Gets all client groups as a list

        Args:

        Returns:
            A list of config object representing the client groups.
        """
        response = self._api.websdk.Config.Enumerate.post(object_dn=self._group_base_dn)

        if response.result.code != 1:
            raise FeatureError.InvalidResultCode(
                code=response.result.code,
                code_description=response.result.credential_result
            )
        return response.objects

    def remove_work(self, group: Union['Config.Object', str], work_name: str):
        """
        Removes work from a client group

        Args:
            group: The Config.Object or name of the client group.
            work_name: The name of the work to be removed.

        Returns:
            A list of config object representing the client groups.
        """
        group_dn = self._get_dn(group, parent_dn=self._group_base_dn)
        response = self._api.websdk.Config.RemoveDnValue.post(
            object_dn=group_dn,
            attribute_name=ClientGroupsAttributes.assigned_work,
            value=fr'{self._work_base_dn}\{work_name}'
        )
        if response.result.code != 1:
            raise FeatureError.InvalidResultCode(
                code=response.result.code,
                code_description=response.result.credential_result
            )
