## ABOUT PROJECT

This project is introducing assignment into *ROS2*. 2 types of nodes's data exchange were implemented: publisher->topic->subscriber and client<->service.

## Packages

1) *ros2_hydrotest* - contain *publisher* and *subscriber* nodes and other package's files.
    *Publisher* publishes info in format "Message N _", where _ is message number in order, into topic *"hydrotest"*. *Subscriber* subscribes on this topic and receives messages from *publisher*.
2) *ros2_hydrotest_service* - contain *service* and *client* nodes and other package's files. 
    *Client* send string to *service* and *service* return to *client* number of characters in received string.
    (Example: Request: Hydronautics; Response: 12 )
3) *extra_interfaces* - contain custom interface for *client*<->*service* data exchange in *.srv* file and others package's files.

