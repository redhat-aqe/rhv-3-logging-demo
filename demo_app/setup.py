#!/usr/bin/python
from setuptools import setup, find_packages

with open('requirements.txt') as f:
    requirements = f.read().splitlines()

setup(
    name="flaskApp",
    version="0.0.2",
    author="mbirger",
    author_email="mbirger@redhat.com",
    description=("Example python app with Kafka logging"),
    license="GPLv3",
    url="https://github.com/redhat-aqe/rhv-3-logging-demo",
    package_dir={'': 'src'},
    packages=find_packages('src', exclude=('tests',)),
    test_suite='nose.collector',
    install_requires=requirements,
    entry_points={
        'console_scripts': [
            'flask-app=flaskApp.main:main',
        ]
    }
)
