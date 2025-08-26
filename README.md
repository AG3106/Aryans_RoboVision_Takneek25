# RoboVision_Aryans Takneek 2025
This document provides a clear insight on how we solved this problem, has detailed instructions for setting up and running the code and a guide to repository structure and usage.

Approach: <br>
The robot is programmed to move in a perfect circle around the target object (a traffic barrel). As it moves it captures 8 images at an interval of random intervals. <br>
Feature extraction and matching- Using openCv, we have used stitcher function to stitch the multiple images into one single image. <br>
We made our own URDF file 
We tried making the robot rotate around the barrel, however we were unsuccessful and the robot could not rotate in a perfect circle.
Point cloud aggregation-
Rviz Integration and Visualization- We used Rviz to use the URDF camera to take images in sync with the Gazebo simulation.

# Instructions:-<br>
**System setup**- ubuntu 22.04<br>
ROS 2 Humble Hawksbill <br>
Dependencies- Python3.10 -Libraries -
OpenCV<br>

In terminal
### Clone the project repository
git clone <your-repo-url> PoolName_RoboVision_Takneek25
cd PoolName_RoboVision_Takneek25

### Install Python dependencies
pip install -r requirements.txt

### Build Package-
cd ~/Aryans_RoboVision_Takneek25<br>
colcon build

### Run:
In one terminal, launch your Gazebo world: `ros2 launch robot_pointcloud_project robot_world.launch.py` <br>
In a second terminal (after sourcing), run the motion node: `ros2 run robot_pointcloud_project robot_motion.py
` <br>
Use src/stiching.py to stich images