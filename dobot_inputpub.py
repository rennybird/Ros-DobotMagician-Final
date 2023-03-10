#!/usr/bin/env python3
from serial.tools import list_ports
import rospy
from std_msgs.msg import String
import pydobot
from pynput.keyboard import Key, Listener

available_ports = list_ports.comports()
port = available_ports[0].device
device = pydobot.Dobot(port=port, verbose=True)
device.move_to(x = 199, y = 0, z = -8, r = 0, wait=True)

def on_press(key):
	(x, y, z, r, j1, j2, j3, j4) = device.pose()
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
	if key.char == ('q'):  # Q pressed +x 
		if x<=200 :
			device.move_to(x+20, y, z, r, wait=True)
		else:
			pass
	elif key.char == ('a'): # A pressed -x
		if x>=80 :
			device.move_to(x-20, y, z, r, wait=True)
		else:
			pass
	elif key.char == ('w'): # W pressed +y
		device.move_to(x, y+20, z, r, wait=True)
	elif key.char == ('s'): # S pressed -y
		device.move_to(x, y-20, z, r, wait=True)
	elif key.char == ('e'): # E pressed +z
		device.move_to(x, y, z+20, r, wait=True)
	elif key.char == ('d'): # D pressed -z
		device.move_to(x, y, z-20, r, wait=True)
	elif key.char == ('r'): # R pressed +r
		device.move_to(x, y, z, r+20, wait=True)
	elif key.char == ('f'): # F pressed -r
		device.move_to(x, y, z, r-20, wait=True)
	if key == Key.delete:
		return False
		
with Listener(on_press = on_press) as listener:
    listener.join()
    

if __name__ == '__main__':
    try:
        talker()
    except rospy.ROSInterruptException:
        pass
