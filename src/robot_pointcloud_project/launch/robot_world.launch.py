from launch import LaunchDescription
from launch.actions import ExecuteProcess
import os
from ament_index_python.packages import get_package_share_directory

def generate_launch_description():
    pkg_name = 'robot_pointcloud_project'
    pkg_path = get_package_share_directory(pkg_name)

    world_file = os.path.join(pkg_path, 'worlds', 'barrel.world')

    return LaunchDescription([
        ExecuteProcess(
            cmd=['gazebo', '--verbose', world_file],
            output='screen'
        )
    ])
