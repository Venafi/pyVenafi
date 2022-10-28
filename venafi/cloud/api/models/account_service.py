from __future__ import annotations
from venafi.cloud.api.api_base import ApiField, ObjectModel
from uuid import UUID
from typing import (Dict, List, Any, Literal)
from datetime import datetime


class ApiKeyInformation(ObjectModel):
    key: UUID = ApiField(alias='key')
    userId: UUID = ApiField(alias='userId')
    username: str = ApiField(alias='username')
    companyId: UUID = ApiField(alias='companyId')
    apiVersion: Literal['ALL', 'V1'] = ApiField(alias='apiVersion')
    apiKeyStatus: Literal['ACTIVE', 'EXPIRED', 'INACTIVE', 'PENDING_ACTIVATION', 'PENDING_ROTATION', 'ROTATED'] = ApiField(alias='apiKeyStatus')
    creationDate: datetime = ApiField(alias='creationDate')
    validityStartDate: datetime = ApiField(alias='validityStartDate')
    validityEndDate: datetime = ApiField(alias='validityEndDate')


class ApiKeyNullResponse(ObjectModel):
    key: UUID = ApiField(alias='key')
    username: str = ApiField(alias='username')


class ApiKeyRequest(ObjectModel):
    apiVersion: Literal['ALL', 'V1'] = ApiField(alias='apiVersion')
    validityDays: int = ApiField(alias='validityDays')


class ApiKeyResponse(ObjectModel):
    apiKeys: List[ApiKeyInformation] = ApiField(alias='apiKeys', default_factory=list)


class CUser(ObjectModel):
    pk: CUserPk = ApiField(alias='pk')
    id: UUID = ApiField(alias='id')
    companyId: UUID = ApiField(alias='companyId')
    firstname: str = ApiField(alias='firstname')
    lastname: str = ApiField(alias='lastname')
    passwordHash: str = ApiField(alias='passwordHash')
    userType: Literal['EXTERNAL', 'INTERNAL'] = ApiField(alias='userType')
    userAccountType: Literal['API', 'WEB_UI'] = ApiField(alias='userAccountType')
    userStatus: Literal['ACTIVE', 'INACTIVE', 'PENDING_ACTIVATION'] = ApiField(alias='userStatus')
    ssoStatus: Literal['ACTIVE', 'INACTIVE'] = ApiField(alias='ssoStatus')
    activationKey: UUID = ApiField(alias='activationKey')
    firstLoginDate: datetime = ApiField(alias='firstLoginDate')
    failedLoginCount: int = ApiField(alias='failedLoginCount')
    eulaAcceptDate: datetime = ApiField(alias='eulaAcceptDate')
    activationEmailDelayedSendDate: datetime = ApiField(alias='activationEmailDelayedSendDate')
    creationDate: datetime = ApiField(alias='creationDate')
    dataEncryptionKeyId: UUID = ApiField(alias='dataEncryptionKeyId')
    systemRoles: List[Literal['CONDOR_METRICS', 'SYSTEM_ADMIN']] = ApiField(alias='systemRoles', default_factory=list)
    requestedEntitlements: List[Literal['ANY', 'DEVOPS', 'MIRA', 'OUTAGE_DETECTION']
                                ] = ApiField(alias='requestedEntitlements', default_factory=list)
    localLoginDisabled: bool = ApiField(alias='localLoginDisabled')
    activationEmailSendDate: datetime = ApiField(alias='activationEmailSendDate')
    marketoAttributes: Dict[str, str] = ApiField(alias='marketoAttributes', default_factory=dict)
    ownedTeams: List[UUID] = ApiField(alias='ownedTeams', default_factory=list)
    memberedTeams: List[UUID] = ApiField(alias='memberedTeams', default_factory=list)
    productRoles: Dict[str, List[Literal['DEVOPS_LEAD', 'DEVOPS_USER', 'GUEST', 'OUTAGEDETECTION_ADMIN',
                                         'PKI_ADMIN', 'RESOURCE_OWNER', 'SECURITY_ADMIN']]] = ApiField(alias='productRoles', default_factory=dict)
    emailAddress: str = ApiField(alias='emailAddress')
    userFullName: str = ApiField(alias='userFullName')
    dataEncryptionKeyContainerId: UUID = ApiField(alias='dataEncryptionKeyContainerId')
    encryptorDecryptors: List[EncryptorDecryptor] = ApiField(alias='encryptorDecryptors', default_factory=list)


