# -*- coding: utf-8 -*-
from setuptools import setup
from setuptools import find_packages


setup(
    name='sqlalchemy-postgres-autocommit',
    version='0.4.0',
    description='A library to use SQLAlchemy with PostgreSQL in an autocommit mode.',
    author='Jakub Gocławski',
    author_email='it@socialwifi.com',
    url='https://github.com/socialwifi/sqlalchemy-postgres-autocommit',
    packages=find_packages(exclude=['tests']),
    install_requires=["psycopg2", "SQLAlchemy"],
    setup_requires=['pytest-runner'],
    tests_require=['pytest'],
    license='BSD',
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Environment :: Console',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
    ]
)
