import os
import sys
from tempfile import NamedTemporaryFile
from setuptools import sandbox
import asyncio
import asyncssh
from sphinx import make_mode


project_dir = os.path.dirname(os.path.abspath(__file__))


def gather_pip_reqs():
    print('\n>>>>>>>>>>>>> Gathering PIP requirements...\n')
    with NamedTemporaryFile(suffix='.txt', dir=os.curdir) as temp_file:
        os.system(f'pipreqs --save {temp_file.name} {project_dir}/venafi/venafi')
        new_reqs = temp_file.readlines()
        with open(os.path.abspath(f'{project_dir}/requirements.txt'), 'rb+') as req_file:
            current_reqs = req_file.readlines()
            if set(new_reqs) != set(current_reqs):
                print('\n>>>>>>>>>>>>> Updating requirements.txt file...\n')
                req_file.seek(0)
                req_file.write(b''.join(new_reqs))
                req_file.truncate()


def compile_docs():
    curdir = os.curdir
    os.chdir(f'{project_dir}/venafi/docs')
    make_mode.run_make_mode(['clean', '.', '_build'])
    make_mode.run_make_mode(['html', '.', '_build'])
    os.chdir(curdir)


async def send_files():
    print('\n>>>>>>>>>>>>> Connecting to PyPI server...\n')
    async with asyncssh.connect(host='192.168.7.239', username='root', password='Passw0rd') as conn:
        print('Uploading Venafi package...')
        await asyncssh.scp(f'{project_dir}/dist/*', (conn, f'/opt/packages'), recurse=True, preserve=True)
        print('\n>>>>>>>>>>>>> Compiling documentation...\n')
        compile_docs()
        print('Uploading documentation... (This can take a minute or two.)')
        await asyncssh.scp(f'{project_dir}/venafi/docs/_build/*', (conn, '/opt/docs'), recurse=True, preserve=True)
        print('Done!')


def main():
    gather_pip_reqs()
    sandbox.run_setup(f'{project_dir}/setup.py', ['clean', 'sdist'])
    try:
        asyncio.get_event_loop().run_until_complete(send_files())
    except (OSError, asyncssh.Error) as exc:
        sys.exit(f'\n>>>>>>>>>>>>> SSH connection failed: {str(exc)}\n')


if __name__ == '__main__':
    main()
