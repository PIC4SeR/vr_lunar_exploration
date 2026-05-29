import os
from glob import glob
from setuptools import setup
from setuptools import find_packages

package_name = 'rover_pic_moon_description'

setup(
    name=package_name,
    version='0.0.0',
    packages=find_packages(exclude=['test']),
    data_files=[
        ('share/ament_index/resource_index/packages', ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
        (os.path.join('share', package_name, 'launch'), glob(os.path.join('launch', '*launch.[pxy][yma]*'))),
        (os.path.join('share', package_name, 'urdf'), glob(os.path.join('urdf/', '*'))),
        (os.path.join('share', package_name, 'rviz'), glob(os.path.join('rviz/', '*'))),
        (os.path.join('share', package_name, 'meshes/stl'), glob(os.path.join('meshes/stl/', '*'))),
        (os.path.join('share', package_name, 'meshes/textures'), glob(os.path.join('meshes/textures/', '*'))),
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='giacomo',
    maintainer_email='giacomo.franchini@polito.it',
    description='TODO: Package description',
    license='Apache-2.0',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [
        ],
    },
)
