from __future__ import annotations
from pyvenafi.cloud.api.api_base import (
    ApiField,
    ObjectModel,
)
from datetime import datetime
from typing import (
    Any,
    Dict,
    List,
    Literal,
)
from uuid import UUID

AnyValue = Any
ApiKeyStatus = Literal[
    "PENDING_ACTIVATION",
    "ACTIVE",
    "INACTIVE",
    "PENDING_ROTATION",
    "ROTATED",
    "EXPIRED"
]
ApiVersion = Literal[
    "ALL",
    "V1"
]
Capability = Literal[
    "DEFAULT",
    "ISSUANCE",
    "VALIDATION",
    "ENTERPRISE",
    "PROVISIONING",
    "SINGLE_SIGN_ON",
    "DISTRIBUTED_ISSUER",
    "CLOUD_PROVIDERS",
    "CREDENTIAL_MANAGER",
    "KUBERNETES_DISCOVERY",
    "KUBERNETES_ENTERPRISE_COMPONENTS",
    "KUBERNETES_ENTERPRISE_COMPONENTS_CERT_MANAGER",
    "KUBERNETES_ENTERPRISE_COMPONENTS_VEI",
    "KUBERNETES_ENTERPRISE_COMPONENTS_APE",
    "KUBERNETES_INTEGRATION_TLSPDC"
]
CompanyType = Literal[
    "INTERNAL",
    "CA",
    "TPP_CUSTOMER",
    "REGULAR",
    "OTHER"
]
DayOfWeek = Literal[
    "MONDAY",
    "TUESDAY",
    "WEDNESDAY",
    "THURSDAY",
    "FRIDAY",
    "SATURDAY",
    "SUNDAY"
]
NotificationType = Literal[
    "CERTIFICATE_EXPIRATION",
    "APPLICATION_CERTIFICATE_EXPIRATION",
    "CERTIFICATE_STATUS_DIGEST"
]
Operator = Literal[
    "EQUALS",
    "NOT_EQUALS",
    "CONTAINS",
    "NOT_CONTAINS",
    "STARTS_WITH",
    "ENDS_WITH"
]
ProductEntitlement = Literal[
    "ANY",
    "MIRA",
    "DEVOPS",
    "OUTAGE_DETECTION",
    "CODESIGN"
]
RecurrenceType = Literal['DAY_OF_WEEK']
ReferralPartner = Literal[
    "globalsign-hvca",
    "digicert-certcentral"
]
Role = Literal[
    "SECURITY_ADMIN",
    "DEVOPS_LEAD",
    "DEVOPS_USER",
    "OUTAGEDETECTION_ADMIN",
    "RESOURCE_OWNER",
    "PKI_ADMIN",
    "GUEST",
    "PLATFORM_ADMIN"
]
SSOStatus = Literal[
    "ACTIVE",
    "INACTIVE"
]
SystemRole = Literal[
    "SYSTEM_ADMIN",
    "CONDOR_METRICS"
]
TeamRole = Literal[
    "SYSTEM_ADMIN",
    "PKI_ADMIN",
    "RESOURCE_OWNER",
    "GUEST",
    "PLATFORM_ADMIN"
]
UserAccountType = Literal[
    "WEB_UI",
    "API"
]
UserPreferenceName = Literal[
    "DASHBOARD_PERSONA",
    "NEWS_BANNER_SHOW",
    "RECENTLY_FOUND_CERTIFICATES_INTERVAL",
    "SELECTED_USER_ENTITLEMENT",
    "DEFAULT_PAGE_VIEW_CA_ACCOUNTS",
    "DEFAULT_PAGE_VIEW_APPLICATIONS",
    "DEFAULT_PAGE_VIEW_USERS",
    "DEFAULT_PAGE_VIEW_TEAMS",
    "DEFAULT_PAGE_VIEW_ORGANIZATIONAL_UNITS",
    "DEFAULT_PAGE_VIEW_OD_CERTIFICATES",
    "SAVED_QUERIES_ACTIVITY_LOGGING",
    "PREFERENCE_1",
    "PREFERENCE_2",
    "PREFERENCE_3",
    "PREFERENCE_4",
    "PREFERENCE_5",
    "PREFERENCE_6",
    "PREFERENCE_7"
]
UserStatus = Literal[
    "PENDING_ACTIVATION",
    "ACTIVE",
    "INACTIVE"
]
UserType = Literal[
    "EXTERNAL",
    "INTERNAL"
]

