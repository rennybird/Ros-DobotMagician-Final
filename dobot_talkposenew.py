#!/usr/bin/env python3
from serial.tools import list_ports
import rospy
from std_msgs.msg import String
import pydobot

available_ports = list_ports.comports()
port = available_ports[0].device
device = pydobot.Dobot(port=port, verbose=True)
def talker():
	pub = rospy.Publisher('chatter', String, queue_size=10)
	rospy.init_node('talker', anonymous=True)
	rate = rospy.Rate(10) # 10hz
	while not rospy.is_shutdown():
		pose = pydobot.Dobot(port=port, verbose=True)
		x = pose.x
		y = pose.y
		z = pose.z
		pos_str = f"DobotPos: x={x}, y={y}, z={z}"  
		hello_str = pos_str
		rospy.loginfo(hello_str)
		pub.publish(hello_str)
		print(type(hello_str))
		rate.sleep()

if __name__ == '__main__':
    try:
        talker()
    except rospy.ROSInterruptException:
        pass
