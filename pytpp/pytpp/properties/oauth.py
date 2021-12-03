from dataclasses import dataclass

@dataclass
class Permissions:
    name: str
    approve: bool = None
    delete: bool = None
    discover: bool = None
    manage: bool = None
    read: bool = None
    revoke: bool = None

    def effective(self):
        return [k for k, v in {
            'approve': self.approve,
            'delete': self.delete,
            'discover': self.discover,
            'manage': self.manage,
            'read': self.read,
            'revoke': self.revoke,
        }.items() if v is not None]

@dataclass
class Scope:
    def __init__(self):
        self._certificate = Permissions(name='certificate')
        self._ssh = Permissions(name='ssh')
        self._codesign = Permissions(name='codesign')
        self._configuration = Permissions(name='configuration')
        self._restricted = Permissions(name='restricted')
        self._security = Permissions(name='security')
        self._statistics = Permissions(name='statistics')
        self._agent = Permissions(name='agent')

    def __str__(self):
        return self.to_string()

    def __repr__(self):
        return self.to_string()

    def to_string(self):
        scopes = [
            f'{p.name}:{",".join(p.effective())}'
            for p in [
                self._certificate, self._ssh, self._codesign,
                self._configuration, self._restricted,
                self._security, self._statistics, self._agent
            ]
        ]
        return ';'.join(scopes)

    def agent(self, delete: bool = False, read: bool = False):
        self._agent.delete = delete
        self._agent.read = read

    def certificate(self, approve: bool = False, delete: bool = False, discover: bool = False,
                    manage: bool = False, read: bool = False, revoke: bool = False):
        self._certificate.approve = approve
        self._certificate.delete = delete
        self._certificate.discover = discover
        self._certificate.manage = manage
        self._certificate.read = read
        self._certificate.revoke = revoke

    def configuration(self, delete: bool = False, manage: bool = False, read: bool = False):
        self._configuration.delete = delete
        self._configuration.manage = manage
        self._configuration.read = read

    def codesign(self, delete: bool = False, manage: bool = False, read: bool = False):
        self._codesign.delete = delete
        self._codesign.manage = manage
        self._codesign.read = read

    def restricted(self, delete: bool = False, manage: bool = False, read: bool = False):
        self._restricted.delete = delete
        self._restricted.manage = manage
        self._restricted.read = read

    def security(self, delete: bool = False, manage: bool = False, read: bool = False):
        self._security.delete = delete
        self._security.manage = manage
        self._security.read = read

    def ssh(self, approve: bool = False, delete: bool = False, discover: bool = False,
            manage: bool = False, read: bool = False):
        self._ssh.approve = approve
        self._ssh.delete = delete
        self._ssh.discover = discover
        self._ssh.manage = manage
        self._ssh.read = read

    def statistics(self, read: bool = False):
        self._statistics.read = read


if __name__ == '__main__':
    scope = Scope()
    scope.certificate(True, True, True, True, True, True)
    scope.ssh(*[True * 5])
    scope.codesign(*[True * 3])
    scope.configuration(*[True * 3])
    scope.restricted(*[True * 3])
    scope.security(True, True, True)
    scope.statistics(True)
    scope.agent(*[True * 2])
    print(scope.to_string())