class ApiKeyInformation(ObjectModel):
    apiKeyStatus: ApiKeyStatus = ApiField(alias='apiKeyStatus')
    apiVersion: ApiVersion = ApiField(alias='apiVersion')
    companyId: UUID = ApiField(alias='companyId')
    creationDate: datetime = ApiField(alias='creationDate')
    key: UUID = ApiField(alias='key')
    memberedTeams: List[UUID] = ApiField(alias='memberedTeams', default_factory=list)
    productRoles: Dict[str, List[Role]] = ApiField(alias='productRoles', default_factory=dict)
    systemRoles: List[SystemRole] = ApiField(alias='systemRoles', default_factory=list)
    userId: UUID = ApiField(alias='userId')
    username: str = ApiField(alias='username')
    validityEndDate: datetime = ApiField(alias='validityEndDate')
    validityStartDate: datetime = ApiField(alias='validityStartDate')

class ApiKeyNullResponse(ObjectModel):
    key: UUID = ApiField(alias='key')
    username: str = ApiField(alias='username')

class ApiKeyRequest(ObjectModel):
    apiVersion: ApiVersion = ApiField(alias='apiVersion')
    validityDays: int = ApiField(alias='validityDays')

class ApiKeyResponse(ObjectModel):
    apiKeys: List[ApiKeyInformation] = ApiField(alias='apiKeys', default_factory=list)

class CapabilityInformation(ObjectModel):
    isTrial: bool = ApiField(alias='isTrial')
    name: Capability = ApiField(alias='name')
    productExpiryDate: datetime = ApiField(alias='productExpiryDate')

class ChangePasswordRequest(ObjectModel):
    currentPassword: str = ApiField(alias='currentPassword')
    newPassword: str = ApiField(alias='newPassword')

class CompanyInformation(ObjectModel):
    active: bool = ApiField(alias='active')
    companyType: CompanyType = ApiField(alias='companyType')
    creationDate: datetime = ApiField(alias='creationDate')
    domains: List[str] = ApiField(alias='domains', default_factory=list)
    id: UUID = ApiField(alias='id')
    name: str = ApiField(alias='name')
    productEntitlements: List[ProductEntitlementInformation] = ApiField(
        alias='productEntitlements',
        default_factory=list
    )
    referralPartner: ReferralPartner = ApiField(alias='referralPartner')
    urlPrefix: str = ApiField(alias='urlPrefix')

class CompanyLoginConfigResponse(ObjectModel):
    companyId: UUID = ApiField(alias='companyId')
    newConfigEnabled: bool = ApiField(alias='newConfigEnabled')
    ssoLogin: bool = ApiField(alias='ssoLogin')

class CreateTeamRequest(ObjectModel):
    members: List[UUID] = ApiField(alias='members', default_factory=list)
    name: str = ApiField(alias='name')
    owners: List[UUID] = ApiField(alias='owners', default_factory=list)
    role: TeamRole = ApiField(alias='role')
    userMatchingRules: List[UserMatchingRule] = ApiField(alias='userMatchingRules', default_factory=list)

class ErrorInformation(ObjectModel):
    args: List[AnyValue] = ApiField(alias='args', default_factory=list)
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
    productRoles: Dict[str, List[Role]] = ApiField(alias='productRoles', default_factory=dict)
    properties: Dict[str, str] = ApiField(alias='properties', default_factory=dict)

class InvitationRequest(ObjectModel):
    properties: Dict[str, str] = ApiField(alias='properties', default_factory=dict)
    roles: Dict[str, Role] = ApiField(alias='roles', default_factory=dict)
    teams: List[UUID] = ApiField(alias='teams', default_factory=list)

class InvitationResponse(ObjectModel):
    invitations: List[InvitationInformation] = ApiField(alias='invitations', default_factory=list)