class CUserPk(ObjectModel):
    encryptedUsername: str = ApiField(alias='encryptedUsername')
    username: str = ApiField(alias='username')


class CapabilityInformation(ObjectModel):
    name: Literal['DEFAULT', 'DISTRIBUTED_ISSUER', 'ENTERPRISE', 'ISSUANCE',
                  'PROVISIONING', 'SINGLE_SIGN_ON', 'VALIDATION'] = ApiField(alias='name')
    productExpiryDate: datetime = ApiField(alias='productExpiryDate')
    isTrial: bool = ApiField(alias='isTrial')


class ChangePasswordRequest(ObjectModel):
    currentPassword: str = ApiField(alias='currentPassword')
    newPassword: str = ApiField(alias='newPassword')


class CompanyInformation(ObjectModel):
    id: UUID = ApiField(alias='id')
    name: str = ApiField(alias='name')
    companyType: Literal['CA', 'INTERNAL', 'OTHER', 'REGULAR', 'TPP_CUSTOMER'] = ApiField(alias='companyType')
    active: bool = ApiField(alias='active')
    creationDate: datetime = ApiField(alias='creationDate')
    domains: List[str] = ApiField(alias='domains', default_factory=list)
    referralPartner: Literal['digicert-certcentral', 'globalsign-hvca'] = ApiField(alias='referralPartner')
    productEntitlements: List[ProductEntitlementInformation] = ApiField(alias='productEntitlements', default_factory=list)


class CreateTeamRequest(ObjectModel):
    name: str = ApiField(alias='name')
    role: Literal['GUEST', 'PKI_ADMIN', 'RESOURCE_OWNER', 'SYSTEM_ADMIN'] = ApiField(alias='role')
    members: List[UUID] = ApiField(alias='members', default_factory=list)
    owners: List[UUID] = ApiField(alias='owners', default_factory=list)
    userMatchingRules: List[UserMatchingRule] = ApiField(alias='userMatchingRules', default_factory=list)


class DataEncryptionKeyInformation(ObjectModel):
    id: UUID = ApiField(alias='id')
    companyId: UUID = ApiField(alias='companyId')
    algorithm: str = ApiField(alias='algorithm')
    active: bool = ApiField(alias='active')


class EncryptorDecryptor(ObjectModel):
    pass


class ErrorInformation(ObjectModel):
    code: int = ApiField(alias='code')
    message: str = ApiField(alias='message')
    args: List[Dict[str, Any]] = ApiField(alias='args', default_factory=list)


class ErrorResponse(ObjectModel):
    errors: List[ErrorInformation] = ApiField(alias='errors', default_factory=list)


class InvitationConfirmationRequest(ObjectModel):
    invitationId: UUID = ApiField(alias='invitationId')
    username: str = ApiField(alias='username')
    password: str = ApiField(alias='password')
    firstname: str = ApiField(alias='firstname')
    lastname: str = ApiField(alias='lastname')
    grecaptchaResponse: str = ApiField(alias='grecaptchaResponse')


class InvitationInformation(ObjectModel):
    id: UUID = ApiField(alias='id')
    productRoles: Dict[str, List[Literal['DEVOPS_LEAD', 'DEVOPS_USER', 'GUEST', 'OUTAGEDETECTION_ADMIN',
                                         'PKI_ADMIN', 'RESOURCE_OWNER', 'SECURITY_ADMIN']]] = ApiField(alias='productRoles', default_factory=dict)
    properties: Dict[str, str] = ApiField(alias='properties', default_factory=dict)


