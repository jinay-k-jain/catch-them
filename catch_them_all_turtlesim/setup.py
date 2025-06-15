from setuptools import find_packages, setup

package_name = 'catch_them_all_turtlesim'

setup(
    name=package_name,
    version='0.0.0',
    packages=find_packages(exclude=['test']),
    data_files=[
        ('share/ament_index/resource_index/packages',
            ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='joy',
    maintainer_email='joy@todo.todo',
    description='TODO: Package description',
    license='TODO: License declaration',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [
            "turtle_spawner = catch_them_all_turtlesim.turtle_spawner:main",
            "turtle_controller = catch_them_all_turtlesim.turtle_controller:main"
        ],
    },
)
