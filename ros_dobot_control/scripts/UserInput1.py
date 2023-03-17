#!/usr/bin/env python3
import rospy
from std_msgs.msg import String
from serial.tools import list_ports
from pynput.keyboard import Key, Listener

pub = rospy.Publisher('Input1',String,queue_size=10)
rospy.init_node('Input1',anonymous=True)
rate = rospy.Rate(10)

def on_press(key):
	msg = String()
	if key.char == ('q'):  # Q pressed +x 
		msg.data = 'q'
	elif key.char == ('a'): # A pressed -x
		msg.data = 'a'
	elif key.char == ('w'): # W pressed +y
		msg.data = 'w'
	elif key.char == ('s'): # S pressed -y
		msg.data = 's'
	elif key.char == ('e'): # E pressed +z
		msg.data = 'e'
	elif key.char == ('d'): # D pressed -z
		msg.data = 'd'
	pub.publish(msg)
	rospy.loginfo('%s',msg.data)
	rate.sleep()

with Listener(on_press = on_press) as listener:
	listener.join()

# pub = rospy.Publisher('Input1Sender',String,queue_size=10)
# rospy.init_node('input1Sender',anonymous=True)
# rate = rospy.Rate(100)
# while not rospy.is_shutdown():
# 	msg = String()
# 	pub.publish(msg)
# 	rate.sleep()