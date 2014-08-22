import os
from setuptools import setup

with open(os.path.join(os.path.dirname(__file__), 'README.rst')) as readme:
    README = readme.read()

# allow setup.py to be run from any path
os.chdir(os.path.normpath(os.path.join(os.path.abspath(__file__), os.pardir)))

setup(
    name='django-kss',
    version='0.1.2',
    packages=['django_kss'],
    include_package_data=True,
    license='BSD License',  # example license
    description='A simple Django app to make styleguide',
    long_description=README,
    url='https://github.com/timtan/django_kss',
    author='Tim Hsu',
    author_email='tim.yellow@gmail.com',
    install_requires = ['pykss'], 
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
