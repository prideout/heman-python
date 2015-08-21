from setuptools import setup

setup(
    name='heman',
    version='0.1',
    description='height map utility belt',
    author='Philip Rideout',
    scripts=['bin/heman-gen'],
    install_requires=['Pillow', 'pytest'],
    packages=['heman'])
