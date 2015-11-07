#!/usr/bin/env bash

docker-machine create --driver virtualbox heman --virtualbox-cpu-count "4" 2>&1
eval "$(docker-machine env heman)"
docker rm -f heman >/dev/null 2>&1
docker build -t heman .

alias heman-start="docker run -itd -v $(pwd):/home --name=heman heman bash"
alias heman-bash="docker start heman && docker attach heman"
alias heman-kill="docker rm -f heman"
alias heman-test="docker start heman && docker exec -i heman bash -c 'cd /home ; python setup.py install && py.test'"
alias heman-coverage="docker start heman && docker exec -i heman bash -c 'cd /home ; py.test --cov=heman test/test_heman.py'"
alias heman-python="docker start heman && docker exec -it heman python"
alias heman-clean="
    rm -rf build dist test/__pycache__ >/dev/null 2>&1;
    ls -1 **/*_wrap.c **/*.so | xargs rm"
alias heman-clobber="docker-machine rm -f heman >/dev/null 2>&1"

heman-clean
heman-start
heman-test
heman-coverage
