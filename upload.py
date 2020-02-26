import os
import sys
from tempfile import NamedTemporaryFile
from setuptools import sandbox
import asyncio
import asyncssh
from sphinx import make_mode
from setup import __version__


PROJECT_DIR = os.path.dirname(os.path.abspath(__file__))


def gather_pip_reqs():
    print('\n>>>>>>>>>>>>> Gathering PIP requirements...\n')
    with NamedTemporaryFile(suffix='.txt', dir=os.curdir) as temp_file:
        os.system(f'pipreqs --save {temp_file.name} {PROJECT_DIR}/venafi/venafi')
        new_reqs = temp_file.readlines()
        with open(os.path.abspath(f'{PROJECT_DIR}/requirements.txt'), 'rb+') as req_file:
            current_reqs = req_file.readlines()
            if set(new_reqs) != set(current_reqs):
                print('\n>>>>>>>>>>>>> Updating requirements.txt file...\n')
                req_file.seek(0)
                req_file.write(b''.join(new_reqs))
                req_file.truncate()
            else:
                print('\n>>>>>>>>>>>>> No changes to requirements.txt file...\n')


def compile_docs():
    curdir = os.curdir
    os.chdir(f'{PROJECT_DIR}/venafi/docs')
    make_mode.run_make_mode(['clean', '.', '_build'])
    make_mode.run_make_mode(['html', '.', '_build'])
    os.chdir(curdir)


async def send_files(src: str, dst: str):
    print('\n>>>>>>>>>>>>> Connecting to PyPI server...\n')
    async with asyncssh.connect(host='192.168.7.239', username='root', password='Passw0rd') as conn:
        async with conn.start_sftp_client() as sftp:
            print('\n>>>>>>>>>>>>> Uploading files...\n')
            await sftp.put(src, dst, recurse=True, preserve=True)
            print('Done!')


def upload(include_code: bool, include_pip: bool, include_docs: bool):
    if include_pip:
        gather_pip_reqs()
    if include_code:
        print('Uploading Venafi package...')
        sandbox.run_setup(f'{PROJECT_DIR}/setup.py', ['clean', 'sdist'])
        try:
            asyncio.get_event_loop().run_until_complete(send_files(f'{PROJECT_DIR}/dist', f'/opt/packages'))
        except (OSError, asyncssh.Error) as exc:
            sys.exit(f'\n>>>>>>>>>>>>> SSH connection failed: {str(exc)}\n')
    if include_docs:
        try:
            print('\n>>>>>>>>>>>>> Compiling documentation...\n')
            compile_docs()
            print(f'\n>>>>>>>>>>>>> Uploading documentation... (This can take a minute or two.)\n')
            asyncio.get_event_loop().run_until_complete(send_files(f'{PROJECT_DIR}/venafi/docs/_build/', f'/opt/docs/{__version__}'))
        except (OSError, asyncssh.Error) as exc:
            sys.exit(f'\n>>>>>>>>>>>>> SSH connection failed: {str(exc)}\n')


def usage():
    print(f'Usage Guide\n'
          f'-a, --all   | Recompile PIP requirements and documentation and upload everything.\n'
          f'-c, --code  | Include uploading the code.\n'
          f'-p, --pip   | Include recompiling the PIP requirements.\n'
          f'-d, --docs  | Include recompiling and uploading the documentation.\n'
          f'-h, --help  | Help.\n')


def main():
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

        upload(
            include_code=include_code,
            include_pip=include_pip,
            include_docs=include_docs
        )
    else:
        upload(
            include_code=True,
            include_pip=True,
            include_docs=True
        )


if __name__ == '__main__':
    main()
