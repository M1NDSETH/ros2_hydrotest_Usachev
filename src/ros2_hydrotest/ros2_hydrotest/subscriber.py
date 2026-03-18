#!/usr/bin/env python3
import rclpy
from rclpy.node import Node
from std_msgs.msg import String

class Subscriber(Node):
    def __init__(self):
        super().__init__("subscriber")
        self.subscriber = self.create_subscription(String, "hydrotest", self.listener_callback, 10)
    def listener_callback(self, msg):
        self.get_logger().info('Received: "%s"' % msg.data)

def main(args=None):
    rclpy.init(args=args)
    subscriber = Subscriber()
    
    while rclpy.ok():
        rclpy.spin_once(subscriber, timeout_sec=0.1)
    
    subscriber.destroy_node()
    rclpy.shutdown()

main()