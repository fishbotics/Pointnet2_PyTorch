import os.path as osp

from setuptools import find_packages, setup

requirements = [
    "hydra-core>=0.11.3", 
    "pytorch-lightning>=0.7.1", 
    "numpy>=1.20.1",
    "msgpack-numpy>=0.4.7.1",
    "lmdb>=1.1.1"
    "h5py>=3.2.1",
]


exec(open(osp.join("pointnet2", "_version.py")).read())

setup(
    name="pointnet2",
    version=__version__,
    author="Erik Wijmans",
    packages=find_packages(),
    install_requires=requirements,
)
