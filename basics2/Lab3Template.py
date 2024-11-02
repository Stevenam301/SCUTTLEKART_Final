# L3_drivingPatterns.py
# Team Number: 18
# Team Names: Kristen Stubenazy & Steven Michaud
# Date:3/1/2022
# Code purpose: Run an s shaped path on the ground
# indicate d1 and d2 distances: 1m and 2m

# Import Internal Programs
import L2_speed_control as sc
import L2_inverse_kinematics as inv
import L2_log as log

# Import External programs
import numpy as np
import time

def post_lab(myVelocities0, myVelocities1):
	x_dot = myVelocities0
	theta_dot = myVelocities1
	print("x:", x_dot, "theta:", theta_dot)
	log.tmpFile(x_dot, "x_dot")
	log.tmpFile(theta_dot, "theta_dot")

def task2():
	myVelocities = np.array([.4, 0]) #input your first pair
	post_lab(myVelocities[0], myVelocities[1])
	myPhiDots = inv.convert(myVelocities)
	sc.driveOpenLoop(myPhiDots)
	time.sleep(2.5) # input your duration (s)
	
	myVelocities = np.array([0, 1.571]) #input your 2nd pair
	post_lab(myVelocities[0], myVelocities[1])
	myPhiDots = inv.convert(myVelocities)
	sc.driveOpenLoop(myPhiDots)
	time.sleep(1) # input your duration (s)
	
	myVelocities = np.array([.4, 0]) #input your 3rd pair
	post_lab(myVelocities[0], myVelocities[1])
	myPhiDots = inv.convert(myVelocities)
	sc.driveOpenLoop(myPhiDots)
	time.sleep(5) # input your duration (s)
	
	myVelocities = np.array([0, 1.571]) #input your 4th pair
	post_lab(myVelocities[0], myVelocities[1])
	myPhiDots = inv.convert(myVelocities)
	sc.driveOpenLoop(myPhiDots)
	time.sleep(1) # input your duration (s)
	
	myVelocities = np.array([.4, 0]) #input your 5th pair
	post_lab(myVelocities[0], myVelocities[1])
	myPhiDots = inv.convert(myVelocities)
	sc.driveOpenLoop(myPhiDots)
	time.sleep(2.5) # input your duration (s)
	
	myVelocities = np.array([0, -1.571]) #input your 6th pair
	myPhiDots = inv.convert(myVelocities)
	sc.driveOpenLoop(myPhiDots)
	time.sleep(1) # input your duration (s)

	myVelocities = np.array([.4, 0]) #input your 7th pair
	myPhiDots = inv.convert(myVelocities)
	sc.driveOpenLoop(myPhiDots)
	time.sleep(5) # input your duration (s)
	
	myVelocities = np.array([0, -1.571]) #input your 8th pair
	post_lab(myVelocities[0], myVelocities[1])
	myPhiDots = inv.convert(myVelocities)
	sc.driveOpenLoop(myPhiDots)
	time.sleep(1) # input your duration (s)
	
	myVelocities = np.array([.4, 0]) #input your 9th pair
	post_lab(myVelocities[0], myVelocities[1])
	myPhiDots = inv.convert(myVelocities)
	sc.driveOpenLoop(myPhiDots)
	time.sleep(2.5) # input your duration (s)
	
	myVelocities = np.array([0, 0]) #input your 10th pair
	post_lab(myVelocities[0], myVelocities[1])
	myPhiDots = inv.convert(myVelocities)
	sc.driveOpenLoop(myPhiDots)
	time.sleep(1000) # input your duration (s)
while 1:
    task2()
    time.sleep(0.2)