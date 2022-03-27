from distutils.core import setup

from astarpy.__version__ import API_VERSION

setup(
    name="astarpy",
    author="Andrew Hong",
    author_email="novialriptide@gmail.com",
    url="https://github.com/novialriptide/pygame_pathfinding",
    packages=["pygame_pathfinding"],
    version=str(API_VERSION),
)
