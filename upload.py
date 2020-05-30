import os
import sys
from pathlib import Path
import ftplib
import asyncio
from tempfile import NamedTemporaryFile
from setuptools import sandbox
from setup import __version__


PROJECT_DIR = os.path.dirname(os.path.abspath(__file__))
MAKE_CMD = 'make' if sys.platform != 'win32' else 'make.bat'


class UploadFiles:
    def __init__(self):
        self.ftp = ftplib.FTP()
        self.ftp.connect(host='10.100.206.19', port=21)
        self.ftp.login(user=r'ftpuser', passwd='newPassw0rd!')

    @staticmethod
    def print_status(msg: str):
        print(f'\n>>>>>>>>>>>>>>>>>>>>>>>>> {msg} <<<<<<<<<<<<<<<<<<<<<<<<<\n')

    @staticmethod
    def gather_pip_reqs():
        print('Gathering PIP requirements...\n')
        with NamedTemporaryFile(suffix='.txt', dir=os.curdir) as temp_file:
            os.system(f'pipreqs --save {temp_file.name} {PROJECT_DIR}/venafi/venafi')
            new_reqs = temp_file.readlines()
            with open(os.path.abspath(f'{PROJECT_DIR}/requirements.txt'), 'rb+') as req_file:
                current_reqs = req_file.readlines()
                if set(new_reqs) != set(current_reqs):
                    print('Updating requirements.txt file...\n')
                    req_file.seek(0)
                    req_file.write(b''.join(new_reqs))
                    req_file.truncate()
                else:
                    print('\nNo changes to requirements.txt file...\n')

    @staticmethod
    def compile_docs():
        cur_dir = os.curdir
        os.chdir(f'{PROJECT_DIR}/venafi/docs')
        os.system(f'{MAKE_CMD} clean')
        os.system(f'{MAKE_CMD} html')
        os.chdir(cur_dir)

    def send_files(self, path: str, dst: str = None):
        if dst:
            self.ftp.cwd('/spi')
            parts = dst.lstrip(os.path.sep).split(os.path.sep)
            for part in parts:
                if not part in self.ftp.nlst():
                    self.ftp.mkd(part)
                self.ftp.cwd(part)

        path = Path(path)
        if path.is_dir():
            print(f'Creating directory {path.name}...')
            if path.name not in self.ftp.nlst():
                self.ftp.mkd(path.name)
            self.ftp.cwd(path.name)
            for file in os.listdir(path):
                self.send_files(path=os.path.join(path, file))
            self.ftp.cwd('../')
        elif path.is_file():
            print(f'Copying file {path.name}...')
            self.ftp.storbinary(f'STOR {path.name}', open(str(path), 'rb'))

    def upload(self, include_code: bool, include_pip: bool, include_docs: bool):
        if include_pip:
            self.gather_pip_reqs()
        if include_code:
            self.print_status('Uploading Venafi package')
            sandbox.run_setup(f'{PROJECT_DIR}/setup.py', ['clean', 'sdist'])
            self.print_status('Send Files Via FTP')
            dist_dir = f'{PROJECT_DIR}/dist'
            for file in os.listdir(dist_dir):
                self.send_files(os.path.join(dist_dir, file), f'/spi/packages')
        if include_docs:
            self.print_status('Compile Documentation')
            self.compile_docs()
            self.print_status('Upload Documentation via FTP')
            build_dir = f'{PROJECT_DIR}/venafi/docs/_build/'
            for file in os.listdir(build_dir):
                self.send_files(os.path.join(build_dir, file), f'/spi/docs/{__version__}')


def usage():
    print(f'Usage Guide\n'
          f'-a, --all   | Recompile PIP requirements and documentation and upload everything.\n'
          f'-c, --code  | Include uploading the code.\n'
          f'-p, --pip   | Include recompiling the PIP requirements.\n'
          f'-d, --docs  | Include recompiling and uploading the documentation.\n'
          f'-h, --help  | Help.\n')


def main():
    uf = UploadFiles()
    if len(sys.argv) > 1:
        include_code = False
        include_pip = False
        include_docs = False
        for opt in sys.argv[1:]:
            if opt in ('-h', '--help'):
                usage()
                sys.exit(2)
            elif opt in ('-a', '--all'):
                include_code = True
                include_pip = True
                include_docs = True
            elif opt in ('-c', '--code'):
                include_code = True
            elif opt in ('-p', '--pip'):
                include_pip = True
            elif opt in ('-d', '--docs'):
                include_docs = True
            else:
                usage()
                sys.exit(2)

        uf.upload(
            include_code=include_code,
            include_pip=include_pip,
            include_docs=include_docs
        )
    else:
        uf.upload(
            include_code=True,
            include_pip=True,
            include_docs=True
        )


if __name__ == '__main__':
    main()
