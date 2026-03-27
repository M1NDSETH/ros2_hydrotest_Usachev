#!/usr/bin/env python3
import sys

from ros2_hydrotest_interfaces.srv import AddString
import rclpy
from rclpy.node import Node


class Client(Node):

    def __init__(self):
        super().__init__('client')
        self.cli = self.create_client(AddString, 'add_string')
        while not self.cli.wait_for_service(timeout_sec=1.0):
            self.get_logger().info('service not available, waiting again...')
        self.req = AddString.Request()

    def send_request(self, word):
        self.req.word = word
        return self.cli.call_async(self.req)


def main():
    rclpy.init()

    client = Client()
    future = client.send_request(sys.argv[1])
    rclpy.spin_until_future_complete(client, future)
    response = future.result()
    client.get_logger().info(
        'Result: %d' %(response.length))
    client.destroy_node()
    rclpy.shutdown()


if __name__ == '__main__':
    main()