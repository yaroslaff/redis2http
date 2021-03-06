#!/usr/bin/env python3

import os
from setuptools import setup


def read(filename):
    return open(os.path.join(os.path.dirname(__file__), filename)).read()


setup(
    name='redis2http',
    version='0.0.2',
    scripts=['redis2http.py'],

    # install_requires=[],

    url='https://github.com/yaroslaff/redis2http',
    license='MIT',
    author='Yaroslav Polyakov',
    long_description=read('README.md'),
    long_description_content_type='text/markdown',
    author_email='yaroslaff@gmail.com',
    description='Simple HTTP client which takes request data from redis',
    install_requires=[
        'redis',
        'requests',
    ],
    data_files=[
        ('redis2http', ['contrib/redis2http.service']),
    ],

    python_requires='>=3',
    classifiers=[
        'Development Status :: 3 - Alpha',

        # Indicate who your project is intended for
        'Intended Audience :: Developers',
        'Operating System :: OS Independent',
        'Programming Language :: Python',        
        # Pick your license as you wish (should match "license" above)
        'License :: OSI Approved :: MIT License',
        # Specify the Python versions you support here. In particular, ensure
        # that you indicate whether you support Python 2, Python 3 or both.
        # 'Programming Language :: Python :: 3.4',
    ]
)
