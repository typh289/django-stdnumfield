# coding=utf-8
import os
from setuptools import setup

# allow setup.py to be run from any path
os.chdir(os.path.normpath(os.path.join(os.path.abspath(__file__), os.pardir)))


# markdown to restructured text:
try:
    import pypandoc
    description = pypandoc.convert('README.md', 'rst')
except (IOError, ImportError):
    description = ''

setup(
    name='django-stdnumfield',
    version='0.1.5',
    packages=['stdnumfield'],
    install_requires=['python-stdnum>=1.5,<1.6'],
    include_package_data=True,
    license='The Unlicense',
    description='Simple Django form and model fields for working with '
                'stdnum fields.',
    long_description=description,
    url='https://github.com/frnhr/django-stdnumfield',
    author='Fran Hrzenjak',
    author_email='fran@changeset.hr',
    classifiers=[
        'Environment :: Web Environment',
        'Framework :: Django',
        'Framework :: Django :: 1.9',
        'Framework :: Django :: 1.10',
        'Framework :: Django :: 1.11',
        'Framework :: Django :: 2.0',
        'Framework :: Django :: 2.1',
        'Intended Audience :: Developers',
        'License :: Freeware',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Topic :: Internet :: WWW/HTTP',
        'Topic :: Internet :: WWW/HTTP :: Dynamic Content',
    ],
)
