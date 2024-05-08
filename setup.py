from setuptools import setup
from codecs import open
from os import path

here = path.abspath(path.dirname(__file__))

with open(path.join(here, 'README.md'), encoding='utf-8') as f:
    long_description = f.read()

setup(
    name='tooniez-timetree-sdk',
    packages=['timetree_sdk', 'timetree_sdk/models/'],
    version='0.0.1',
    license='MIT',
    install_requires=['requests'],
    author='tooniez',
    author_email='tooni22@proton.me',
    url='https://github.com/tooniez/timetree-sdk',
    description='TimeTree SDK',
    long_description=long_description,
    long_description_content_type='text/markdown',
    keywords='timetree api sdk',
    classifiers=[
        'Development Status :: 4 - Beta',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3.8',
    ],
)
