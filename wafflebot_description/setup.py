from setuptools import find_packages, setup
import os

package_name = 'wafflebot_description'

def package_files(directory):
    paths = []
    for (path, directories, filenames) in os.walk(directory):
        for filename in filenames:
            paths.append(os.path.join(path, filename))
    return paths

setup(
    name=package_name,
    version='0.0.0',
    packages=find_packages(exclude=['test']),
    data_files=[
        ('share/ament_index/resource_index/packages',
            ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
        (os.path.join('share', package_name, 'meshes'), package_files('meshes')),
        (os.path.join('share', package_name, 'rviz'), package_files('rviz')),
        (os.path.join('share', package_name, 'urdf'), package_files('urdf')),
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='aditya',
    maintainer_email='aditya16ranjan@gmail.com',
    description='the wafflebot_description package provides URDF models and meshes for wafflebot',
    license='Apache-2.0',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [
        ],
    },
)
