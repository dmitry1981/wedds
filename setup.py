# Always prefer setuptools over distutils
from setuptools import setup, find_packages
# To use a consistent encoding
from codecs import open
from os import path

here = path.abspath(path.dirname(__file__))

setup(
    name='crypto-invoices-api',
    version='0.1.0',
    author='Dmitry Zhidkih',
    author_email='dzh@exante.eu',
    url='https://gitlab.exan.tech/exantech/crypto-payments-api',
    license='EULA',
    description='crypto-payments-api',
    packages=find_packages(exclude=['contrib', 'docs', 'tests']),
    include_package_data=True,
    install_requires=[
        'Django==2.2.24',
        'psycopg2-binary==2.8.4',

        'djangorestframework==3.10.3',
        'django-rest-auth==0.9.5',
        'coreapi==2.3.3',
        'django-extensions==2.2.5',

        # 'raven==6.10.0',
        'requests==2.22.0',
        # 'pyOpenSSL==19.0.0',
        'django-cors-headers==3.1.1',

        # 'uWSGI==2.0.18',
    ],

    extras_require={
        'dev': ['check-manifest'],
        'test': ['coverage'],
    },
)
