from distutils.core import setup

from astarpy.__version__ import API_VERSION

setup(
    name="astarpy",
    author="Andrew Hong",
    author_email="novialriptide@gmail.com",
    url="https://github.com/novialriptide/astarpy",
    packages=["astarpy"],
    version=str(API_VERSION),
)
