# Copyright 2015 Open Platform for NFV Project, Inc. and its contributors
# This software is distributed under the terms and conditions of the 'Apache-2.0'
# license which can be found in the file 'LICENSE' in this package distribution
# or at 'http://www.apache.org/licenses/LICENSE-2.0'.

from setuptools import setup, find_packages
import moon_authz


setup(

    name='moon_authz',

    version=moon_authz.__version__,

    packages=find_packages(),

    author="Thomas Duval",

    author_email="thomas.duval@orange.com",

    description="",

    long_description=open('README.md').read(),

    # install_requires= ,

    include_package_data=True,

    url='https://git.opnfv.org/moon',

    classifiers=[
        "Programming Language :: Python",
        "Development Status :: 1 - Planning",
        "License :: OSI Approved",
        "Natural Language :: French",
        "Operating System :: OS Independent",
        "Programming Language :: Python :: 3",
    ],

    entry_points={
        'console_scripts': [
            'moon_authz = moon_authz.server:run',
        ],
    }

)