class LocalLoginRequest(ObjectModel):
    localLoginDisabled: bool = ApiField(alias='localLoginDisabled')

class NotificationConfigurationInformation(ObjectModel):
    id: UUID = ApiField(alias='id')
    recipients: List[str] = ApiField(alias='recipients', default_factory=list)
    recurrencePattern: RecurrencePatternInformation = ApiField(alias='recurrencePattern')
    type: NotificationType = ApiField(alias='type')

class NotificationConfigurationRequest(ObjectModel):
    recipients: List[str] = ApiField(alias='recipients', default_factory=list)
    recurrencePattern: RecurrencePatternInformation = ApiField(alias='recurrencePattern')
    type: NotificationType = ApiField(alias='type')

class NotificationConfigurationResponse(ObjectModel):
    configurations: List[NotificationConfigurationInformation] = ApiField(alias='configurations', default_factory=list)

class ProductEntitlementInformation(ObjectModel):
    capabilities: List[CapabilityInformation] = ApiField(alias='capabilities', default_factory=list)
    label: ProductEntitlement = ApiField(alias='label')
    visibilityConstraintsInformation: VisibilityConstraintsInformation = ApiField(
        alias='visibilityConstraintsInformation'
    )

class RecurrencePatternInformation(ObjectModel):
    recurrenceType: RecurrenceType = ApiField(alias='recurrenceType')
    recurrenceValues: List[DayOfWeek] = ApiField(alias='recurrenceValues', default_factory=list)

class ResendActivationRequest(ObjectModel):
    email: str = ApiField(alias='email')

class ResendActivationResponse(ObjectModel):
    user: UserInformation = ApiField(alias='user')

class ResetPasswordRequest(ObjectModel):
    email: str = ApiField(alias='email')

class ResetPasswordResponse(ObjectModel):
    message: str = ApiField(alias='message')

class RolesRequest(ObjectModel):
    roles: Dict[str, Role] = ApiField(alias='roles', default_factory=dict)
    systemAdmin: bool = ApiField(alias='systemAdmin')

class SsoConfigurationInformation(ObjectModel):
    clientId: str = ApiField(alias='clientId')
    clientSecret: str = ApiField(alias='clientSecret')
    companyId: UUID = ApiField(alias='companyId')
    id: UUID = ApiField(alias='id')
    issuerUrl: str = ApiField(alias='issuerUrl')
    newConfigEnabled: bool = ApiField(alias='newConfigEnabled')
    scopes: List[str] = ApiField(alias='scopes', default_factory=list)
    skipUserInfo: bool = ApiField(alias='skipUserInfo')

class SsoConfigurationRequest(ObjectModel):
    clientId: str = ApiField(alias='clientId')
    clientSecret: str = ApiField(alias='clientSecret')
    issuerUrl: str = ApiField(alias='issuerUrl')
    newConfigEnabled: bool = ApiField(alias='newConfigEnabled')
    scopes: List[str] = ApiField(alias='scopes', default_factory=list)
    skipUserInfo: bool = ApiField(alias='skipUserInfo')

class SsoConfigurationResponse(ObjectModel):
    ssoConfigurations: List[SsoConfigurationInformation] = ApiField(alias='ssoConfigurations', default_factory=list)

class TeamInformation(ObjectModel):
    companyId: UUID = ApiField(alias='companyId')
    id: UUID = ApiField(alias='id')
    members: List[UUID] = ApiField(alias='members', default_factory=list)
    modificationDate: datetime = ApiField(alias='modificationDate')
    name: str = ApiField(alias='name')
    owners: List[UUID] = ApiField(alias='owners', default_factory=list)
    productRoles: Dict[str, List[Role]] = ApiField(alias='productRoles', default_factory=dict)
    role: TeamRole = ApiField(alias='role')
    systemRoles: List[SystemRole] = ApiField(alias='systemRoles', default_factory=list)
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
    userId: UUID = ApiField(alias='userId')

