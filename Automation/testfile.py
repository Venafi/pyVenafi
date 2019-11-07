from tools.logger.logger import log_to_html
from config.settings import LOG_TO_JSON
from config.test_base import TestBase
from apilibs.authenticator import Authenticate
from features.folder import Folder
from features.credentials import UsernamePasswordCredential
from tools.threads import Thread


class TestNewStyleLibs(TestBase):
    def __init__(self):
        self.auth = Authenticate(username='local:admin', password='newPassw0rd!', preference='websdk')

    def websdk_test(self):
        self.auth.preference = 'websdk'
        self.run_test()

    def aperture_test(self):
        self.auth.preference = 'aperture'
        self.run_test()

    def run_test(self):
        folder = Folder(self.auth)
        folder.create('_%s_%s' % (self.auth.preference, self.timestamp), '\\VED\\Policy')

        cred = UsernamePasswordCredential(self.auth)
        cred.create(
            name='_%s_credential' % self.auth.preference,
            folder=folder,
            username= 'tyler',
            password='newPassw0rd!'
        )
        self.logger.log('Created credential!!')

    def identity_test(self):
        admin = self.auth.websdk.Identity.Browse.post('admin', 100, 11).identities
        groups = self.auth.websdk.Identity.GetMemberships.post(identity=admin[0]).memberships
        users = self.auth.websdk.Identity.GetMembers.post(identity=groups[0]).members

    def get_objects_test(self):
        result = self.auth.websdk.Config.FindObjectsOfClass.post(class_name='PKCS11', object_dn=r'\VED\Policy\DevApps', recursive=True)
        pksc11_objects = result.object
        print("\n".join([obj.dn for obj in pksc11_objects]))

    def create_pkcs11_application(self):
        with Folder(auth_obj=self.auth, name='Tyler_%s'%self.timestamp, container=r'\VED\Policy') as folder:
            websdk = self.auth.websdk
            named_attr = lambda x, y: {"Name": x, "Value": y}

            device_attributes = [
                named_attr('Host', 'dc.psdev.local'),
                named_attr('Temp Directory', 'C:\\Temp'),
                named_attr('Remote Server Type', 'OS_WINDOWS'),
                named_attr('Credential', r'\VED\Policy\Credentials\Win Domain')
            ]
            device = websdk.Config.Create.post(object_dn=folder.dn+"\\TylersDevice", class_name='Device', name_attribute_list=device_attributes).object

            app_attributes = [
                named_attr('Driver Name', r'apppkcs11'),
                named_attr('Disabled', r'0'),
                named_attr('HSM:Certificate Directory', r'C:\\Users\\Administrator\\E1\\RSA\\Oracle'),
                named_attr('HSM:Requested Usecase', r'TLS Server - RSA - IBM JVM'),
            ]
            application = websdk.Config.Create.post(object_dn=device.dn+"\\TylersApp", class_name="PKCS11", name_attribute_list=app_attributes).object
            print(application.dn)

    def get_workflow_by_guid(self):
        # websdk = self.auth.websdk
        # result = websdk.session.post('https://192.168.7.157/vedsdk/Workflow/Ticket/Status', data=json.dumps({"GUID": "{c15e5db9-2d14-42c7-af7b-ea7a783ca2df}"}))
        # print(result.json())
        aperture = self.auth.aperture
        result = aperture.session.get('https://192.168.7.157/aperture/api/workflow/ticketStatus/{4cefcff1-ebfd-4c7c-9e93-9ffbd3798cbf}')
        print(result.json())

    def create_many_folders_with_creds(self, parent_folder, folder_name, cred_name):
        # if folder_name.endswith('0'):
        #     raise ValueError("I don't like this value at al!")
        folder = Folder(self.auth)
        cred = UsernamePasswordCredential(self.auth)
        folder.create(
            name=folder_name,
            container=parent_folder
        )
        cred.create(
            name=cred_name,
            folder=folder,
            username='admin',
            password='newPassw0rd!'
        )
        return folder, cred

    def try_creating_many_folder_with_creds(self):
        # with Folder(auth_obj=self.auth, name='TestThreads', container='\\VED\\Policy') as folder:
        folder = Folder(self.auth)
        folder.create(name='TestThreads', container='\\VED\\Policy')

        threads = [
            Thread.create_thread(
                self.create_many_folders_with_creds,
                parent_folder=folder.dn,
                folder_name='folder_%s_%s'% (self.timestamp, i),
                cred_name="y_%s_%s" % (self.timestamp, i)
            ) for i in range(100)
        ]
        results = Thread.run_threads(threads)
        print(results)


if __name__ == '__main__':
    x = TestNewStyleLibs()
    try:
        x.try_creating_many_folder_with_creds()
        # x.websdk_test()
        # x.aperture_test()
    except Exception as e:
        x.logger.log_exception()
        raise
    finally:
        if LOG_TO_JSON:
            log_to_html()
