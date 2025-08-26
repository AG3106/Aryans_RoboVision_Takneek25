from launch import LaunchDescription
from launch.actions import ExecuteProcess
from launch_ros.actions import Node
import os
from ament_index_python.packages import get_package_share_directory

def generate_launch_description():
    pkg_name = 'robot_pointcloud_project'
    pkg_path = get_package_share_directory(pkg_name)

    world_file = os.path.join(pkg_path, 'worlds', 'object_world.world')
    urdf_file  = os.path.join(pkg_path, 'urdf', 'robot.urdf')

    with open(urdf_file, 'r') as infp:
        robot_desc = infp.read()

    return LaunchDescription([
        ExecuteProcess(
            cmd=['gazebo', '--verbose', world_file, '-s', 'libgazebo_ros_factory.so'],
            output='screen'),

        Node(
            package='robot_state_publisher',
            executable='robot_state_publisher',
            name='robot_state_publisher',
            output='screen',
            parameters=[{'robot_description': robot_desc}]
        ),

        Node(
            package='gazebo_ros',
            executable='spawn_entity.py',
            arguments=['-topic', 'robot_description', '-entity', 'vision_bot'],
            output='screen'
        )
    ])
