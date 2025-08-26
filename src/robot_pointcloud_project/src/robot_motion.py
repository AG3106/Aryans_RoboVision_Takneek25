#!/usr/bin/env python3

import rclpy
from rclpy.node import Node
from geometry_msgs.msg import Twist

class CircularMotionNode(Node):
    def __init__(self):
        super().__init__('circular_motion_node')

        # Parameters
        self.declare_parameter('scanning_radius', 5.0)
        self.declare_parameter('linear_velocity', 0.5)
        self.radius = self.get_parameter('scanning_radius').get_parameter_value().double_value
        self.linear_vel = self.get_parameter('linear_velocity').get_parameter_value().double_value

        if self.radius <= 0.0:
            self.get_logger().error("Radius must be > 0. Defaulting angular velocity to 0.")
            self.angular_vel = 0.0
        else:
            self.angular_vel = self.linear_vel / self.radius

        # Publisher + timer
        self.publisher_ = self.create_publisher(Twist, '/cmd_vel', 10)
        self.timer = self.create_timer(0.1, self.move_robot)

        self.get_logger().info(
            f"Moving in a circle of radius {self.radius:.2f} m "
            f"with linear vel {self.linear_vel:.2f} m/s "
            f"and angular vel {self.angular_vel:.2f} rad/s."
        )

    def move_robot(self):
        twist = Twist()
        twist.linear.x = self.linear_vel      # forward
        twist.angular.z = self.angular_vel    # turn
        self.publisher_.publish(twist)

    def stop_robot(self):
        self.get_logger().info("Stopping the robot...")
        self.publisher_.publish(Twist())      # all zeros

def main(args=None):
    rclpy.init(args=args)
    node = CircularMotionNode()
    try:
        rclpy.spin(node)
    except KeyboardInterrupt:
        pass
    finally:
        node.stop_robot()
        node.destroy_node()
        rclpy.shutdown()

if __name__ == '__main__':
    main()
