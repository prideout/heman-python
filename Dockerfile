FROM ubuntu:14.04.1

MAINTAINER prideout

RUN apt-get -y update --fix-missing && apt-get install -y \
    g++ gdb software-properties-common \
    python python-setuptools python-dev python-pip scons \
    wget unzip swig

RUN apt-get install -y \
    libtiff5-dev libjpeg8-dev zlib1g-dev \
    libfreetype6-dev liblcms2-dev libwebp-dev tcl8.6-dev tk8.6-dev python-tk

RUN pip install sphinx sphinx-autobuild numpy pillow pytest pytest-cov
RUN echo "cd /home" >> /root/.bashrc
