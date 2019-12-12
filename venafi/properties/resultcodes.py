class ResultCodes:
    Client = {
         0: 'Success, the operation succeeded, however, the client entry is untrusted',
         1: 'SuccessButUntrusted',
         2: 'ArgumentInvalidValue',
         3: 'ArgumentUnsupportedDerivingClass',
         4: 'ArgumentIsEmpty',
         5: 'ArgumentIsNull',
         6: 'BadAuthentication, the authentication check failed',
         7: 'BeginTransactionFailed',
         8: 'CommitTransactionFailed',
         9: 'ConnectionError',
        10: 'ConfigObjectDoesNotExist',
        11: 'ConfigOperationFailed',
        12: 'EntryDoesNotExist',
        13: 'EntryAlreadyExists',
        14: 'EntryIsDisabled, the entry is disabled',
        15: 'EntryIsUntrusted, the entry is untrusted',
        16: 'Exception',
        17: 'DuplicateDriverRegistration, an existing storage driver has already been registered with a matching name',
        18: 'DuplicateIdentifer',
        19: 'DuplicateNetInterface',
        20: 'DuplicateOperatingSystemInTable',
        21: 'DuplicateManufacturerInTable',
        22: 'IdentityFromProviderIdFailed',
        23: 'InsufficientRights (also known as permissions)',
        24: 'InvalidCallingAssembly',
        25: 'InvalidCharacterInDistinguishedName',
        26: 'InvalidDistinguishedName',
        27: 'InvalidDriverName',
        28: 'InvalidDriverPrefix',
        29: 'InvalidKey (ClientId is not formatted correctly)',
        30: 'InvalidKeyRole (ClientId has an invalid role)',
        31: 'InvalidKeyId (ClientId is invalid)',
        32: 'InvalidRole',
        33: 'InvalidOperation',
        34: 'MachineAlreadyExists',
        35: 'MissingDriverInterface',
        36: 'MissingProviderSid',
        37: 'NoDriver',
        38: 'NoPendingOperations',
        39: 'NotImplemented',
        40: 'NotSupported',
        41: 'RightsOperationFailed',
        42: 'StatementExecutionFailed',
        43: 'TransactionInProgress',
        44: 'TryLater (Requested data was not yet available, retry later)',
        45: 'RemoteError (remote request failed; see Error property for details)',
        46: 'FailedToRetrieveSession (Session was not available)'
    }

    Config = {
          1 : 'Success',
          2 : 'InvalidArgument',
          3 : 'InvalidArgumentRange',
          4 : 'MismatchedArguments',
          5 : 'NotImplemented',
          6 : 'InvalidDestinationList',
          7 : 'InsufficientPrivileges',
          8 : 'InvalidOperation',
          9 : 'UnexpectedAssemblyError',
         10 : 'OutOfMemory',
        100 : 'AttributeDoesNotExist',
        101 : 'AttributeAlreadyExists',
        102 : 'AttributeNotFound',
        103 : 'AttributeValueExists',
        104 : 'AttributeStillInUse',
        105 : 'AttributeNameTooLong',
        106 : 'AttributeReferenceDoesNotExist',
        107 : 'AttributeSyntaxCollision',
        108 : 'AttributePropertyCollision',
        109 : 'CannotRemoveMandatory',
        110 : 'AttributeValueIsMandatory',
        111 : 'AttributeValueTooLong',
        112 : 'IllegalAttributeForClass',
        113 : 'InvalidAttributeDN',
        114 : 'AttributeValueDoesNotExist',
        115 : 'AttributeIsSingleValued',
        116 : 'AttributeIsReadOnly',
        117 : 'AttributeIsHidden',
        200 : 'ClassDoesNotExist',
        201 : 'ClassAlreadyExists',
        202 : 'ClassStillInUse',
        203 : 'ClassNameTooLong',
        204 : 'ClassInvalidSuperClass',
        205 : 'ClassInvalidContainmentClass',
        206 : 'ClassInvalidNamingAttribute',
        207 : 'ClassInvalidMandatoryAttribute',
        208 : 'ClassInvalidOptionalAttribute',
        209 : 'ClassInvalidName',
        210 : 'ClassInvalidContainmentSubClass',
        211 : 'ClassInvalidPolicyClass',
        300 : 'PolicyDoesNotExist',
        301 : 'PolicyLockStateCollision',
        350 : 'LockNameAlreadyExists',
        351 : 'LockNameDoesNotExist',
        352 : 'LockNameOwnedByAnother',
        353 : 'LockNameLimitReached',
        354 : 'LockNameAttemptTimedOut',
        400 : 'ObjectDoesNotExist',
        401 : 'ObjectAlreadyExists',
        402 : 'ObjectHasChildren',
        403 : 'ObjectNameTooLong',
        404 : 'ObjectDepthTooDeep',
        405 : 'ObjectInvalidName',
        406 : 'ObjectInvalidClass',
        407 : 'ObjectInvalidContainment',
        408 : 'ObjectMandatoryMissing',
        409 : 'ObjectIsReadOnly',
        410 : 'ObjectInvalidOperation',
        500 : 'DriverMissingDSN',
        501 : 'DriverMissingDatabaseName',
        502 : 'DriverDatabaseError',
        503 : 'DriverTransactionError',
        504 : 'DriverTransactionCollision',
        505 : 'DriverGenerationUpdateError',
        600 : 'CacheLockException',
        601 : 'CacheEntryNotFound',
        602 : 'CacheEntryAlreadyExists',
        603 : 'CacheEntryIsSuperior',
        604 : 'CacheEntryIsIncompatible',
        700 : 'XmlInvalidStructure',
        701 : 'XmlMissingNaming',
        702 : 'XmlMissingSyntax',
        703 : 'XmlMissingProperty',
        704 : 'XmlUnknownElementAttribute'
    }
    
    Credential = {
           1: 'Success',
           2: 'InvalidArgument',
           3: 'InvalidArgumentRange',
           4: 'MismatchedArguments',
           5: 'NotImplemented',
           6: 'InvalidDestinationList',
           7: 'InsufficientPrivileges',
           8: 'InvalidOperation',
           9: 'UnexpectedAssemblyError',
          10: 'OutOfMemory',
         100: 'AttributeDoesNotExist',
         101: 'AttributeAlreadyExists',
         102: 'AttributeNotFound',
         103: 'AttributeValueExists',
         104: 'AttributeStillInUse',
         105: 'AttributeNameTooLong',
         106: 'AttributeReferenceDoesNotExist',
         107: 'AttributeSyntaxCollision',
         108: 'AttributePropertyCollision',
         109: 'CannotRemoveMandatory',
         110: 'AttributeValueIsMandatory',
         111: 'AttributeValueTooLong',
         112: 'IllegalAttributeForClass',
         113: 'InvalidAttributeDN',
         114: 'AttributeValueDoesNotExist',
         115: 'AttributeIsSingleValued',
         116: 'AttributeIsReadOnly',
         117: 'AttributeIsHidden',
         200: 'ClassDoesNotExist',
         201: 'ClassAlreadyExists',
         202: 'ClassStillInUse',
         203: 'ClassNameTooLong',
         204: 'ClassInvalidSuperClass',
         205: 'ClassInvalidContainmentClass',
         206: 'ClassInvalidNamingAttribute',
         207: 'ClassInvalidMandatoryAttribute',
         208: 'ClassInvalidOptionalAttribute',
         209: 'ClassInvalidName',
         210: 'ClassInvalidContainmentSubClass',
         300: 'PolicyDoesNotExist',
         301: 'PolicyLockStateCollision',
         350: 'LockNameAlreadyExists',
         351: 'LockNameDoesNotExist',
         352: 'LockNameOwnedByAnother',
         353: 'LockNameLimitReached',
         354: 'LockNameAttemptTimedOut',
         400: 'Disadvantageous',
         401: 'ObjectAlreadyExists',
         402: 'ObjectHasChildren',
         403: 'ObjectNameTooLong',
         404: 'ObjectDepthTooDeep',
         405: 'ObjectInvalidName',
         406: 'ObjectInvalidClass',
         407: 'ObjectInvalidContainment',
         408: 'ObjectMandatoryMissing',
         409: 'ObjectIsReadOnly',
         410: 'ObjectInvalidOperation',
         500: 'DriverMissingDSN',
         501: 'DriverMissingDatabaseName',
         502: 'DriverDatabaseError',
         503: 'DriverTransactionError',
         504: 'DriverTransactionCollision',
         505: 'DriverGenerationUpdateError',
         600: 'CacheLockException',
         601: 'CacheEntryNotFound',
         602: 'CacheEntryAlreadyExists',
         603: 'CacheEntryIsSuperior',
         604: 'CacheEntryIsIncompatible',
         700: 'XmlInvalidStructure',
         701: 'XmlMissingNaming',
         702: 'XmlMissingSyntax',
         703: 'XmlMissingProperty',
         704: 'XmlUnknownElementAttribute',
        1000: 'SecretStoreFailed',
        1001: 'AddAttributeFailed',
        1002: 'UnexpectedException',
        1003: 'PartialDeleteFailure',
        1004: 'CredentialTypeMismatch',
        1005: 'NoDriver',
        1006: 'VaultTypeMismatch',
        1007: 'DriverDenied',
        1008: 'VaultDataUnrecognized'
    }

    CertificatesWorkToDo = {
          0: 'Success',
          1: 'MissingDSN',
          2: 'MissingDatabaseName',
         99: 'UnexpectedAssemblyError',
        100: 'DatabaseError',
        101: 'DatabaseConnectionUnavailable',
        102: 'TransactionError',
        103: 'TransactionCollision',
        200: 'InsufficientPrivileges',
        300: 'IdentifierDoesNotExist',
        301: 'IdentifierAlreadyExists'
    }

    ChainValidation = {
          0: 'None',
          2: 'Success',
          4: 'NoChain',
          8: 'InvalidChain',
         16: 'ExpiringChain',
         32: 'IncompleteChain',
         64: 'BlacklistedChain',
        128: 'MismatchedChain',
        512: 'MismatchedCertificate'
    }

    Discovery = {
          0: 'None',
          1: 'Success',
          2: 'InvalidArgument',
          3: 'InvalidArgumentRange',
          4: 'MismatchedArguments',
          5: 'NotImplemented',
          6: 'InvalidDestinationList',
          7: 'InsufficientPrivileges',
          8: 'UnexpectedAssemblyError',
         99: 'ConfigAssemblyError',
        100: 'InvalidDiscoveryDefinition',
        102: 'PendingPreviousRun',
        500: 'DriverMissingDSN',
        501: 'DriverMissingDatabaseName',
        502: 'DriverDatabaseError',
        503: 'DriverTransactionError',
        504: 'DriverTransactionCollision',
        505: 'DriverGenerationUpdateError',
        506: 'DriverConnectionError',
        507: 'DriverUnexpectedQueryResult',
        600: 'RemoveVaultEntryError',
    }

    EndEntityValidation = {
        -2147483648: 'UnexpectedError',
          0: 'None',
          2: 'Success',
          4: 'HostResolutionFailed',
          8: 'SettingError',
         16: 'ConnectionFailure',
         32: 'NoCertificateFound',
         64: 'MismatchWithPrevious',
        128: 'MismatchWithKnown',
        256: 'MismatchWithUnknown',
        512: 'NoLocalCertificate',
        536870912: 'NotSupported',
        1073741824: 'RetryLater'
    }

    Metadata = {
         0: 'Success',
         1: 'InvalidConfigObject',
         2: 'InvalidDN',
         3: 'InvalidName',
         4: 'InvalidItem',
         5: 'InvalidClass',
         6: 'InvalidMetadataObject',
         7: 'InvalidRights',
         8: 'ItemIsNull',
         9: 'ItemAlreadyExists',
        10: 'ItemTypeUnknown',
        11: 'ConfigCreateFailed',
        12: 'ConfigWriteFailed',
        13: 'ConfigDeleteFailed',
        14: 'MetadataInUse',
        15: 'NoAllowedValues',
        16: 'AllowedValueDoesNotExist',
        17: 'ValueNotInAllowedList',
        18: 'ItemNotValidForClass',
        19: 'NameTooLong',
        20: 'TooManyContainers',
        21: 'ConfigDnNotContainer',
        22: 'InvalidPolicyState',
        23: 'ConfigLockFailed',
        24: 'ConfigReadFailed',
        25: 'RemoteError'
    }

    SecretStore = {
         0: 'Success',
         1: 'InvalidCallingAssembly',
         2: 'CreateDatabaseError',
         3: 'UseDatabaseError',
         4: 'CreateTableError',
         5: 'CreateIndexError',
         6: 'ConnectionError',
         7: 'TransactionError',
         8: 'InvalidVaultID',
         9: 'InvalidParams',
        10: 'InsufficientPermissions',
        11: 'CryptoFailure',
        12: 'DeleteSecretFailed',
        13: 'AddSecretFailed',
        14: 'RetrieveSecretFailed',
        15: 'RetrieveSecretTypeFailed',
        16: 'GetNextVaultIDFailed',
        17: 'DisassociateFailed',
        18: 'OwnerLookupFailed',
        19: 'AssociateDataFailed',
        20: 'LookupFailed',
        21: 'InvalidKey',
        22: 'QueryError',
        23: 'SecurityGroupNotImplemented'
    }

    ToDo = {
          0 : 'Success',
          1 : 'MissingDSN',
          2 : 'MissingDatabaseName',
         99 : 'UnexpectedAssemblyError',
        100	: 'DatabaseError',
        101	: 'DatabaseConnectionUnavailable',
        102	: 'TransactionError',
        103	: 'TransactionCollision',
        200	: 'InsufficientPrivileges',
        300	: 'IdentifierDoesNotExist',
        301	: 'IdentifierAlreadyExists',
    }

    ValidationProtocols = {
          12: "SSL 2.0",
          48: "SSL 3.0",
          60: "SSL 2.0, SSL 3.0",
         192: "TLS 1.0",
         204: "SSL 2.0, TLS 1.0",
         240: "SSL 3.0, TLS 1.0",
         252: "SSL 2.0, SSL 3.0, TLS 1.0",
         768: "TLS 1.1",
         780: "SSL 2.0, TLS 1.1",
         816: "SSL 3.0, TLS 1.1",
         960: "TLS 1.0, TLS 1.1",
         828: "SSL 2.0, SSL 3.0, TLS 1.1",
         972: "SSL 2.0, TLS 1.0, TLS 1.1",
        1008: "SSL 3.0, TLS 1.0, TLS 1.1",
        1020: "SSL 2.0, SSL 3.0, TLS 1.0, TLS 1.1",
        3072: "TLS 1.2",
        3084: "SSL 2.0, TLS 1.2",
        3120: "SSL 3.0, TLS 1.2",
        3264: "TLS 1.0, TLS 1.2",
        3840: "TLS 1.1, TLS 1.2",
        3132: "SSL 2.0, SSL 3.0, TLS 1.2",
        3276: "SSL 2.0, TLS 1.0, TLS 1.2",
        3852: "SSL 2.0, TLS 1.1, TLS 1.2",
        3312: "SSL 3.0, TLS 1.0, TLS 1.2",
        3888: "SSL 3.0, TLS 1.1, TLS 1.2",
        4032: "TLS 1.0, TLS 1.1, TLS 1.2",
        3324: "SSL 2.0, SSL 3.0, TLS 1.0, TLS 1.2",
        3900: "SSL 2.0, SSL 3.0, TLS 1.1, TLS 1.2",
        4044: "SSL 2.0, TLS 1.0, TLS 1.1, TLS 1.2",
        4080: "SSL 3.0, TLS 1.0, TLS 1.1, TLS 1.2",
        4092: "SSL 2.0, SSL 3.0, TLS 1.0, TLS 1.1, TLS 1.2"
    }
    
    Workflow = {
        0: 'None',
        1: 'Success',
        2: 'GenericFailure',
        3: 'TicketDoesNotExist',
        4: 'InsufficientPrivileges',
        5: 'BadArguments',
        6: 'ObjectDoesNotExist',
        7: 'RemoteError',
        8: 'WorkflowObjectDoesNotExist',
    }
