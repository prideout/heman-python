from setuptools import setup, Extension
from glob import glob
import os.path
import numpy
import sys

numpyinc = os.path.join(numpy.__path__[0], 'core/include')
ext_src = glob('ext/src/*.c') + glob('ext/kazmath/*.c') + ['heman/adam.i']
include_dirs = ['ext/include', 'ext', numpyinc]
gcc_args = '-O3 -std=c99'.split()
link_args = []

if sys.platform != 'darwin':
    link_args.append('-fopenmp')
    gcc_args.append('-fopenmp')

setup(
    name='heman',
    version='0.1',
    description='height map utility belt',
    author='Philip Rideout',
    scripts=[
        'bin/heman-gen-island.py',
        'bin/heman-gen-scalloped.py'],
    ext_modules=[Extension(
        '_adam',
        ext_src,
        include_dirs=include_dirs,
        extra_link_args=link_args,
        extra_compile_args=gcc_args)],
    packages=['heman'],
    install_requires=['Pillow', 'pytest', 'numpy'])
