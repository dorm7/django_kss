import os
from setuptools import setup

BASE_DIR = os.path.dirname(__file__)

with open(os.path.join(BASE_DIR, 'README.rst')) as readme:
    README = readme.read()

# allow setup.py to be run from any path
os.chdir(os.path.normpath(os.path.join(os.path.abspath(__file__), os.pardir)))

setup(
    name='django-kss',
    version='0.1',
    packages=['django_kss'],
    include_package_data=True,
    license='BSD License',  # example license
    description='A simple Django app to make styleguide',
    long_description=README,
    install_requires=['pykss'],
    url='http://www.example.com/',
    author='Tim Hsu',
    author_email='tim.yellow@gmail.com',
    classifiers=[
        'Environment :: Web Environment',
        'Framework :: Django',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        # Replace these appropriately if you are stuck on Python 2.
        'Topic :: Internet :: WWW/HTTP',
        'Topic :: Internet :: WWW/HTTP :: Dynamic Content',
    ],
)