class InvitationRequest(ObjectModel):
    roles: Dict[str, Literal['DEVOPS_LEAD', 'DEVOPS_USER', 'GUEST', 'OUTAGEDETECTION_ADMIN',
                             'PKI_ADMIN', 'RESOURCE_OWNER', 'SECURITY_ADMIN']] = ApiField(alias='roles', default_factory=dict)
    teams: List[UUID] = ApiField(alias='teams', default_factory=list)
    properties: Dict[str, str] = ApiField(alias='properties', default_factory=dict)


class InvitationResponse(ObjectModel):
    invitations: List[InvitationInformation] = ApiField(alias='invitations', default_factory=list)


class LocalLoginRequest(ObjectModel):
    localLoginDisabled: bool = ApiField(alias='localLoginDisabled')


class NotificationConfigurationInformation(ObjectModel):
    id: UUID = ApiField(alias='id')
    type: Literal['APPLICATION_CERTIFICATE_EXPIRATION', 'CERTIFICATE_EXPIRATION', 'CERTIFICATE_STATUS_DIGEST'] = ApiField(alias='type')
    recurrencePattern: RecurrencePatternInformation = ApiField(alias='recurrencePattern')
    recipients: List[str] = ApiField(alias='recipients', default_factory=list)


class NotificationConfigurationRequest(ObjectModel):
    type: Literal['APPLICATION_CERTIFICATE_EXPIRATION', 'CERTIFICATE_EXPIRATION', 'CERTIFICATE_STATUS_DIGEST'] = ApiField(alias='type')
    recurrencePattern: RecurrencePatternInformation = ApiField(alias='recurrencePattern')
    recipients: List[str] = ApiField(alias='recipients', default_factory=list)


class NotificationConfigurationResponse(ObjectModel):
    configurations: List[NotificationConfigurationInformation] = ApiField(alias='configurations', default_factory=list)


class ProductEntitlementInformation(ObjectModel):
    label: Literal['ANY', 'DEVOPS', 'MIRA', 'OUTAGE_DETECTION'] = ApiField(alias='label')
    capabilities: List[CapabilityInformation] = ApiField(alias='capabilities', default_factory=list)
    visibilityConstraintsInformation: VisibilityConstraintsInformation = ApiField(alias='visibilityConstraintsInformation')


class RecurrencePatternInformation(ObjectModel):
    recurrenceType: Literal['DAY_OF_WEEK'] = ApiField(alias='recurrenceType')
    recurrenceValues: List[Literal['FRIDAY', 'MONDAY', 'SATURDAY', 'SUNDAY', 'THURSDAY',
                                   'TUESDAY', 'WEDNESDAY']] = ApiField(alias='recurrenceValues', default_factory=list)


class ResendActivationRequest(ObjectModel):
    email: str = ApiField(alias='email')


class ResendActivationResponse(ObjectModel):
    user: UserInformation = ApiField(alias='user')


class ResetPasswordRequest(ObjectModel):
    email: str = ApiField(alias='email')


class ResetPasswordResponse(ObjectModel):
    message: str = ApiField(alias='message')


class RolesRequest(ObjectModel):
    systemAdmin: bool = ApiField(alias='systemAdmin')
    roles: Dict[str, Literal['DEVOPS_LEAD', 'DEVOPS_USER', 'GUEST', 'OUTAGEDETECTION_ADMIN',
                             'PKI_ADMIN', 'RESOURCE_OWNER', 'SECURITY_ADMIN']] = ApiField(alias='roles', default_factory=dict)


class SsoConfigurationInformation(ObjectModel):
    clientId: str = ApiField(alias='clientId')
    clientSecret: str = ApiField(alias='clientSecret')
    issuerUrl: str = ApiField(alias='issuerUrl')
    scopes: List[str] = ApiField(alias='scopes', default_factory=list)
    id: UUID = ApiField(alias='id')
    companyId: UUID = ApiField(alias='companyId')


