[![Docker Cloud Automated build](https://img.shields.io/docker/cloud/automated/tomdesinto/monitoror)](https://hub.docker.com/r/tomdesinto/monitoror/builds)
[![Docker Pulls](https://img.shields.io/docker/pulls/tomdesinto/monitoror)
![Docker Image Version (latest semver)](https://img.shields.io/docker/v/tomdesinto/monitoror?sort=semver)](https://hub.docker.com/r/tomdesinto/monitoror/tags)

Unofficial Docker image for Monitoror
=====================================

[![][LOGO]](https://monitoror.com)

Monitoror is a unified monitoring wallboard.

> Light, ergonomic and reliable monitoring for anything, because you deserve dependable and clean wallboard.

See https://monitoror.com/

Usage
-----

```bash
docker run --name monitoror -d -p 8080:8080 tomdesinto/monitoror
```

Build
-----

```bash
docker build -t monitoror https://raw.githubusercontent.com/thomasleveil/docker-monitoror/master/Dockerfile
```

To specify a different [version of Monitoror](https://github.com/monitoror/monitoror/releases) :

```bash
docker build \
    -t monitoror:3.1.0 \
    --build-arg MONITOROR_VERSION=3.1.0 \
    https://raw.githubusercontent.com/thomasleveil/docker-monitoror/master/Dockerfile
```


[LOGO]: https://github.com/thomasleveil/docker-monitoror/raw/master/monitoror-logo.png
