from __future__ import annotations
from pyvenafi.cloud.api.api_base import ApiField, ObjectModel
from datetime import datetime
from typing import (Any, Dict, List, Literal)
from uuid import UUID


class ApiKeyInformation(ObjectModel):
    apiKeyStatus: Literal['ACTIVE', 'EXPIRED', 'INACTIVE', 'PENDING_ACTIVATION', 'PENDING_ROTATION', 'ROTATED'] = ApiField(alias='apiKeyStatus')
    apiVersion: Literal['ALL', 'V1'] = ApiField(alias='apiVersion')
    companyId: UUID = ApiField(alias='companyId')
    creationDate: datetime = ApiField(alias='creationDate')
    key: UUID = ApiField(alias='key')
    userId: UUID = ApiField(alias='userId')
    username: str = ApiField(alias='username')
    validityEndDate: datetime = ApiField(alias='validityEndDate')
    validityStartDate: datetime = ApiField(alias='validityStartDate')


class ApiKeyNullResponse(ObjectModel):
    key: UUID = ApiField(alias='key')
    username: str = ApiField(alias='username')


class ApiKeyRequest(ObjectModel):
    apiVersion: Literal['ALL', 'V1'] = ApiField(alias='apiVersion')
    validityDays: int = ApiField(alias='validityDays')


class ApiKeyResponse(ObjectModel):
    apiKeys: List[ApiKeyInformation] = ApiField(alias='apiKeys', default_factory=list)


class CUser(ObjectModel):
    activationEmailDelayedSendDate: datetime = ApiField(alias='activationEmailDelayedSendDate')
    activationEmailSendDate: datetime = ApiField(alias='activationEmailSendDate')
    activationKey: UUID = ApiField(alias='activationKey')
    companyId: UUID = ApiField(alias='companyId')
    creationDate: datetime = ApiField(alias='creationDate')
    dataEncryptionKeyContainerId: UUID = ApiField(alias='dataEncryptionKeyContainerId')
    dataEncryptionKeyId: UUID = ApiField(alias='dataEncryptionKeyId')
    emailAddress: str = ApiField(alias='emailAddress')
    encryptorDecryptors: List[EncryptorDecryptor] = ApiField(alias='encryptorDecryptors', default_factory=list)
    eulaAcceptDate: datetime = ApiField(alias='eulaAcceptDate')
    failedLoginCount: int = ApiField(alias='failedLoginCount')
    firstLoginDate: datetime = ApiField(alias='firstLoginDate')
    firstname: str = ApiField(alias='firstname')
    id: UUID = ApiField(alias='id')
    lastname: str = ApiField(alias='lastname')
    localLoginDisabled: bool = ApiField(alias='localLoginDisabled')
    marketoAttributes: Dict[str, str] = ApiField(alias='marketoAttributes', default_factory=dict)
    memberedTeams: List[UUID] = ApiField(alias='memberedTeams', default_factory=list)
    ownedTeams: List[UUID] = ApiField(alias='ownedTeams', default_factory=list)
    passwordHash: str = ApiField(alias='passwordHash')
    pk: CUserPk = ApiField(alias='pk')
    productRoles: Dict[str, List[Literal['DEVOPS_LEAD', 'DEVOPS_USER', 'GUEST', 'OUTAGEDETECTION_ADMIN',
                                         'PKI_ADMIN', 'RESOURCE_OWNER', 'SECURITY_ADMIN']]] = ApiField(alias='productRoles', default_factory=dict)
    requestedEntitlements: List[Literal['ANY', 'DEVOPS', 'MIRA', 'OUTAGE_DETECTION']
                                ] = ApiField(alias='requestedEntitlements', default_factory=list)
    ssoStatus: Literal['ACTIVE', 'INACTIVE'] = ApiField(alias='ssoStatus')
    systemRoles: List[Literal['CONDOR_METRICS', 'SYSTEM_ADMIN']] = ApiField(alias='systemRoles', default_factory=list)
    userAccountType: Literal['API', 'WEB_UI'] = ApiField(alias='userAccountType')
    userFullName: str = ApiField(alias='userFullName')
    userStatus: Literal['ACTIVE', 'INACTIVE', 'PENDING_ACTIVATION'] = ApiField(alias='userStatus')
    userType: Literal['EXTERNAL', 'INTERNAL'] = ApiField(alias='userType')


