# All of these attributes are defined in _about.py, but it must be imported this way.
__project_name__ = None
__version__ = None
__author__ = None
__author_email__= None
__project_url__ = None
exec(open('pytpp/_about.py', 'r').read())

from setuptools import setup, find_packages
import os


if __name__ == '__main__':
    with open(os.path.join(os.path.dirname(__file__), 'README.md')) as f:
        long_description = f.read()

    if os.path.exists('requirements/prod.txt'):
        with open('requirements/prod.txt', 'r') as f:
            requirements = f.readlines()
    else:
        with open('requirements.txt', 'r') as f:
            requirements = f.readlines()

    setup(
        name=__project_name__,
        url=__project_url__,
        version=__version__,
        author=__author__,
        author_email=__author_email__,
        packages=find_packages(include=('pytpp*',)),
        package_dir={
            '': '.'
        },
        description='Venafi TPP Features and WebSDK API In Python',
        long_description=long_description,
        long_description_content_type='text/markdown',
        keywords=['pytpp', 'venafi', 'tpp', 'trust protection platform'],
        install_requires=requirements,
        classifiers=[
            'Development Status :: 4 - Beta',
            'Intended Audience :: Developers',
            'License :: OSI Approved :: MIT License',
            'Natural Language :: English',
            'Programming Language :: Python :: 3.8',
            'Topic :: Software Development :: Libraries :: Python Modules',
        ],
    )
