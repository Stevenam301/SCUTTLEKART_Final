# this file will let you use your gamepad to drive the SCUTTLE robot

import time					
import L2_speed_control as sc
import L2_inverse_kinematics as inv


def manual_nav():
	c = inv.getPdTargets()		#polls the gamepad for input and returns a detailed numpy array of the current state of all buttons and joysticks	
	sc.driveOpenLoop(c)		#Takes the joystick inputs from the gamepad and creates a duty cycle for both wheel motors

while 1:					#run loop infinitely
	manual_nav()			#calls the function manual_nav
	time.sleep(0.02)		#pasues for 0.2 seconds
