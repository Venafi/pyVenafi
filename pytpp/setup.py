__version__ = "0.1"

from setuptools import setup, find_packages

if __name__ == '__main__':
    setup(
        name='pytpp',
        packages=find_packages(where='.', exclude=['docs']),
        # packages=find_packages(where='.', exclude=['docs', '*plugins*']), # Use this line to exclude the plugins.
        package_dir={
          '': '.'
        },
        description='Venafi TPP Features and WebSDK API In Python',
        version=__version__,
        author='Venafi SPI Team',
        author_email='spi@pytpp.com',
        keywords=['pytpp'],
        install_requires=[
            'requests',
            'datetime',
            'jsonpickle',
            'python-dateutil',
            'isodate',
            'dblogging'
        ]
    )
