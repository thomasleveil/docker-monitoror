#!/usr/bin/env sh
dir=$(CDPATH= cd -- "$(dirname -- "$0")" && pwd -P)
cd $dir

docker-compose -f docker-compose.test.yml build
exec docker-compose -f docker-compose.test.yml run sut