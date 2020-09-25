from pypsrp.client import Client, DEFAULT_CONFIGURATION_NAME
from pypsrp.wsman import WinRMTransportError
import os


def _format_ps_cmd(cmd: str, params: dict = None):
    args = " ".join([f"-{k} {v}" for k, v in params.items() if v is not None])
    return f'{cmd} {args}'


class PowerShell(Client):
    def __init__(self, server: str, username: str, password: str, port: int = 5985, use_ssl: bool = False, **kwargs):
        super().__init__(
            server=server,
            username=username,
            password=password,
            port=port,
            ssl=use_ssl,
            auth='negotiate',
            reconnection_retries=3,
            **kwargs
        )

        self._server = server
        self._username = username
        self._password = password
        self._port = port
        self._use_ssl = use_ssl
        self._kwargs = kwargs

    def execute_ps(self, script, configuration_name=DEFAULT_CONFIGURATION_NAME,
                   environment=None):
        try:
            stdout, stderr, has_errors = super().execute_ps(script=script, configuration_name=configuration_name,
                                                            environment=environment)
        except WinRMTransportError:
            self.__init__(
                server=self._server,
                username=self._username,
                password=self._password,
                port=self._port,
                use_ssl=self._use_ssl,
                **self._kwargs
            )
            stdout, stderr, has_errors = super().execute_ps(script=script, configuration_name=configuration_name,
                                                            environment=environment)
        if has_errors:
            if not any(stderr.error):
                raise PowerShellException(f'{self._server} threw an unknown error.')
            raise PowerShellException(
                f'{self._server} threw this error:\n' +
                '\n'.join([str(s) for s in stderr.error])
            )
        return stdout, stderr, has_errors


class PowerShellException(Exception):
    pass


class SqlCloneException(Exception):
    pass


class SqlCloneHost:
    def __init__(self, ip_address: str, machine_name: str, sql_instance: str, server_username: str,
                 server_password: str, db_username: str, db_password: str, url: str, port: int = 1433):
        self.ip_address = ip_address
        self.port = port
        self.machine_name = machine_name
        self.sql_instance = sql_instance
        self.server_username = server_username
        self.server_password = server_password
        self.db_username = db_username
        self.db_password = db_password
        self.url = url
        self.session = PowerShell(
            server=ip_address,
            username=server_username,
            password=server_password
        )

    def sql_connection_properties(self, db_name: str):
        properties = '\n'.join([f"{k} = {v}" for k, v in {
            'Host'    : self.ip_address,
            'Port'    : self.port,
            'DB Name' : db_name,
            'Username': self.db_username,
            'Password': self.db_password
        }.items()])
        return "\n".join([
            f"--------- Connection Details ---------",
            f"{properties.strip()}"
        ])

    def list_images(self, name_only: bool = False):
        print(f'Retrieving images from {self.machine_name}...')
        script = f"""
            Connect-SqlClone -ServerUrl "{self.url}"
            {'Get-SqlCloneImage | Select-Object Name' if name_only else 'Get-SqlCloneImage'}
        """
        stdout, stderr, has_errors = self.session.execute_ps(script=script)
        return stdout

    def list_clones(self, image: str, name_only: bool = False):
        print(f'Retrieving clones from {image}...')
        script = f"""
            Connect-SqlClone -ServerUrl "{self.url}"
            $image = Get-SqlCloneImage -Name "{image}"
            Get-SqlClone | Where-Object {{$_.ParentImageId -eq $image.Id}} {'| Select-Object Name' if name_only else ''}
        """
        stdout, stderr, has_errors = self.session.execute_ps(script=script)
        return stdout

    def create_clone(self, image: str, clone: str):
        print(f'Creating a clone named "{clone}" from image "{self.machine_name}\\{image}...')
        script = f"""
            Connect-SqlClone -ServerUrl {self.url}
            $image = Get-SqlCloneImage -Name {image}
            $SqlServerInstance = Get-SqlCloneSqlServerInstance -MachineName "{self.machine_name}"
            $image | New-SqlClone -Name "{clone}" -Location $sqlServerInstance | Wait-SqlCloneOperation
        """
        self.session.execute_ps(script=script)
        if not self.does_clone_exists(clone=clone):
            raise SqlCloneException(f'Unable to create {clone} from {image}.')
        self.set_new_broker_on_clone(clone=clone)
        print(self.sql_connection_properties(db_name=clone))

    def reset_clone(self, clone: str):
        print(f'Resetting "{clone}"...')
        script = f"""
            Connect-SqlClone -ServerUrl "{self.url}"
            $SqlServerInstance = Get-SqlCloneSqlServerInstance -MachineName "{self.machine_name}"
            $clone = Get-SqlClone -Name "{clone}" -Location $SqlServerInstance
            Reset-SqlClone -Clone $clone | Wait-SqlCloneOperation
        """
        self.session.execute_ps(script=script)
        self.set_new_broker_on_clone(clone=clone)

    def delete_clone(self, clone: str):
        print(f'Deleting "{clone}"...')
        script = f"""
            Connect-SqlClone -ServerUrl "{self.url}"
            $SqlServerInstance = Get-SqlCloneSqlServerInstance -MachineName "{self.machine_name}"
            $clone = Get-SqlClone -Name "{clone}" -Location $SqlServerInstance
            Remove-SqlClone -Clone $clone | Wait-SqlCloneOperation
        """
        self.session.execute_ps(script=script)
        if self.does_clone_exists(clone=clone, should_exist=False):
            raise SqlCloneException(f'Unable to delete {clone}.')

    def set_new_broker_on_clone(self, clone: str):
        print(f'Setting a new broker for "{clone}"...')
        script = f"""
            $ServerInstance = "{self.sql_instance}"
            $query = "ALTER DATABASE [`$(DbName)] SET NEW_BROKER WITH ROLLBACK IMMEDIATE"
            $params = "DbName={clone}"
            $result = Invoke-Sqlcmd -ServerInstance $ServerInstance -Database "{clone}" `
                -Query $query -Variable $params -Username "sa" -Password "P@ssw0rd!"
        """
        stdout, stderr, has_errors = self.session.execute_ps(script=script)
        return stdout

    def does_clone_exists(self, clone: str, should_exist=True):
        if should_exist:
            print(f"Validating that {clone} exists...")
        else:
            print(f"Validating that {clone} does not exist...")
        script = f"""
            Connect-SqlClone -ServerUrl "{self.url}"
            $SqlServerInstance = Get-SqlCloneSqlServerInstance -MachineName "{self.machine_name}"
            try {{
                $clone = Get-SqlClone -Name "{clone}" -Location $SqlServerInstance
                if(!$clone) {{
                    return $false
                }}
                return $true
            }} catch {{
                return $false
            }}
        """
        stdout, stderr, has_errors = self.session.execute_ps(script=script)
        return eval(stdout)

    def get_clone(self, clone: str):
        print(f'Retrieving {clone}...')
        script = f"""
            Connect-SqlClone -ServerUrl "{self.url}"
            $SqlServerInstance = Get-SqlCloneSqlServerInstance -MachineName "{self.machine_name}"
            Get-SqlClone -Name "{clone}" -Location $SqlServerInstance
        """
        stdout, stderr, has_errors = self.session.execute_ps(script=script)
        if not stdout:
            print(f'{clone} does not exist.')
        else:
            print('\n'.join([
                '------------ Clone Details -----------',
                stdout.strip(),
            ]))
            print('\n')
            print(self.sql_connection_properties(db_name=clone))
        return stdout



