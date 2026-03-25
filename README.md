## ABOUT PROJECT

This project is introducing assignment into *ROS2*, version *Humble*. 2 types of nodes's data exchange were implemented: publisher->topic->subscriber and client<->service.

## PACKAGES

1) *extra_interfaces* - contain custom interface for *client*<->*service* data exchange in *.srv* file and others package's files.

2) *ros2_hydrotest* - contain *publisher* and *subscriber* nodes and other package's files.
    *Publisher* publishes info in format "Message N _", where _ is message number in order, into topic *"hydrotest"*. *Subscriber* subscribes on this topic and receives messages from *publisher*.

3) *ros2_hydrotest_launch* - this package launches full project.

4) *ros2_hydrotest_service* - contain *service* and *client* nodes and other package's files. 
    *Client* send string to *service* and *service* return to *client* number of characters in received string.
    (Example: Request: Hydronautics; Response: 12 )

## INSTALLATION

### LINUX

You need to have installed *ROS2 HUMBLE* on your device. Source ROS2 and copy this repository to foulder *src/* of your project workspace. Then use command *colcon build* in root of workspace to build packages. 

## LAUNCH

### LINUX

Source ROS2 and your workspace with command *source install/setup.bash* in root of workspace. Then launch project with command *ros2 launch ros2_hydrotest_launch start_project.launch.py word:= __* . Use your string what you want client to send to service instead of __ . You will see 3 new terminals: with publisher, with subscriber and with service. Responce of service you will see in terminal where you have launched project.

### !!! 

If you have not *gnome-terminal* terminal you have to change lines *prefix='gnome-terminal --'* in file *start_project.launch.py* in package *ros2_hydrotest_launch*
