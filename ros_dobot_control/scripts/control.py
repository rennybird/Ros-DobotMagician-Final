#!/usr/bin/env python3

#LIB used
from std_msgs.msg import Float32MultiArray,String
from serial.tools import list_ports
import pydobot
import rospy


#configurating Port
available_ports = list_ports.comports()
print(f'available ports: {[x.device for x in available_ports]}')
port = available_ports[0].device
device = pydobot.Dobot(port=port, verbose=True)


#Move the robot
def robotMove(dx,dy,dz):
	(x, y, z, r, j1, j2, j3, j4) = device.pose()
	device.move_to(x+dx,y+dy,z+dz,r,wait=True)

#Check key condition
def callback(data):
	KEY_GET = data.data
	rate = rospy.Rate(1)
	rospy.loginfo('Key recieve is : %s',KEY_GET)
	(x, y, z, r, j1, j2, j3, j4) = device.pose()
	if  KEY_GET == ('q'):  # Q pressed +x 
		if x<=200 :
			robotMove(20,0,0)
		else :
			pass
	elif KEY_GET == ('a'): # A pressed -x
		if x>=80 :
			robotMove(-20,0,0)
		else :
			pass
	elif KEY_GET == ('w'): # W pressed +y
		if y<=200 :
			robotMove(0,20,0)
		else :
			pass
	elif KEY_GET == ('s'): # S pressed -y
		if y>=-150 :
			robotMove(0,-20,0)
		else :
			pass
	elif KEY_GET == ('e'): # E pressed +z
		if z<=72 :
			robotMove(0,0,20)
		else :
			pass
	elif KEY_GET == ('d'): # D pressed -z
		if z>=-98 :
			robotMove(0,0,-20)
		else :
			pass
	msg = Float32MultiArray()
	(x, y, z, r, j1, j2, j3, j4) = device.pose()
	msg.data = [x,y,z,r]
	pub.publish(msg)
	rate.sleep()


rospy.init_node('dobotControl',anonymous=True)
sub = rospy.Subscriber('Input1', String, callback)
pub = rospy.Publisher('Position',Float32MultiArray,queue_size=10)
rospy.spin()