class CUserPk(ObjectModel):
    encryptedUsername: str = ApiField(alias='encryptedUsername')
    username: str = ApiField(alias='username')


class CapabilityInformation(ObjectModel):
    isTrial: bool = ApiField(alias='isTrial')
    name: Literal['DEFAULT', 'DISTRIBUTED_ISSUER', 'ENTERPRISE', 'ISSUANCE',
                  'PROVISIONING', 'SINGLE_SIGN_ON', 'VALIDATION'] = ApiField(alias='name')
    productExpiryDate: datetime = ApiField(alias='productExpiryDate')


class ChangePasswordRequest(ObjectModel):
    currentPassword: str = ApiField(alias='currentPassword')
    newPassword: str = ApiField(alias='newPassword')


class CompanyInformation(ObjectModel):
    active: bool = ApiField(alias='active')
    companyType: Literal['CA', 'INTERNAL', 'OTHER', 'REGULAR', 'TPP_CUSTOMER'] = ApiField(alias='companyType')
    creationDate: datetime = ApiField(alias='creationDate')
    domains: List[str] = ApiField(alias='domains', default_factory=list)
    id: UUID = ApiField(alias='id')
    name: str = ApiField(alias='name')
    productEntitlements: List[ProductEntitlementInformation] = ApiField(alias='productEntitlements', default_factory=list)
    referralPartner: Literal['digicert-certcentral', 'globalsign-hvca'] = ApiField(alias='referralPartner')


class CreateTeamRequest(ObjectModel):
    members: List[UUID] = ApiField(alias='members', default_factory=list)
    name: str = ApiField(alias='name')
    owners: List[UUID] = ApiField(alias='owners', default_factory=list)
    role: Literal['GUEST', 'PKI_ADMIN', 'RESOURCE_OWNER', 'SYSTEM_ADMIN'] = ApiField(alias='role')
    userMatchingRules: List[UserMatchingRule] = ApiField(alias='userMatchingRules', default_factory=list)


class DataEncryptionKeyInformation(ObjectModel):
    active: bool = ApiField(alias='active')
    algorithm: str = ApiField(alias='algorithm')
    companyId: UUID = ApiField(alias='companyId')
    id: UUID = ApiField(alias='id')


class EncryptorDecryptor(ObjectModel):
    pass


class ErrorInformation(ObjectModel):
    args: List[Dict[str, Any]] = ApiField(alias='args', default_factory=list)
    code: int = ApiField(alias='code')
    message: str = ApiField(alias='message')


class ErrorResponse(ObjectModel):
    errors: List[ErrorInformation] = ApiField(alias='errors', default_factory=list)


class InvitationConfirmationRequest(ObjectModel):
    firstname: str = ApiField(alias='firstname')
    grecaptchaResponse: str = ApiField(alias='grecaptchaResponse')
    invitationId: UUID = ApiField(alias='invitationId')
    lastname: str = ApiField(alias='lastname')
    password: str = ApiField(alias='password')
    username: str = ApiField(alias='username')


class InvitationInformation(ObjectModel):
    id: UUID = ApiField(alias='id')
    productRoles: Dict[str, List[Literal['DEVOPS_LEAD', 'DEVOPS_USER', 'GUEST', 'OUTAGEDETECTION_ADMIN',
                                         'PKI_ADMIN', 'RESOURCE_OWNER', 'SECURITY_ADMIN']]] = ApiField(alias='productRoles', default_factory=dict)
    properties: Dict[str, str] = ApiField(alias='properties', default_factory=dict)