class UpdateTeamRequest(ObjectModel):
    name: str = ApiField(alias='name')
    role: TeamRole = ApiField(alias='role')
    userMatchingRules: List[UserMatchingRule] = ApiField(alias='userMatchingRules', default_factory=list)

class UserAccountRequest(ObjectModel):
    companyName: str = ApiField(alias='companyName')
    firstname: str = ApiField(alias='firstname')
    grecaptchaResponse: str = ApiField(alias='grecaptchaResponse')
    lastname: str = ApiField(alias='lastname')
    marketoAttributes: Dict[str, str] = ApiField(alias='marketoAttributes', default_factory=dict)
    password: str = ApiField(alias='password')
    urlPrefix: str = ApiField(alias='urlPrefix')
    userAccountType: UserAccountType = ApiField(alias='userAccountType')
    username: str = ApiField(alias='username')

class UserAccountResponse(ObjectModel):
    apiKey: ApiKeyInformation = ApiField(alias='apiKey')
    company: CompanyInformation = ApiField(alias='company')
    user: UserInformation = ApiField(alias='user')

class UserAccountTypeRequest(ObjectModel):
    accountType: UserAccountType = ApiField(alias='accountType')

class UserDisabledRequest(ObjectModel):
    disabled: bool = ApiField(alias='disabled')

class UserInformation(ObjectModel):
    companyId: UUID = ApiField(alias='companyId')
    creationDate: datetime = ApiField(alias='creationDate')
    disabled: bool = ApiField(alias='disabled')
    emailAddress: str = ApiField(alias='emailAddress')
    firstLoginDate: datetime = ApiField(alias='firstLoginDate')
    firstname: str = ApiField(alias='firstname')
    hasPassword: bool = ApiField(alias='hasPassword')
    id: UUID = ApiField(alias='id')
    lastname: str = ApiField(alias='lastname')
    localLoginDisabled: bool = ApiField(alias='localLoginDisabled')
    memberedTeams: List[UUID] = ApiField(alias='memberedTeams', default_factory=list)
    ownedTeams: List[UUID] = ApiField(alias='ownedTeams', default_factory=list)
    productRoles: Dict[str, List[Role]] = ApiField(alias='productRoles', default_factory=dict)
    signupAttributes: Dict[str, str] = ApiField(alias='signupAttributes', default_factory=dict)
    ssoStatus: SSOStatus = ApiField(alias='ssoStatus')
    systemRoles: List[SystemRole] = ApiField(alias='systemRoles', default_factory=list)
    userAccountType: UserAccountType = ApiField(alias='userAccountType')
    userStatus: UserStatus = ApiField(alias='userStatus')
    userType: UserType = ApiField(alias='userType')
    username: str = ApiField(alias='username')

class UserLoginConfigResponse(ObjectModel):
    companyId: UUID = ApiField(alias='companyId')
    localLogin: bool = ApiField(alias='localLogin')
    ssoLogin: bool = ApiField(alias='ssoLogin')

class UserMatchingRule(ObjectModel):
    claimName: str = ApiField(alias='claimName')
    operator: Operator = ApiField(alias='operator')
    value: str = ApiField(alias='value')

class UserPreferenceInformation(ObjectModel):
    id: UUID = ApiField(alias='id')
    name: UserPreferenceName = ApiField(alias='name')
    value: AnyValue = ApiField(alias='value')

class UserPreferenceRequest(ObjectModel):
    name: UserPreferenceName = ApiField(alias='name')
    value: AnyValue = ApiField(alias='value')

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
CapabilityInformation.update_forward_refs()
ChangePasswordRequest.update_forward_refs()
CompanyInformation.update_forward_refs()
CompanyLoginConfigResponse.update_forward_refs()
CreateTeamRequest.update_forward_refs()
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
UserDisabledRequest.update_forward_refs()
UserInformation.update_forward_refs()
UserLoginConfigResponse.update_forward_refs()
UserMatchingRule.update_forward_refs()
UserPreferenceInformation.update_forward_refs()
UserPreferenceRequest.update_forward_refs()
UserPreferencesResponse.update_forward_refs()
UserResponse.update_forward_refs()
VisibilityConstraintsInformation.update_forward_refs()
