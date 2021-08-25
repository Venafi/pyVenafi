__version__ = "0.5.5"

from setuptools import setup, find_packages
import os

PROJECT_DIR = os.path.abspath(os.path.dirname(__file__))
with open(os.path.join(PROJECT_DIR, 'README.md')) as f:
    long_description = f.read()

if __name__ == '__main__':
    setup(
        name='pytpp-dev',
        packages=find_packages(where='pytpp', exclude=['docs']),
        package_dir={
            '': 'pytpp'
        },
        description='Venafi TPP Features and WebSDK API In Python',
        long_description=long_description,
        long_description_content_type='text/markdown',
        url='https://coolsolutions.venafi.com/spi/pytpp',
        version=__version__,
        author='Venafi SPI Team',
        author_email='spi@venafi.com',
        keywords=['pytpp', 'venafi', 'tpp', 'trust protection platform', 'vcert'],
        install_requires=[
            'requests',
            'datetime',
            'jsonpickle',
            'python-dateutil',
            'isodate',
            'dblogging>=1.2.1',
            'packaging'
        ],
        classifiers=[
            'Development Status :: 4 - Beta',
            'Intended Audience :: Developers',
            'License :: OSI Approved :: MIT License',
            'Natural Language :: English',
            'Programming Language :: Python :: 3.8',
            'Topic :: Software Development :: Libraries :: Python Modules',
        ]
    )
