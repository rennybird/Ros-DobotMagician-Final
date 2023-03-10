#!/usr/bin/env python3
from serial.tools import list_ports
import rospy
from std_msgs.msg import String
import pydobot

available_ports = list_ports.comports()
port = available_ports[0].device
device = pydobot.Dobot(port=port, verbose=True)

def publish_position():
    # initialize node
    rospy.init_node('dobot_position_publisher', anonymous=True)

    # initialize publisher
    pub = rospy.Publisher('dobot_position', String, queue_size=10)

    # set publishing rate
    rate = rospy.Rate(5) # 5 Hz

    while not rospy.is_shutdown():
        # get dobot position
        pose = dobot._get_pose()
        x = pose[0]
        y = pose[1]
        z = pose[2]

        # create message string
        msg_str = "Dobot position: x={}, y={}, z={}".format(x, y, z)

        # publish message
        pub.publish(msg_str)

        # sleep for remainder of the publishing rate period
        rate.sleep()
