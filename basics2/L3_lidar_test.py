
# creating code for the lidar to stop the robot


# Import Internal Programs
import L1_lidar as lidar
import L2_speed_control as sc
import L2_inverse_kinematics as inv
import L2_log as log

# Import External programs
import numpy as np
import time

import L2_vector as vec
import L1_encoder as enc 

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
	time.sleep(0.5) # input your duration (s)
	



print("Started")
while 1:
    #declares variables
    print("In loop")

    myVector = vec.getNearest()
    distance = myVector[0]
    angle = myVector[1]
    log.tmpFile(distance, "distance")
    log.tmpFile(angle, "angle")
        
        
    myXY = vec.polar2cart(myVector[0], myVector[1])
    dx = myXY[0]
    dy = myXY[1]
    log.tmpFile(dx, "dx")
    log.tmpFile(dy, "dy")


    if (distance <= 0.2):
        myVelocities = np.array([0, 0]) #input your first pair
        post_lab(myVelocities[0], myVelocities[1])
        myPhiDots = inv.convert(myVelocities)
        sc.driveOpenLoop(myPhiDots)
        time.sleep(0.5) # input your duration (s)

    else:
        task2()
        time.sleep(0.2)



