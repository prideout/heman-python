FROM ubuntu:14.04.1

MAINTAINER prideout

RUN apt-get -y update --fix-missing && apt-get install -y \
    g++ gdb software-properties-common \
    python python-setuptools python-dev python-pip scons \
    wget unzip swig

RUN pip install sphinx sphinx-autobuild numpy pillow pytest
RUN echo "cd /heman" >> /root/.bashrc
