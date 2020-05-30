import os
import re

from setuptools import setup, find_packages

BASE_DIR = os.path.abspath(os.path.dirname(__file__))


def get_version(package: str) -> str:
    with open(os.path.join(BASE_DIR, f'{package}/__version__.py')) as version:
        version = version.readline()
    match = re.search("__version__ = ['\"]([^'\"]+)['\"]", version)
    assert match is not None
    return match.group(1)


def get_log_description():
    with open('README.md') as readme:
        with open('CHANGELOG.md') as changelog:
            return readme.read() + "\n\n" + changelog.read()


setup(
    name='bKashWebhook',
    version=get_version('bkash_webhook'),
    author='Vubon Roy',
    author_email='vubon.roy@gmail.com',
    description='This package will help to receive bKash Webhook payment payload',
    url='https://github.com/vubon/bkash-webhook',
    packages=find_packages(),
    long_description=get_log_description(),
    long_description_content_type="text/markdown",
    license='MIT',
    platforms='Python',
    install_requires=[
        'requests',
        'pyOpenSSL',
        'responses',
    ],
    classifiers=[
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Intended Audience :: Developers",
        "Programming Language :: Python :: 3 :: Only",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Environment :: Web Environment",
        "Topic :: Software Development :: Libraries :: Python Modules"
    ]
)
