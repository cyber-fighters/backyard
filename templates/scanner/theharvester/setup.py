#!/usr/bin/env python3
from setuptools import setup, find_packages
import os

setup(
    name = "backyard.scans.theharvester",
    version = "1.0",
    author = "GONICUS GmbH",
    author_email = "info@gonicus.de",
    description = "",

    packages = find_packages('src', exclude=['examples', 'tests']),
    package_dir={'': 'src'},
    namespace_packages = ['backyard'],

    include_package_data = True,
    package_data = {},

    zip_safe = False,

    setup_requires = [
        'pylint',
        ],
    tests_require = [
        'pytest',
    ],
    install_requires = [
        'protobuf',
        'asyncio-nats-client',
        'colorlog'
        ],

    entry_points = """
        [console_scripts]
        scanner-theharvester = backyard.scans.theharvester.__main__:main
    """,
)