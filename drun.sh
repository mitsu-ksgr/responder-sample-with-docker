#!/bin/bash
#
# for Dockerfile testing
#

TAG="responder-firstapp:latest"

if [[ "$1" = "-b" ]]; then
    docker build -t $TAG .
fi

docker run -it --rm -v `pwd`:/app $TAG /bin/bash

