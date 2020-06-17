import os
import sys
from pathlib import Path
import ftplib
from tempfile import NamedTemporaryFile
from setuptools import sandbox
from setup import __version__
import threading
from typing import List


PROJECT_DIR = os.path.dirname(os.path.abspath(__file__))
MAKE_CMD = 'make' if sys.platform != 'win32' else 'make.bat'
THREADS = []  # type: List[threading.Thread]


def fire_and_forget(f):
    def wrapped(*args, **kwargs):
        thread = threading.Thread(target=f, args=args, kwargs=kwargs)
        THREADS.append(thread)
        thread.start()
    return wrapped


class UploadFiles:
    def __init__(self):
        self.host = '10.100.203.5'
        self.port = 21
        self.username = 'ftpuser'
        self.password = 'newPassw0rd!'

        self.ftp = ftplib.FTP()
        self.ftp.connect(host=self.host, port=self.port)
        self.ftp.login(user=self.username, passwd=self.password)

    def __del__(self):
        for thread in THREADS:
            if thread.is_alive():
                print(f'Waiting for {thread.name} to finish...')
                thread.join()

    @staticmethod
    def print_stage(msg: str):
        print(f'\n>>>>>>>>>>>>>>>>>>>>>>>>> {msg} <<<<<<<<<<<<<<<<<<<<<<<<<\n')

    @staticmethod
    def print_step(msg: str):
        print(f'{msg}{" " * 50}', end='\r', flush=True)

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

    @fire_and_forget
    def _send_file(self, src: Path, dst: str):
        with ftplib.FTP(host=self.host, user=self.username, passwd=self.password) as ftp:
            ftp.cwd(dst)
            ftp.storbinary(f'STOR {src.name}', open(str(src), 'rb'))

    def send_files(self, src: str, dst: str):
        files = []
        try:
            self.ftp.cwd(dst)
        except:
            self.ftp.cwd('/')
            parts = dst.lstrip(os.path.sep).split(os.path.sep)
            for part in parts:
                if not part in self.ftp.nlst():
                    self.ftp.mkd(part)
                self.ftp.cwd(part)
        for file in os.listdir(src):
            path = os.path.join(src, file)
            if os.path.isdir(path):
                if file not in self.ftp.nlst():
                    self.ftp.mkd(file)
                self.send_files(src=path, dst=f'{dst}/{file}')
                self.ftp.cwd('../')
            elif os.path.isfile(path):
                files.append(path)

        for file in files:
            file = Path(file)
            self.print_step(f'Copying file: \033[94m{file.name}\033[0m')
            self._send_file(src=file, dst=dst)

    def upload(self, include_code: bool, include_pip: bool, include_docs: bool):
        if include_pip:
            self.gather_pip_reqs()
        if include_code:
            self.print_stage('Uploading Venafi package')
            sandbox.run_setup(f'{PROJECT_DIR}/setup.py', ['clean', 'sdist'])
            self.print_stage('Send Files Via FTP')
            dist_dir = f'{PROJECT_DIR}/dist'
            self.send_files(dist_dir, f'/spi/packages')
        if include_docs:
            self.print_stage('Compile Documentation')
            self.compile_docs()
            self.print_stage('Upload Documentation via FTP')
            build_dir = f'{PROJECT_DIR}/venafi/docs/_build/'
            self.send_files(build_dir, f'/spi/docs/{__version__}')


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
