# 0. brew install swig
# 1. virtualenv env
# 2. source env/bin/activate
# 3. pip install numpy pillow pytest

source env/bin/activate
python setup.py build_ext
