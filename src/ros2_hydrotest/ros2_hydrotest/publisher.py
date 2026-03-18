#!/usr/bin/env python3
import rclpy
from rclpy.node import Node
from std_msgs.msg import String

class Publisher(Node):
    def __init__(self):
        super().__init__("publisher")
        self.publisher_=self.create_publisher(String,"hydrotest",10)
        period=0,5
        self.timer=self.create_timer(period, self.timer_callback)
        self.counter=0
    def timer_callback(self):
        msg=String
        msg.data="Message N %d" % self.counter
        self.publisher_.publish(msg)
        self.get_logger().info('Publishing: "%s"' % msg.data)
        self.counter+=1
def main(args=None):
    rclpy.init(args=args)
    publisher=Publisher
    rclpy.spin(publisher)
    publisher.destroy_node
    rclpy.shutdown
main()

    
