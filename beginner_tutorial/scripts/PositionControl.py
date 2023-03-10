#!/usr/bin/env python3
import rospy
from std_msgs.msg import String
from serial.tools import list_ports
from pynput.keyboard import Key, Listener
import pydobot

#Port control
available_ports = list_ports.comports()
print(f'available ports: {[x.device for x in available_ports]}')
port = available_ports[0].device
device = pydobot.Dobot(port=port, verbose=True)

#Reset robot to home
(x, y, z, r, j1, j2, j3, j4) = device.pose()
device.move_to(x=199, y=0, z=-8, r=0, wait=True)

def on_press(key):
	(x, y, z, r, j1, j2, j3, j4) = device.pose()
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
	

