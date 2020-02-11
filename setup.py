__version__ = "19.4.0.0"

from setuptools import setup, find_packages

if __name__ == '__main__':
    setup(
        name='venafi',
        packages=find_packages(where='venafi', exclude=['docs']),
        package_dir={
          '': 'venafi'
        },
        description='Venafi Features and API Implementation In Python',
        version=__version__,
        url='ssh://git@git.eng.venafi.com/spi',
        author='Venafi',
        author_email='spi@venafi.com',
        keywords=['pip','venafi'],
        install_requires=[
            'requests',
            'datetime',
            'jsonpickle',
            'python-dateutil'
        ],
    )
