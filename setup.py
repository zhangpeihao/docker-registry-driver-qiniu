try:
    import setuptools
except ImportError:
    import distutils.core as setuptools

__author__ = 'Zhang Peihao'
__copyright__ = 'Copyright 2014'
__credits__ = []

__version__ = '0.1.17'
__maintainer__ = 'Zhang Peihao'
__email__ = 'zhangpeihao@gmail.com'

__title__ = 'docker-registry-driver-qiniu'
__build__ = 0x000000

__url__ = 'https://gitcafe.com/zhangpeihao/docker-registry-driver-qiniu'
__description__ = 'Docker registry qiniu storage driver'
__download__ = 'https://gitcafe.com/zhangpeihao/docker-registry-driver-qiniu/archiveball/master/zip'

setuptools.setup(
    name=__title__,
    version=__version__,
    author=__author__,
    author_email=__email__,
    maintainer=__maintainer__,
    maintainer_email=__email__,
    keywords='docker registry core',
    url=__url__,
    description=__description__,
    long_description=open('./README.md').read(),
    download_url=__download__,
    classifiers=['Development Status :: 4 - Beta',
                 'Intended Audience :: Developers',
                 'Programming Language :: Python',
                 'Programming Language :: Python :: 2.6',
                 'Programming Language :: Python :: 2.7',
                 # 'Programming Language :: Python :: 3.2',
                 # 'Programming Language :: Python :: 3.3',
                 'Programming Language :: Python :: 3.4',
                 'Programming Language :: Python :: Implementation :: CPython',
                 # 'Programming Language :: Python :: Implementation :: PyPy',
                 'Operating System :: OS Independent',
                 'Topic :: Utilities',
                 'License :: OSI Approved :: Apache Software License'],
    platforms=['Independent'],
    license=open('./LICENSE').read(),
    namespace_packages=['docker_registry', 'docker_registry.drivers'],
    packages=['docker_registry', 'docker_registry.drivers'],
    package_data = {'docker_registry': ['../config/*']},
    install_requires=open('./requirements.txt').read(),
    zip_safe=True,
    tests_require=open('./tests/requirements.txt').read(),
    test_suite='nose.collector'
)