class InvitationRequest(ObjectModel):
    properties: Dict[str, str] = ApiField(alias='properties', default_factory=dict)
    roles: Dict[str, Literal['DEVOPS_LEAD', 'DEVOPS_USER', 'GUEST', 'OUTAGEDETECTION_ADMIN',
                             'PKI_ADMIN', 'RESOURCE_OWNER', 'SECURITY_ADMIN']] = ApiField(alias='roles', default_factory=dict)
    teams: List[UUID] = ApiField(alias='teams', default_factory=list)


class InvitationResponse(ObjectModel):
    invitations: List[InvitationInformation] = ApiField(alias='invitations', default_factory=list)


class LocalLoginRequest(ObjectModel):
    localLoginDisabled: bool = ApiField(alias='localLoginDisabled')


class NotificationConfigurationInformation(ObjectModel):
    id: UUID = ApiField(alias='id')
    recipients: List[str] = ApiField(alias='recipients', default_factory=list)
    recurrencePattern: RecurrencePatternInformation = ApiField(alias='recurrencePattern')
    type: Literal['APPLICATION_CERTIFICATE_EXPIRATION', 'CERTIFICATE_EXPIRATION', 'CERTIFICATE_STATUS_DIGEST'] = ApiField(alias='type')


class NotificationConfigurationRequest(ObjectModel):
    recipients: List[str] = ApiField(alias='recipients', default_factory=list)
    recurrencePattern: RecurrencePatternInformation = ApiField(alias='recurrencePattern')
    type: Literal['APPLICATION_CERTIFICATE_EXPIRATION', 'CERTIFICATE_EXPIRATION', 'CERTIFICATE_STATUS_DIGEST'] = ApiField(alias='type')


class NotificationConfigurationResponse(ObjectModel):
    configurations: List[NotificationConfigurationInformation] = ApiField(alias='configurations', default_factory=list)


class ProductEntitlementInformation(ObjectModel):
    capabilities: List[CapabilityInformation] = ApiField(alias='capabilities', default_factory=list)
    label: Literal['ANY', 'DEVOPS', 'MIRA', 'OUTAGE_DETECTION'] = ApiField(alias='label')
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
    roles: Dict[str, Literal['DEVOPS_LEAD', 'DEVOPS_USER', 'GUEST', 'OUTAGEDETECTION_ADMIN',
                             'PKI_ADMIN', 'RESOURCE_OWNER', 'SECURITY_ADMIN']] = ApiField(alias='roles', default_factory=dict)
    systemAdmin: bool = ApiField(alias='systemAdmin')


class SsoConfigurationInformation(ObjectModel):
    clientId: str = ApiField(alias='clientId')
    clientSecret: str = ApiField(alias='clientSecret')
    companyId: UUID = ApiField(alias='companyId')
    id: UUID = ApiField(alias='id')
    issuerUrl: str = ApiField(alias='issuerUrl')
    scopes: List[str] = ApiField(alias='scopes', default_factory=list)


class SsoConfigurationRequest(ObjectModel):
    clientId: str = ApiField(alias='clientId')
    clientSecret: str = ApiField(alias='clientSecret')
    issuerUrl: str = ApiField(alias='issuerUrl')
    scopes: List[str] = ApiField(alias='scopes', default_factory=list)


class SsoConfigurationResponse(ObjectModel):
    ssoConfigurations: List[SsoConfigurationInformation] = ApiField(alias='ssoConfigurations', default_factory=list)


