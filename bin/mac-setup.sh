# If you're building this for the first time,
# 0. brew install swig
# 1. virtualenv env
# 2. source env/bin/activate
# 3. pip install numpy pillow pytest
# 4. git submodule init && git submodule update

source env/bin/activate
python setup.py build_ext
python setup.py develop
py.test test/test_heman.py