class SsoConfigurationRequest(ObjectModel):
    clientId: str = ApiField(alias='clientId')
    clientSecret: str = ApiField(alias='clientSecret')
    issuerUrl: str = ApiField(alias='issuerUrl')
    scopes: List[str] = ApiField(alias='scopes', default_factory=list)


class SsoConfigurationResponse(ObjectModel):
    ssoConfigurations: List[SsoConfigurationInformation] = ApiField(alias='ssoConfigurations', default_factory=list)


class TeamInformation(ObjectModel):
    id: UUID = ApiField(alias='id')
    name: str = ApiField(alias='name')
    systemRoles: List[Literal['CONDOR_METRICS', 'SYSTEM_ADMIN']] = ApiField(alias='systemRoles', default_factory=list)
    productRoles: Dict[str, List[Literal['DEVOPS_LEAD', 'DEVOPS_USER', 'GUEST', 'OUTAGEDETECTION_ADMIN',
                                         'PKI_ADMIN', 'RESOURCE_OWNER', 'SECURITY_ADMIN']]] = ApiField(alias='productRoles', default_factory=dict)
    role: Literal['GUEST', 'PKI_ADMIN', 'RESOURCE_OWNER', 'SYSTEM_ADMIN'] = ApiField(alias='role')
    members: List[UUID] = ApiField(alias='members', default_factory=list)
    owners: List[UUID] = ApiField(alias='owners', default_factory=list)
    companyId: UUID = ApiField(alias='companyId')
    userMatchingRules: List[UserMatchingRule] = ApiField(alias='userMatchingRules', default_factory=list)
    modificationDate: datetime = ApiField(alias='modificationDate')


class TeamMembersRequest(ObjectModel):
    members: List[UUID] = ApiField(alias='members', default_factory=list)


class TeamOwnersRequest(ObjectModel):
    owners: List[UUID] = ApiField(alias='owners', default_factory=list)


class TeamsResponse(ObjectModel):
    teams: List[TeamInformation] = ApiField(alias='teams', default_factory=list)


class UnsubscribeNotificationInformation(ObjectModel):
    message: str = ApiField(alias='message')


class UpdatePasswordRequest(ObjectModel):
    newPassword: str = ApiField(alias='newPassword')
    token: str = ApiField(alias='token')


class UpdatePasswordResponse(ObjectModel):
    message: str = ApiField(alias='message')


class UpdateTeamRequest(ObjectModel):
    name: str = ApiField(alias='name')
    role: Literal['GUEST', 'PKI_ADMIN', 'RESOURCE_OWNER', 'SYSTEM_ADMIN'] = ApiField(alias='role')
    userMatchingRules: List[UserMatchingRule] = ApiField(alias='userMatchingRules', default_factory=list)


class UserAccountRequest(ObjectModel):
    userAccountType: Literal['API', 'WEB_UI'] = ApiField(alias='userAccountType')
    username: str = ApiField(alias='username')
    password: str = ApiField(alias='password')
    firstname: str = ApiField(alias='firstname')
    lastname: str = ApiField(alias='lastname')
    companyId: UUID = ApiField(alias='companyId')
    companyName: str = ApiField(alias='companyName')
    referralPartner: Literal['digicert-certcentral', 'globalsign-hvca'] = ApiField(alias='referralPartner')
    productEntitlements: List[Literal['ANY', 'DEVOPS', 'MIRA', 'OUTAGE_DETECTION']] = ApiField(alias='productEntitlements', default_factory=list)
    marketoAttributes: Dict[str, str] = ApiField(alias='marketoAttributes', default_factory=dict)
    grecaptchaResponse: str = ApiField(alias='grecaptchaResponse')


