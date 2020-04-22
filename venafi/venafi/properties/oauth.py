class Scope:
    def __init__(self):
        self.scopes = []

    def _scope(self, scope_name: str, approve: bool = None, delete: bool = None, discover: bool = None,
               manage: bool = None, read: bool = None, revoke: bool = None):
        scope = {
            'name': scope_name, 
            'permissions': {
                'approve': approve,
                'delete': delete,
                'discover': discover,
                'manage': manage,
                'read': read,
                'revoke': revoke
            }
        }
        self.scopes.append(scope)

    def to_string(self):
        total_scope = []
        for scope in self.scopes:  # type: dict
            name = scope.get('name', '??unknown??')
            restrictions = ','.join([
                k for k, v in scope.get('permissions', {}).items()
                if v is True and k != 'read'
            ])
            if restrictions:
                total_scope.append(f"{name}:{restrictions}")
            else:
                total_scope.append(name)
        return ';'.join(total_scope)

    def agent(self, delete: bool = False, read: bool = False):
        self._scope(
            scope_name='agent',
            delete=delete,
            read=read
        )

    def certificate(self, approve: bool = False, delete: bool = False, discover: bool = False,
                    manage: bool = False, read: bool = False, revoke: bool = False):
        self._scope(
            scope_name='certificate',
            approve=approve,
            delete=delete,
            discover=discover,
            manage=manage,
            read=read,
            revoke=revoke
        )

    def configuration(self, delete: bool = False, manage: bool = False, read: bool = False):
        self._scope(
            scope_name='configuration',
            delete=delete,
            manage=manage,
            read=read
        )

    def codesign(self, delete: bool = False, manage: bool = False, read: bool = False):
        self._scope(
            scope_name='codesign',
            delete=delete,
            manage=manage,
            read=read
        )

    def restricted(self, delete: bool = False, manage: bool = False, read: bool = False):
        self._scope(
            scope_name='restricted',
            delete=delete,
            manage=manage,
            read=read
        )

    def security(self, delete: bool = False, manage: bool = False, read: bool = False):
        self._scope(
            scope_name='security',
            delete=delete,
            manage=manage,
            read=read
        )

    def ssh(self, approve: bool = False, delete: bool = False, discover: bool = False,
            manage: bool = False, read: bool = False):
        self._scope(
            scope_name='ssh',
            approve=approve,
            delete=delete,
            discover=discover,
            manage=manage,
            read=read
        )

    def statistics(self, read: bool = False):
        self._scope(
            scope_name='statistics',
            read=read
        )