def main():
    # region Clear Method
    _clr_cmd = 'cls' if os.name == 'nt' else 'clear'
    clear = lambda: os.system(_clr_cmd)
    # endregion Clear Method

    def print_options(opts):
        for e, img in enumerate(opts):
            print(f'    {e + 1}. {img}')

    # region Initialize SqlCloneHost
    sqlclone_host = SqlCloneHost(
        ip_address='10.100.209.16',
        machine_name='SQLCLONE',
        sql_instance='SQLCLONE',
        server_username=r'VENSPI\Administrator',
        server_password='P@ssw0rd!',
        db_username='sa',
        db_password='P@ssw0rd!',
        url=f'http://10.100.209.16'
    )
    # endregion Initialize SqlCloneHost

    clear()

    # region Get Execution Method
    options = {
        'Create A New Clone'               : sqlclone_host.create_clone,
        'Reset A Clone'                    : sqlclone_host.reset_clone,
        'Delete A Clone'                   : sqlclone_host.delete_clone,
        'Show Clone Details'               : sqlclone_host.get_clone,
        'List Clones From A Specific Image': sqlclone_host.list_clones,
        'List Images'                      : sqlclone_host.list_images,
    }

    method = None
    while method is None:
        print('What would you like to do?')
        print_options(options.keys())
        index = input('Choice: ')
        try:
            key = list(options)[int(index) - 1]
            method = options[key]
        except:
            clear()
    # endregion Get Execution Method

    clear()

    # region Method = List Images (No Inputs Required)
    if method == sqlclone_host.list_images:
        print(sqlclone_host.list_images())
        return
    # endregion Method = List Images (No Inputs Required)

    # region Get Image
    image = None
    images = sqlclone_host.list_images(name_only=True).strip().split('\n')[2:]
    while image is None:
        print('Choose an image.')
        print_options(images)
        index = input('Choice: ')
        try:
            index = int(index) - 1
            image = images[index]
        except:
            clear()
    # endregion Get Image

    clear()

    # region Get Clone
    clone = None

    # region Method = List Clones
    if method == sqlclone_host.list_clones:
        clones = sqlclone_host.list_clones(image=image)
        if not clones:
            print('There are no clones on this image. Exiting.')
            return
        print(clones)
        return
    # endregion Method = List Clones

    elif method != sqlclone_host.create_clone:
        clones = sqlclone_host.list_clones(image=image, name_only=True).strip().split('\n')[2:]
        if not clones:
            print('There are no clones on this image. Exiting.')
            return

        while clone is None:
            print('Choose a clone.')
            print_options(clones)
            index = input('Choice: ')
            try:
                index = int(index) - 1
                clone = clones[index]
            except:
                clear()
    else:
        print('Provide the name of the clone you would like to create.')
        clone = input('Name: ')
    # endregion Get Clone

    clear()


    if method == sqlclone_host.create_clone:
        method(image=image, clone=clone)

    elif method == sqlclone_host.list_clones:
        method(image=image)

    else:
        method(clone=clone)


if __name__ == '__main__':
    main()
