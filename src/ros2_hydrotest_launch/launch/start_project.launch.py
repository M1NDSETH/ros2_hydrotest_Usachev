#!/usr/bin/env python3

from launch import LaunchDescription
from launch_ros.actions import Node
from launch.actions import DeclareLaunchArgument
from launch.substitutions import LaunchConfiguration


def generate_launch_description():
    word_arg = LaunchConfiguration('word') 
    return LaunchDescription([

        DeclareLaunchArgument(
            'word',
            default_value='HYDRONAUTICS',
            description='String for client node'
        ),

        Node(
            package='ros2_hydrotest_publisher',
            executable='talker',
            name='publisher',
            output='screen',
            prefix='gnome-terminal --'
        ),

        Node(
            package='ros2_hydrotest_publisher',
            executable='listener',
            name='subscriber',
            output='screen',
            prefix='gnome-terminal --'
        ),

        Node(
            package='ros2_hydrotest_service',
            executable='service',
            name='service',
            output='screen',
            prefix='gnome-terminal --'
        ),

        Node(
            package='ros2_hydrotest_service',
            executable='client',
            name='client',
            output='screen',
            arguments=[word_arg]
        ),
    ])