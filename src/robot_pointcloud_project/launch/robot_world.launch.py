# from launch import LaunchDescription
# from launch.actions import ExecuteProcess
# import os
# from ament_index_python.packages import get_package_share_directory

# def generate_launch_description():
#     pkg_name = 'robot_pointcloud_project'
#     pkg_path = get_package_share_directory(pkg_name)

#     world_file = os.path.join(pkg_path, 'worlds', 'barrel.world')

#     return LaunchDescription([
#         ExecuteProcess(
#             cmd=['gazebo', '--verbose', world_file],
#             output='screen'
#         )
#     ])

from launch import LaunchDescription
from launch.actions import IncludeLaunchDescription, ExecuteProcess
from launch.launch_description_sources import PythonLaunchDescriptionSource
from launch_ros.actions import Node
from launch.substitutions import PathJoinSubstitution
from launch_ros.substitutions import FindPackageShare
import os

def generate_launch_description():
    pkg_share = FindPackageShare('robot_pointcloud_project').find('robot_pointcloud_project')

    world_file = os.path.join(pkg_share, 'worlds', 'barrel.world')
    xacro_file = os.path.join(pkg_share, 'urdf', 'myrobot.xacro')
    urdf_file = os.path.join(pkg_share, 'urdf', 'myrobot.urdf')

    # Convert xacro → urdf
    xacro_to_urdf = ExecuteProcess(
        cmd=['xacro', xacro_file, '-o', urdf_file],
        output='screen'
    )

    return LaunchDescription([
        # Convert xacro
        xacro_to_urdf,

        # Launch Gazebo
        IncludeLaunchDescription(
            PythonLaunchDescriptionSource(
                [FindPackageShare('gazebo_ros'), '/launch/gazebo.launch.py']
            ),
            launch_arguments={'world': world_file}.items(),
        ),

        # Robot State Publisher
        Node(
            package='robot_state_publisher',
            executable='robot_state_publisher',
            output='screen',
            parameters=[{'use_sim_time': True}],
            arguments=[urdf_file]
        ),

        # Spawn robot in Gazebo
        Node(
            package='gazebo_ros',
            executable='spawn_entity.py',
            arguments=['-entity', 'vision_bot', '-file', urdf_file],
            output='screen'
        ),
    ])
