class Scope:
    @classmethod
    def _create_scope(cls, scope_name: str, approve: bool= False, delete: bool = False, discover: bool = False,
                      manage: bool = False, revoke: bool = False):
        restrictions = []
        if approve:
            restrictions.append('approve')
        if delete:
            restrictions.append('delete')
        if discover:
            restrictions.append('discover')
        if manage:
            restrictions.append('manage')
        if revoke:
            restrictions.append('revoke')
        if restrictions:
            return f'{scope_name}:' + ','.join(restrictions)
        else:
            return scope_name

    @classmethod
    def any(cls, approve: bool = False, manage: bool = False):
        return cls._create_scope('any', approve=approve, manage=manage)

    @classmethod
    def agent(cls, delete: bool = False):
        return cls._create_scope('agent', delete=delete)

    @classmethod
    def certificate(cls, delete: bool = False, discover: bool = False, manage: bool = False,
                    revoke: bool = False):
        return cls._create_scope('certificate', delete=delete, discover=discover, manage=manage,
                                 revoke=revoke)

    @classmethod
    def configuration(cls, delete: bool = False, manage: bool = False):
        return cls._create_scope('configuration', delete=delete, manage=manage)

    @classmethod
    def restricted(cls, delete: bool = False, manage: bool = False):
        return cls._create_scope('restricted', delete=delete, manage=manage)

    @classmethod
    def security(cls, delete: bool = False, manage: bool = False):
        return cls._create_scope('security', delete=delete, manage=manage)

    @classmethod
    def ssh(cls, delete: bool = False, discover: bool = False, manage: bool = False):
        return cls._create_scope('ssh', delete=delete, discover=discover, manage=manage)
