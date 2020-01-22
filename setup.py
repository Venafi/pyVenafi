from setuptools import setup, find_packages

setup(
    name='venafi',
    packages=find_packages(where='venafi', exclude=['docs']),
    package_dir={
      '': 'venafi'
    },
    description='Venafi Features and API Implementation In Python',
    version='0.1',
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
