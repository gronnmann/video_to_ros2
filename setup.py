from setuptools import setup

package_name = 'video_to_ros2'

setup(
    name=package_name,
    version='0.0.1',
    packages=[package_name],
    data_files=[
        ('share/ament_index/resource_index/packages',
            ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='gronnmann',
    maintainer_email='root@todo.todo',
    description='Allows you to publish and preview video files to ROS2\'s sensor_msgs/Image',
    license='TODO: License declaration',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [
            "video_preview = video_to_ros2.video_receiver_node:main",
            "video_publisher = video_to_ros2.video_publisher_node:main"
        ],
    },
)
