__version__ = "0.1"

from setuptools import setup, find_packages

if __name__ == '__main__':
    setup(
        name='venafi',
        packages=find_packages(where='.', exclude=['docs']),
        # packages=find_packages(where='.', exclude=['docs', '*plugins*']), # Use this line to exclude the plugins.
        package_dir={
          '': '.'
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
