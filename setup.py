# Copyright (C) 2020-2022 by Vd.
# This file is part of BetterLogging, my logging improvement.
# BetterLogging is released under the MIT License (see LICENSE).


from os.path import join, dirname

import setuptools

setuptools.setup(
    name='betterlogging',
    version='0.1.0',
    author='Vd',
    author_email='vd@vd2.org',
    url='https://github.com/vd2org/betterlogging',
    license='MIT',
    description='My logging improvement',
    long_description=open(join(dirname(__file__), 'README.md')).read(),
    long_description_content_type='text/markdown',
    packages=setuptools.find_packages(),
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Intended Audience :: Developers',
        'Intended Audience :: Education',
        'Intended Audience :: Information Technology',
        'License :: OSI Approved :: MIT License',
        'Natural Language :: English',
        'Operating System :: OS Independent',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
        'Programming Language :: Python :: 3.10',
        'Programming Language :: Python :: 3 :: Only',
        'Topic :: Utilities',
        'Topic :: Software Development',
        'Topic :: Software Development :: Libraries',
        'Topic :: Software Development :: Libraries :: Python Modules',
    ],
)