class TeamInformation(ObjectModel):
    companyId: UUID = ApiField(alias='companyId')
    id: UUID = ApiField(alias='id')
    members: List[UUID] = ApiField(alias='members', default_factory=list)
    modificationDate: datetime = ApiField(alias='modificationDate')
    name: str = ApiField(alias='name')
    owners: List[UUID] = ApiField(alias='owners', default_factory=list)
    productRoles: Dict[str, List[Literal['DEVOPS_LEAD', 'DEVOPS_USER', 'GUEST', 'OUTAGEDETECTION_ADMIN',
                                         'PKI_ADMIN', 'RESOURCE_OWNER', 'SECURITY_ADMIN']]] = ApiField(alias='productRoles', default_factory=dict)
    role: Literal['GUEST', 'PKI_ADMIN', 'RESOURCE_OWNER', 'SYSTEM_ADMIN'] = ApiField(alias='role')
    systemRoles: List[Literal['CONDOR_METRICS', 'SYSTEM_ADMIN']] = ApiField(alias='systemRoles', default_factory=list)
    userMatchingRules: List[UserMatchingRule] = ApiField(alias='userMatchingRules', default_factory=list)


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
    companyId: UUID = ApiField(alias='companyId')
    companyName: str = ApiField(alias='companyName')
    firstname: str = ApiField(alias='firstname')
    grecaptchaResponse: str = ApiField(alias='grecaptchaResponse')
    lastname: str = ApiField(alias='lastname')
    marketoAttributes: Dict[str, str] = ApiField(alias='marketoAttributes', default_factory=dict)
    password: str = ApiField(alias='password')
    productEntitlements: List[Literal['ANY', 'DEVOPS', 'MIRA', 'OUTAGE_DETECTION']] = ApiField(alias='productEntitlements', default_factory=list)
    referralPartner: Literal['digicert-certcentral', 'globalsign-hvca'] = ApiField(alias='referralPartner')
    userAccountType: Literal['API', 'WEB_UI'] = ApiField(alias='userAccountType')
    username: str = ApiField(alias='username')


class UserAccountResponse(ObjectModel):
    apiKey: ApiKeyInformation = ApiField(alias='apiKey')
    company: CompanyInformation = ApiField(alias='company')
    user: UserInformation = ApiField(alias='user')


class UserAccountTypeRequest(ObjectModel):
    accountType: Literal['API', 'WEB_UI'] = ApiField(alias='accountType')


class UserInformation(ObjectModel):
    companyId: UUID = ApiField(alias='companyId')
    creationDate: datetime = ApiField(alias='creationDate')
    emailAddress: str = ApiField(alias='emailAddress')
    firstLoginDate: datetime = ApiField(alias='firstLoginDate')
    firstname: str = ApiField(alias='firstname')
    hasPassword: bool = ApiField(alias='hasPassword')
    id: UUID = ApiField(alias='id')
    lastname: str = ApiField(alias='lastname')
    localLoginDisabled: bool = ApiField(alias='localLoginDisabled')
    memberedTeams: List[UUID] = ApiField(alias='memberedTeams', default_factory=list)
    ownedTeams: List[UUID] = ApiField(alias='ownedTeams', default_factory=list)
    productRoles: Dict[str, List[Literal['DEVOPS_LEAD', 'DEVOPS_USER', 'GUEST', 'OUTAGEDETECTION_ADMIN',
                                         'PKI_ADMIN', 'RESOURCE_OWNER', 'SECURITY_ADMIN']]] = ApiField(alias='productRoles', default_factory=dict)
    ssoStatus: Literal['ACTIVE', 'INACTIVE'] = ApiField(alias='ssoStatus')
    systemRoles: List[Literal['CONDOR_METRICS', 'SYSTEM_ADMIN']] = ApiField(alias='systemRoles', default_factory=list)
    userAccountType: Literal['API', 'WEB_UI'] = ApiField(alias='userAccountType')
    userStatus: Literal['ACTIVE', 'INACTIVE', 'PENDING_ACTIVATION'] = ApiField(alias='userStatus')
    userType: Literal['EXTERNAL', 'INTERNAL'] = ApiField(alias='userType')
    username: str = ApiField(alias='username')


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
    limitedAccessNotificationDays: int = ApiField(alias='limitedAccessNotificationDays')
    limitedVisibilityCertCount: int = ApiField(alias='limitedVisibilityCertCount')
    limitedVisibilityCertInstallPerCertCount: int = ApiField(alias='limitedVisibilityCertInstallPerCertCount')


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
