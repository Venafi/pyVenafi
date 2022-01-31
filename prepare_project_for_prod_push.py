#!/usr/bin/env python

import os
import shutil


IGNORED_FILES = [
    'upload.py',
    'update_attributes',
    '.readthedocs.yaml',
]

IGNORED_DIRECTORIES = [
    'pytpp/plugins',
    'docs',
    'requirements'
]


def main():
    # Alter requirements
    with open('requirements.txt', 'w') as f:
        with open('requirements/prod.txt', 'r') as p:
            reqs = p.read()
        f.write(reqs)

    for file in IGNORED_FILES:
        if os.path.exists(file) and os.path.isfile(file):
            os.remove(file)

    for directory in IGNORED_DIRECTORIES:
        if os.path.exists(directory) and os.path.isdir(directory):
            shutil.rmtree(str(directory))



if __name__ == '__main__':
    main()

