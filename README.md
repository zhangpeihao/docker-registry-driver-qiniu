# Docker registry qiniu storage driver

This is a [docker-registry backend driver][registry-core] for [Qiniu Cloud Storage][qiniu].

## Usage (recommendation)

Go to [Qiniu Cloud Storage](http://www.qiniu.com/) to get your access_key first.

Run docker-registry service by docker container

```
docker run --rm \
  -e SETTINGS_FLAVOR=qiniustorage \
  -e QINIU_BUCKET=YOUR_BUCKET \
  -e QINIU_ACCESSKEY=YOUR_ACCESSKEY \
  -e QINIU_SECRETKEY=YOUR_SECRETKEY \
  -e QINIU_DOMAIN=YOUR_BUCKET_DOMAIN \
  -p 5000:5000 \
  --name registry \
  zhangpeihao/docker-registry-qiniu
```

## Usage via pip

```
# Install pip
apt-get -y install python-pip

# Install deps for backports.lzma (python2 requires it)
apt-get -y install python-dev liblzma-dev libevent1-dev

# Install docker-registry
pip install docker-registry

# finally
pip install qiniu docker-registry-driver-qiniu

export DOCKER_REGISTRY_CONFIG=/usr/local/lib/python2.7/dist-packages/docker-registry-driver-qiniu/config/config_qiniu.yml
export SETTINGS_FLAVOR=qiniustorage

export QINIU_BUCKET=YOUR_BUCKET
export QINIU_ACCESSKEY=YOUR_ACCESSKEY
export QINIU_SECRETKEY=YOUR_SECRETKEY
export QINIU_DOMAIN=YOUR_BUCKET_DOMAIN
docker-registry
```

## Contributing

In order to verify what you did is ok, just run `pip install tox; tox`. This will run the tests
provided by [`docker-registry-core`][registry-core].

For more information, plz check [`docker-registry-readme`][registry-readme]

[registry-core]: https://github.com/dotcloud/docker-registry/tree/master/depends/docker-registry-core
[qiniu]: http://www.qiniu.com/
[registry-readme]: https://github.com/docker/docker-registry/blob/master/README.md