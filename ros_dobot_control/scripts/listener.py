#!/usr/bin/env python3
import rospy
from std_msgs.msg import Float32MultiArray

def callback(data):
	PosArray = data.data
	rospy.loginfo('data recieved with length : %d',len(PosArray))
	rospy.loginfo('x = %f',PosArray[0])
	rospy.loginfo('y = %f',PosArray[1])
	rospy.loginfo('z = %f',PosArray[2])
	rospy.loginfo('r = %f',PosArray[3])
def listener():
	rospy.init_node('Position_Reader', anonymous=True)
	rospy.Subscriber('Position', Float32MultiArray, callback)
	rospy.spin()

if __name__ == '__main__':
	listener()
