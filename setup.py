__version__ = "20.1.0.0"

from setuptools import setup, find_packages

if __name__ == '__main__':
    setup(
        name='venafi',
        packages=find_packages(where='venafi', exclude=['docs']),
        package_dir={
          '': 'venafi'
        },
        package_data={'': [
            'tools/logger/generators/html_gen/*.js',
            'tools/logger/generators/html_gen/*.css',
            'tools/logger/sqlite/*.sql'
        ]},
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
            'Pygments'
        ]
    )
