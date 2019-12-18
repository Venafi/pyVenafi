import subprocess
import os
import glob
import sys


ALL_DOCS_FOLDER = os.path.abspath('./all_docs')
if not os.path.exists(ALL_DOCS_FOLDER):
    os.mkdir(ALL_DOCS_FOLDER)
EXCLUDED_DOCS_FOLDER = os.path.abspath(os.path.join(ALL_DOCS_FOLDER, 'excluded'))
if not os.path.exists(EXCLUDED_DOCS_FOLDER):
    os.mkdir(EXCLUDED_DOCS_FOLDER)
VENAFI_FOLDER = os.path.abspath('../venafi')

EXCLUDED_DOCS = [
    'venafi.api.*.rst',
    'venafi.properties',
    'venafi.tools',
    'venafi.logger'
    'venafi.features.bases'
]


def _read_output(process):
    while True:
        output = process.stdout.readline()
        print(output.strip())
        # Do something else
        return_code = process.poll()
        if return_code is not None:
            print('RETURN CODE', return_code)
            # Process has finished, read rest of the output
            for output in process.stdout.readlines():
                print(output.strip())
            return


def main():
    proc = lambda cmd: subprocess.Popen(cmd.split(' '), stdout=subprocess.PIPE, universal_newlines=True)

    # Collect .rst files for all modules under venafi.
    apidoc = proc(f'sphinx-apidoc -e -o {ALL_DOCS_FOLDER} {VENAFI_FOLDER}')
    _read_output(apidoc)

    # Move all .rst files in EXCLUDED_DOCS to the EXCLUDED_DOCS_FOLDER so they do not appear in the documentation.
    for doc in EXCLUDED_DOCS:
        paths = glob.glob(os.path.join(ALL_DOCS_FOLDER, f'*{doc}*'))
        for path in paths:
            if os.path.exists(path):
                _, filename = os.path.split(path)
                os.rename(path, os.path.join(EXCLUDED_DOCS_FOLDER, filename))

    # Make the html documentation.
    if sys.platform == 'win32':
        make_html = proc('make.bat html')
    else:
        make_html = proc('make html')
    _read_output(make_html)


if __name__ == '__main__':
    main()
