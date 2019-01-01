import ast
import os
import re

from setuptools import setup

_version_re = re.compile(r'__version__\s+=\s+(.*)')
with open('cpyfunctional/__init__.py', 'rb') as f:
    VERSION = str(ast.literal_eval(_version_re.search(
        f.read().decode('utf-8')).group(1)))

with open(os.path.join(os.path.dirname(__file__), 'README.rst')) as page:
    README = page.read()

install_requires = [
    'typing ; python_version<"3.5"'
]

setup(
    name='Cpyfunctional',
    version=VERSION,
    url='https://github.com/3mp3ri0r/cpyfunctional/',
    license='MIT',
    author='Christoforus Surjoputro',
    author_email='cs_sanmar@yahoo.com',
    description='A python package to help you code python in functional programming paradigm.',
    long_description=README,
    packages=['cpyfunctional'],
    zip_safe=False,
    platforms='any',
    install_requires=install_requires,
    extras_require={
        'dev': ['coverage', 'mypy'],
    },
    python_requires='~=3.4',
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Environment :: Plugins',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Topic :: Software Development :: Libraries',
        'Topic :: Software Development :: Libraries :: Python Modules',
        'Topic :: Utilities'
    ]
)
