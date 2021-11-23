#!/usr/bin/env python
import os
import sys
from pathlib import Path
import ftplib
from tempfile import NamedTemporaryFile
from setuptools import sandbox
from setup import __version__
import threading
import requests
import shutil
from typing import List
from packaging.version import Version
from paramiko import SSHClient, AutoAddPolicy

PROJECT_DIR = os.path.dirname(os.path.abspath(__file__))
REMOTE_PACKAGES_DIR = '/spi/packages/data'

class UploadFiles:
    def __init__(self):
        self.host = '10.100.203.5'
        self.port = 22
        self.username = r'root'
        self.password = 'newPassw0rd!'

        self.ssh_client = SSHClient()
        self.ssh_client.load_system_host_keys()
        self.ssh_client.set_missing_host_key_policy(AutoAddPolicy())
        self.ssh_client.connect(
            hostname=self.host,
            port=self.port,
            username=self.username,
            password=self.password
        )

    @staticmethod
    def print_stage(msg: str):
        print(f'\n>>>>>>>>>>>>>>>>>>>>>>>>> {msg} <<<<<<<<<<<<<<<<<<<<<<<<<\n')

    def upload(self):
        self.print_stage('Uploading PyTPP package')
        # response = requests.get('http://spi.eng.venafi.com/spi/api/latestVersion',
        #                         params={'baseVersion': __version__})
        # response.raise_for_status()
        # last_version_pushed = response.json().get('latestMicro')
        # if last_version_pushed and Version(__version__) <= Version(last_version_pushed):
        #     print(f'FAILURE!!!\nCannot push code because its version must be greater than the micro '
        #           f'version for the relative <major>.<minor> version on the remote server.\n'
        #           f'Please update the __version__ in setup.py.')
        #     return
        sandbox.run_setup(f'{PROJECT_DIR}/setup.py', ['clean', 'sdist'])
        self.print_stage('Send Files Via SFTP')
        dist_dir = f'{PROJECT_DIR}/dist'
        files = [f for f in os.listdir(dist_dir) if f'{__version__}.tar.gz' in f]
        with self.ssh_client.open_sftp() as sftp:
            for file in files:
                sftp.put(localpath=f'{dist_dir}/{file}', remotepath=f'{REMOTE_PACKAGES_DIR}/{file}')
                print(f'{file} sent...')
        # shutil.rmtree(f'{PROJECT_DIR}/dist')
        print('Done!')


def main():
    uf = UploadFiles()
    uf.upload()


if __name__ == '__main__':
    main()
