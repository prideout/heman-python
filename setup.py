from setuptools import setup, Extension
from glob import glob
import os.path
import numpy

numpyinc = os.path.join(numpy.__path__[0], 'core/include')
ext_src = glob('ext/src/*.c') + glob('ext/kazmath/*.c') + ['src/heman.i']
include_dirs = ['ext/include', 'ext', numpyinc]
gcc_args = '-fopenmp -O3 -std=c99'.split()
link_args = ['-fopenmp']

setup(
    name='heman',
    version='0.1',
    description='height map utility belt',
    author='Philip Rideout',
    scripts=['bin/heman-gen'],
    ext_modules=[Extension(
        'heman._heman',
        ext_src,
        include_dirs=include_dirs,
        extra_link_args=link_args,
        extra_compile_args=gcc_args)],
    install_requires=['Pillow', 'pytest', 'numpy'],
    package_dir={'heman': 'src'},
    packages=['heman'])