class UserAccountResponse(ObjectModel):
    user: UserInformation = ApiField(alias='user')
    company: CompanyInformation = ApiField(alias='company')
    apiKey: ApiKeyInformation = ApiField(alias='apiKey')


class UserAccountTypeRequest(ObjectModel):
    accountType: Literal['API', 'WEB_UI'] = ApiField(alias='accountType')


class UserInformation(ObjectModel):
    username: str = ApiField(alias='username')
    id: UUID = ApiField(alias='id')
    companyId: UUID = ApiField(alias='companyId')
    firstname: str = ApiField(alias='firstname')
    lastname: str = ApiField(alias='lastname')
    emailAddress: str = ApiField(alias='emailAddress')
    userType: Literal['EXTERNAL', 'INTERNAL'] = ApiField(alias='userType')
    userAccountType: Literal['API', 'WEB_UI'] = ApiField(alias='userAccountType')
    ssoStatus: Literal['ACTIVE', 'INACTIVE'] = ApiField(alias='ssoStatus')
    userStatus: Literal['ACTIVE', 'INACTIVE', 'PENDING_ACTIVATION'] = ApiField(alias='userStatus')
    systemRoles: List[Literal['CONDOR_METRICS', 'SYSTEM_ADMIN']] = ApiField(alias='systemRoles', default_factory=list)
    productRoles: Dict[str, List[Literal['DEVOPS_LEAD', 'DEVOPS_USER', 'GUEST', 'OUTAGEDETECTION_ADMIN',
                                         'PKI_ADMIN', 'RESOURCE_OWNER', 'SECURITY_ADMIN']]] = ApiField(alias='productRoles', default_factory=dict)
    localLoginDisabled: bool = ApiField(alias='localLoginDisabled')
    hasPassword: bool = ApiField(alias='hasPassword')
    firstLoginDate: datetime = ApiField(alias='firstLoginDate')
    creationDate: datetime = ApiField(alias='creationDate')
    ownedTeams: List[UUID] = ApiField(alias='ownedTeams', default_factory=list)
    memberedTeams: List[UUID] = ApiField(alias='memberedTeams', default_factory=list)


class UserMatchingRule(ObjectModel):
    claimName: str = ApiField(alias='claimName')
    operator: Literal['CONTAINS', 'ENDS_WITH', 'EQUALS', 'NOT_CONTAINS', 'NOT_EQUALS', 'STARTS_WITH'] = ApiField(alias='operator')
    value: str = ApiField(alias='value')


class UserPreferenceInformation(ObjectModel):
    id: UUID = ApiField(alias='id')
    name: Literal['DASHBOARD_PERSONA', 'DEFAULT_PAGE_VIEW_APPLICATIONS', 'DEFAULT_PAGE_VIEW_CA_ACCOUNTS', 'DEFAULT_PAGE_VIEW_OD_CERTIFICATES', 'DEFAULT_PAGE_VIEW_ORGANIZATIONAL_UNITS', 'DEFAULT_PAGE_VIEW_TEAMS', 'DEFAULT_PAGE_VIEW_USERS', 'NEWS_BANNER_SHOW',
                  'PREFERENCE_1', 'PREFERENCE_2', 'PREFERENCE_3', 'PREFERENCE_4', 'PREFERENCE_5', 'PREFERENCE_6', 'PREFERENCE_7', 'RECENTLY_FOUND_CERTIFICATES_INTERVAL', 'SAVED_QUERIES_ACTIVITY_LOGGING', 'SELECTED_USER_ENTITLEMENT'] = ApiField(alias='name')
    value: Dict[str, Any] = ApiField(alias='value', default_factory=dict)


