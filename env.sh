#!/usr/bin/env bash

rm -rf build dist *_wrap.c >/dev/null 2>&1
boot2docker up
eval "$(boot2docker shellinit)"
docker rm -f heman >/dev/null 2>&1
docker build -t heman .

alias heman-start="docker run -itd -v $(pwd):/heman --name=heman heman bash"
alias heman-bash="docker start heman && docker attach heman"
alias heman-kill="docker rm -f heman"
alias heman-test="docker start heman && docker exec -i heman bash -c 'cd /heman ; python setup.py develop && py.test'"
alias heman-python="docker start heman && docker exec -it heman bash -c 'cd /home ; python'"

heman-start
heman-test
