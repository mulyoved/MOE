# -*- coding: utf-8 -*-
"""Setup for the MOE webapp."""
import os
import shlex
import shutil
import subprocess
import sys
import warnings
from collections import namedtuple

from setuptools import setup, find_packages
from setuptools.command.install import install

try:
    import sysconfig
except ImportError:
    from distutils import sysconfig


here = os.path.abspath(os.path.dirname(__file__))
README = open(os.path.join(here, 'README.md')).read()


CLASSIFIERS = [
        'Development Status :: 4 - Beta',
        'Intended Audience :: Science/Research',
        'Intended Audience :: Developers',
        'Programming Language :: Python',
        'Topic :: Software Development',
        'Topic :: Scientific/Engineering',
        'Operating System :: Unix',
        'Operating System :: MacOS'
        ]


# If you change something here, change it in requirements.txt
requires = [
    'simplejson',
    'numpy',
    'colander',
    ]


MoeExecutable = namedtuple('MoeExecutable', ['env_var', 'exe_name'])


setup(name='clientMOE',
      version='0.1',
      description='Client API for MOE (Metric Optimization Engine)',
      long_description=README,
      classifiers=CLASSIFIERS,
      author="Scott Clark and Eric Liu",
      author_email='mulyoved@gmail.com',
      url='https://github.com/mulyoved/clientMOE',
      keywords='bayesian global optimization optimal learning expected improvement experiment design',
      packages=find_packages(),
      include_package_data=True,
      zip_safe=False,
      install_requires=requires,
      )
