# VERSION 0.2

# Latest Ubuntu LTS
from ubuntu:14.04
maintainer Zhang Peihao <zhangpeihao@gmail.com>

# Update
run apt-get update
run apt-get -y upgrade

# Install pip
run apt-get -y install python-pip

# Install deps for backports.lzma (python2 requires it)
run apt-get -y install python-dev liblzma-dev libevent1-dev

# Install docker-registry
run pip install docker-registry docker-registry-driver-qiniu

add . /docker-registry-driver-qiniu

env DOCKER_REGISTRY_CONFIG /docker-registry-driver-qiniu/config/config_qiniu.yml
env SETTINGS_FLAVOR qiniustorage

expose 5000

cmd exec docker-registry