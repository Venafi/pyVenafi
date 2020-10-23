from pypsrp.client import Client, DEFAULT_CONFIGURATION_NAME
from pypsrp.wsman import WinRMTransportError
import os
from datetime import datetime, timezone
import json


def convert_bytes(size):
    for x in ['bytes', 'KB', 'MB', 'GB', 'TB']:
        if size < 1024.0:
            return "%3.1f %s" % (size, x)
        size /= 1024.0

    return size


def convert_from_json_date(dt: str, utc: bool = False):
    dt = ''.join((d for d in dt if d.isdigit()))
    dt = datetime.fromtimestamp(float(dt[:10]), tz=timezone.utc if utc else None)
    return dt.strftime('%d %b %Y %I:%M %p')


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
    def __init__(self, ip_address: str, username: str, password: str, url: str):
        self.ip_address = ip_address
        self.username = username
        self.password = password
        self.url = url


class SqlCloneSession:
    def __init__(self, sql_clone_host: SqlCloneHost):
        self.url = sql_clone_host.url
        self.session = PowerShell(
            server=sql_clone_host.ip_address,
            username=sql_clone_host.username,
            password=sql_clone_host.password
        )

    def sql_connection_properties(self, location_id: str, clone: str):
        script = f"""
            Connect-SqlClone -ServerUrl "{self.url}"
            $instance = Get-SqlCloneSqlServerInstance | Where-Object {{$_.Id -eq {location_id}}}
            Resolve-DnsName $instance.ServerAddress -DnsOnly | ConvertTo-Json
        """
        stdout, stderr, has_errors = self.session.execute_ps(script=script)
        details = json.loads(stdout)
        if isinstance(details, list):
            details = details[0]

        properties = '\n'.join([f"{k} = {v}" for k, v in {
            'HostName'      : details['Name'],
            'IP Address'    : details['IP4Address'],
            'Port'          : 1433,
            'DB Name'       : clone
        }.items()])
        return properties.strip()

    def list_machines(self, name_only: bool = False):
        script = f"""
            Connect-SqlClone -ServerUrl "{self.url}"
            {'Get-SqlCloneMachine | Select-Object MachineName' if name_only else 'Get-SqlCloneMachine'}
        """
        stdout, stderr, has_errors = self.session.execute_ps(script=script)
        return stdout

    def get_machines(self) -> list:
        script = f"""
            Connect-SqlClone -ServerUrl "{self.url}"
            Get-SqlCloneMachine | ConvertTo-Json
        """
        stdout, stderr, has_errors = self.session.execute_ps(script=script)
        return json.loads(stdout)

    def list_images(self) -> list:
        print(f'Retrieving images...')
        script = f"""
            Connect-SqlClone -ServerUrl "{self.url}"
            Get-SqlCloneImage | ConvertTo-Json
        """
        stdout, stderr, has_errors = self.session.execute_ps(script=script)
        images = json.loads(stdout)
        if not isinstance(images, list):
            images = [images]
        for image in images:
            image = self.normalize_image_details(image)
        return images

    def list_clones(self, image: str) -> list:
        print(f'Retrieving clones from {image}...')
        script = f"""
            Connect-SqlClone -ServerUrl "{self.url}"
            $image = Get-SqlCloneImage -Name "{image}"
            Get-SqlClone | Where-Object {{$_.ParentImageId -eq $image.Id}} | ConvertTo-Json
        """
        stdout, stderr, has_errors = self.session.execute_ps(script=script)
        clones = json.loads(stdout)
        if not isinstance(clones, list):
            clones = [clones]
        for clone in clones:
            clone = self.normalize_clone_details(clone, image)
        return clones

    def create_clone(self, machine: str, image: str, clone: str, wait: bool = True):
        print(f'Creating a clone named "{clone}" from image "{image}" on "{machine}"...')
        template = "Set New Broker"
        if not self.does_template_exist(image=image, template=template):
            self.create_template(
                image=image,
                name=template,
                sql="""
                    EXEC('ALTER DATABASE [' + @SQLClone_CloneName + '] SET NEW_BROKER WITH ROLLBACK IMMEDIATE')
                """
            )

        script = f"""
            Connect-SqlClone -ServerUrl {self.url}
            $image = Get-SqlCloneImage -Name {image}
            $SqlServerInstance = Get-SqlCloneSqlServerInstance -MachineName "{machine}"
            $template = Get-SqlCloneTemplate -Image $image -Name "{template}"
            {f'$image | New-SqlClone -Name "{clone}" -Location $sqlServerInstance -Template $template' + (' | Wait-SqlCloneOperation' if wait else '')}
        """
        self.session.execute_ps(script=script)
        if not self.does_clone_exists(image=image, clone=clone):
            raise SqlCloneException(f'Unable to create {clone} from {image}.')

    def reset_clone(self, image: str, clone: str, wait: bool = True):
        print(f'Resetting "{clone}"...')
        script = f"""
            Connect-SqlClone -ServerUrl "{self.url}"
            $image = Get-SqlCloneImage -Name "{image}"
            $clone = Get-SqlClone -Name "{clone}" -Image $image
            {'Reset-SqlClone -Clone $clone' + (' | Wait-SqlCloneOperation' if wait else '')}
        """
        self.session.execute_ps(script=script)

    def delete_clone(self, image: str, clone: str, wait: bool = True):
        print(f'Deleting "{clone}"...')
        script = f"""
            Connect-SqlClone -ServerUrl "{self.url}"
            $image = Get-SqlCloneImage -Name "{image}"
            $clone = Get-SqlClone -Name "{clone}" -Image $image
            {'Remove-SqlClone -Clone $clone' + (' | Wait-SqlCloneOperation' if wait else '')}
        """
        self.session.execute_ps(script=script)
        if self.does_clone_exists(image=image, clone=clone, should_exist=False):
            raise SqlCloneException(f'Unable to delete {clone}.')

    def does_clone_exists(self, image: str, clone: str, should_exist=True):
        if should_exist:
            print(f'Validating that "{clone}" exists under "{image}"...')
        else:
            print(f'Validating that "{clone}" does not exist under "{image}"...')
        script = f"""
            Connect-SqlClone -ServerUrl "{self.url}"
            $image = Get-SqlCloneImage -Name "{image}"
            try {{
                $clone = Get-SqlClone -Name "{clone}" -Image $image
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

    @staticmethod
    def normalize_image_details(image_details: dict):
        image_details['CreatedDate'] = convert_from_json_date(image_details['CreatedDate'])
        image_details['CreatedDateUtc'] = convert_from_json_date(image_details['CreatedDateUtc'], utc=True)
        image_details['SizeInBytes'] = convert_bytes(image_details['SizeInBytes'])
        return image_details

    @staticmethod
    def normalize_clone_details(clone_details: dict, image: str):
        clone_details['CreatedDate'] = convert_from_json_date(clone_details['CreatedDate'])
        clone_details['CreatedDateUtc'] = convert_from_json_date(clone_details['CreatedDateUtc'], utc=True)
        clone_details['SizeInBytes'] = convert_bytes(clone_details['SizeInBytes'])
        clone_details['Image Name'] = image
        return clone_details

    def get_clone(self, image: str, clone: str):
        print(f'Retrieving {clone} from {image}...')
        script = f"""
            Connect-SqlClone -ServerUrl "{self.url}"
            $image = Get-SqlCloneImage -Name "{image}"
            Get-SqlClone -Name "{clone}" -Image $image | ConvertTo-Json
        """
        stdout, stderr, has_errors = self.session.execute_ps(script=script)
        if not stdout:
            print(f'{clone} does not exist.')
            return

        clone_details = json.loads(stdout)
        if not isinstance(clone_details, dict):
            if isinstance(clone_details, (list, tuple)):
                print(f'Expected only one clone with the name "{clone}", but found {len(clone_details)} instances instead.')
            else:
                print(f'An unknown error occurred in getting "{clone}".')
            return
        clone_details = self.normalize_clone_details(clone_details, image)
        properties = self.sql_connection_properties(
            location_id=clone_details['LocationId'],
            clone=clone
        )
        print('\n'.join([
            '------------ Clone Details -----------',
            "\n".join([f'{k}: {v}' for k, v in clone_details.items()]),
        ]))
        print('\n')
        print( "\n".join([
                f"--------- Connection Details ---------",
                f"{properties.strip()}"
            ]))
        return stdout

    def does_template_exist(self, image: str, template: str):
        print(f'Validating that the template "{template}" exists...')
        script = f"""
            Connect-SqlClone -ServerUrl "{self.url}"
            try {{
                $image = Get-SqlCloneImage -Name "{image}"
                $template = Get-SqlCloneTemplate -Name "{template}" -Image $image
                if(!$template) {{
                    return $false
                }}
                return $true
            }} catch {{
                return $false
            }}
        """
        stdout, stderr, has_errors = self.session.execute_ps(script=script)
        return eval(stdout)

    def create_template(self, image: str, name: str, sql: str):
        print(f'Creating new template {name} on {image}...')
        script = f"""
            Connect-SqlClone -ServerUrl "{self.url}"
            $image = Get-SqlCloneImage -Name "{image}"
            New-SqlCloneTemplate -Name "{name}" -Image $image -Modifications (New-SqlCloneSqlScript -Sql "{sql.strip()}")
        """
        self.session.execute_ps(script=script)


def main():
    # region Clear Method
    _clr_cmd = 'cls' if os.name == 'nt' else 'clear'
    clear = lambda: os.system(_clr_cmd)
    # endregion Clear Method

    def get_option(msg: str, opts: list):
        while True:
            print(msg)
            for e, img in enumerate(opts):
                print(f'    {e + 1}. {img}')
            try:
                i = int(input('\nChoice: ')) - 1
                return opts[i].strip()
            except KeyboardInterrupt:
                exit(1)
            except:
                clear()

    # region Initialize SqlCloneHost
    clear()

    hosts = {
        'SQLCLONE.venspi.eng.venafi.com': SqlCloneHost(ip_address='10.100.209.16',
                     username=r'VENSPI\Administrator', password='P@ssw0rd!', url=f'http://10.100.209.16')
    }

    host = get_option('Choose a SQL Clone server.', list(hosts.keys()))
    sqlclone_host = SqlCloneSession(hosts[host])
    # endregion Initialize SqlCloneHost

    clear()

    # region Get Execution Method
    options = [
        'Create A Clone',
        'Reset A Clone',
        'Delete A Clone',
        'Show Clone Details',
        'List Clones',
        'List Images',
    ]

    task = get_option('What would you like to do?', options)
    # endregion Get Execution Method

    clear()

    # region Get Image
    # region Method = List Images (No Inputs Required)
    images = sqlclone_host.list_images()
    if task == 'List Images':
        clear()
        print(f'------------- Images On {host} -------------\n')
        for image in images:
            print('\n'.join(f"{k}: {v}" for k, v in image.items()))
            print('\n\t-------------\n')
        return
    # endregion Method = List Images (No Inputs Required)
    image = get_option('Choose an image.', sorted([i['Name'] for i in images]))
    # endregion Get Image

    clear()

    # region Get Clone
    # region Method = List Clones
    if task == 'List Clones':
        clones = sqlclone_host.list_clones(image=image)
        clear()
        if not clones:
            print('There are no clones on this image.')
            return
        print(f'------------- Clones Created From {image} -------------\n')
        for clone in clones:
            print('\n'.join(f"{k}: {v}" for k, v in clone.items()))
            print('\n\t-------------\n')
        return
    # endregion Method = List Clones

    # region Specify Clone Name
    if task != 'Create A Clone':
        clones = sqlclone_host.list_clones(image=image)
        if not clones:
            print('There are no clones on this image.')
            return
        clone = get_option('Choose a clone.', sorted([c['Name'] for c in clones]))
    else:
        print('Provide the name of the clone you would like to create.')
        clone = input('Name: ')
    # endregion Specify Clone Name
    # endregion Get Clone

    clear()

    if task == 'Create A Clone':
        machines = sqlclone_host.get_machines()
        machine = get_option('Choose a machine to store the clone.', sorted([m['MachineName'] for m in machines]))
        sqlclone_host.create_clone(machine=machine, image=image, clone=clone)
    elif task == 'Show Clone Details':
        sqlclone_host.get_clone(image=image, clone=clone)
    elif task == 'Reset A Clone':
        sqlclone_host.reset_clone(image=image, clone=clone)
    elif task == 'Delete A Clone':
        sqlclone_host.delete_clone(image=image, clone=clone)
    else:
        raise Exception(f'Uh-oh. Not sure what to do about {task}.')


if __name__ == '__main__':
    main()
