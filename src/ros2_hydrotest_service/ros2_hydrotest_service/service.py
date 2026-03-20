#!/usr/bin/env python3
from extra_interfaces.srv import AddString

import rclpy
from rclpy.node import Node


class Service(Node):

    def __init__(self):
        super().__init__('service')
        self.srv = self.create_service(AddString, 'add_string', self.add_two_ints_callback)

    def add_two_ints_callback(self, request, response):
        response.length = len(request.word)
        self.get_logger().info('Incoming request\nword: %s' %(request.word))

        return response


def main():
    rclpy.init()

    service = Service()

    rclpy.spin(service)

    rclpy.shutdown()


if __name__ == '__main__':
    main()