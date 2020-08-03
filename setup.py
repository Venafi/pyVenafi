__version__ = "20.2.0.2"

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
        author='Venafi',
        author_email='spi@venafi.com',
        keywords=['venafi'],
        install_requires=[
            'requests',
            'datetime',
            'jsonpickle',
            'python-dateutil',
            'isodate',
            'dblogging'
        ]
    )