class UserPreferenceRequest(ObjectModel):
    name: Literal['DASHBOARD_PERSONA', 'DEFAULT_PAGE_VIEW_APPLICATIONS', 'DEFAULT_PAGE_VIEW_CA_ACCOUNTS', 'DEFAULT_PAGE_VIEW_OD_CERTIFICATES', 'DEFAULT_PAGE_VIEW_ORGANIZATIONAL_UNITS', 'DEFAULT_PAGE_VIEW_TEAMS', 'DEFAULT_PAGE_VIEW_USERS', 'NEWS_BANNER_SHOW',
                  'PREFERENCE_1', 'PREFERENCE_2', 'PREFERENCE_3', 'PREFERENCE_4', 'PREFERENCE_5', 'PREFERENCE_6', 'PREFERENCE_7', 'RECENTLY_FOUND_CERTIFICATES_INTERVAL', 'SAVED_QUERIES_ACTIVITY_LOGGING', 'SELECTED_USER_ENTITLEMENT'] = ApiField(alias='name')
    value: Dict[str, Any] = ApiField(alias='value', default_factory=dict)


class UserPreferencesResponse(ObjectModel):
    preferences: List[UserPreferenceInformation] = ApiField(alias='preferences', default_factory=list)


class UserResponse(ObjectModel):
    users: List[UserInformation] = ApiField(alias='users', default_factory=list)


class VisibilityConstraintsInformation(ObjectModel):
    fullAccessDurationDays: int = ApiField(alias='fullAccessDurationDays')
    limitedVisibilityCertCount: int = ApiField(alias='limitedVisibilityCertCount')
    limitedVisibilityCertInstallPerCertCount: int = ApiField(alias='limitedVisibilityCertInstallPerCertCount')
    limitedAccessNotificationDays: int = ApiField(alias='limitedAccessNotificationDays')


ApiKeyInformation.update_forward_refs()
ApiKeyNullResponse.update_forward_refs()
ApiKeyRequest.update_forward_refs()
ApiKeyResponse.update_forward_refs()
CUser.update_forward_refs()
CUserPk.update_forward_refs()
CapabilityInformation.update_forward_refs()
ChangePasswordRequest.update_forward_refs()
CompanyInformation.update_forward_refs()
CreateTeamRequest.update_forward_refs()
DataEncryptionKeyInformation.update_forward_refs()
EncryptorDecryptor.update_forward_refs()
ErrorInformation.update_forward_refs()
ErrorResponse.update_forward_refs()
InvitationConfirmationRequest.update_forward_refs()
InvitationInformation.update_forward_refs()
InvitationRequest.update_forward_refs()
InvitationResponse.update_forward_refs()
LocalLoginRequest.update_forward_refs()
NotificationConfigurationInformation.update_forward_refs()
NotificationConfigurationRequest.update_forward_refs()
NotificationConfigurationResponse.update_forward_refs()
ProductEntitlementInformation.update_forward_refs()
RecurrencePatternInformation.update_forward_refs()
ResendActivationRequest.update_forward_refs()
ResendActivationResponse.update_forward_refs()
ResetPasswordRequest.update_forward_refs()
ResetPasswordResponse.update_forward_refs()
RolesRequest.update_forward_refs()
SsoConfigurationInformation.update_forward_refs()
SsoConfigurationRequest.update_forward_refs()
SsoConfigurationResponse.update_forward_refs()
TeamInformation.update_forward_refs()
TeamMembersRequest.update_forward_refs()
TeamOwnersRequest.update_forward_refs()
TeamsResponse.update_forward_refs()
UnsubscribeNotificationInformation.update_forward_refs()
UpdatePasswordRequest.update_forward_refs()
UpdatePasswordResponse.update_forward_refs()
UpdateTeamRequest.update_forward_refs()
UserAccountRequest.update_forward_refs()
UserAccountResponse.update_forward_refs()
UserAccountTypeRequest.update_forward_refs()
UserInformation.update_forward_refs()
UserMatchingRule.update_forward_refs()
UserPreferenceInformation.update_forward_refs()
UserPreferenceRequest.update_forward_refs()
UserPreferencesResponse.update_forward_refs()
UserResponse.update_forward_refs()
VisibilityConstraintsInformation.update_forward_refs()
