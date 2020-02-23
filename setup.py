import os
from setuptools import setup

here = os.path.abspath(os.path.dirname(__file__))
README = open(os.path.join(here, 'README.rst')).read()

setup(
    name='bkash-webhook',
    version='0.1',
    packages=['bkash_webhook'],
    description='This package will help to receive bKash Webhook payment payload',
    long_description=README,
    long_description_content_type='text/x-rst',
    author='Vubon Roy',
    author_email='vubon.roy@gmail.com',
    url='https://github.com/vubon/bkash-webhook',
    license='MIT',
    platforms='Python',
    install_requires=[
        'requests',
        'pyOpenSSL',
    ]
)
