#!/usr/bin/env bash

boot2docker up
eval "$(boot2docker shellinit)"
docker rm -f heman >/dev/null 2>&1
docker build -t heman .

alias heman-start="docker run -itd -v $(pwd):/home --name=heman heman bash"
alias heman-bash="docker start heman && docker attach heman"
alias heman-kill="docker rm -f heman"
alias heman-test="docker start heman && docker exec -i heman bash -c 'cd /home ; python setup.py install && py.test'"
alias heman-python="docker start heman && docker exec -it heman python"
alias heman-clean="
    rm -rf build dist test/__pycache__ >/dev/null 2>&1;
    ls -1 **/*_wrap.c **/*.so **/heman.py | xargs rm"

heman-clean
heman-start
heman-test
