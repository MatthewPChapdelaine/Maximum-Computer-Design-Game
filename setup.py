#!/usr/bin/env python3
"""
Setup script for Maximum PC Builder Game
"""

from setuptools import setup, find_packages

setup(
    name='maximum-pc-builder',
    version='1.0.0',
    description='Strategic PC building RPG game for Linux',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    author='Matthew Chapdelaine',
    url='https://github.com/MatthewPChapdelaine/Maximum-Computer-Design-Game',
    packages=find_packages(),
    package_dir={'': 'src'},
    py_modules=['maximum_pc_game'],
    install_requires=[],
    entry_points={
        'console_scripts': [
            'maximum-pc-builder=maximum_pc_game:main',
        ],
    },
    classifiers=[
        'Development Status :: 4 - Beta',
        'Intended Audience :: End Users/Desktop',
        'Topic :: Games/Entertainment :: Simulation',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
        'Programming Language :: Python :: 3.10',
        'Programming Language :: Python :: 3.11',
        'Operating System :: POSIX :: Linux',
    ],
    python_requires='>=3.8',
)
