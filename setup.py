"""
XBlock for linking to a Qualtrics survey
"""
from os import path
from setuptools import setup


version = '2.0.1'
description = __doc__.strip().split('\n')[0]
this_directory = path.abspath(path.dirname(__file__))
with open(path.join(this_directory, 'README.rst')) as file_in:
    long_description = file_in.read()

setup(
    name='xblock_qualtrics_survey',
    version=version,
    description=description,
    long_description=long_description,
    author='David Adams',
    author_email='dcadams@stanford.edu',
    url='https://github.com/Stanford-Online/xblock-qualtrics-survey',
    license='AGPL-3.0',
    packages=[
        'qualtricssurvey',
    ],
    install_requires=[
        'Django>=2.2,<3.0',
        'edx-opaque-keys',
        'mock',
        'six',
        'XBlock',
        'xblock-utils',
    ],
    entry_points={
        'cms.djangoapp': [
            'qualtricssurvey = qualtricssurvey.apps:QualtricsSurveyAppConfig'
        ],
        'lms.djangoapp': [
            'qualtricssurvey = qualtricssurvey.apps:QualtricsSurveyAppConfig'
        ],
        'xblock.v1': [
            'qualtricssurvey = qualtricssurvey.xblocks:QualtricsSurvey',
        ],
    },
    package_dir={
        'qualtricssurvey': 'qualtricssurvey',
    },
    package_data={
        "qualtricssurvey": [
            'mixins/*',
            'public/*',
            'scenarios/*.xml',
            'templates/*',
        ],
    },
    classifiers=[
        # https://pypi.python.org/pypi?%3Aaction=list_classifiers
        'Intended Audience :: Developers',
        'Intended Audience :: Education',
        'License :: OSI Approved :: GNU Affero General Public License v3',
        'Operating System :: OS Independent',
        'Programming Language :: JavaScript',
        'Programming Language :: Python',
        'Topic :: Education',
        'Topic :: Internet :: WWW/HTTP',
    ],
    test_suite='qualtricssurvey.tests',
)
