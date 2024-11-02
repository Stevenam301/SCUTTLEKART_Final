
# creating code for the lidar to stop the robot
# made a new program called L3_gamepad_lidar_test.py, this program should 
#adapt the gamepads ability to control the robot and use the lidar to stop it if gets too close to something.

# Import Internal Programs
import L1_lidar as lidar
import L1_bmp as bmp
import L1_adc as adc
import L2_speed_control as sc
import L2_inverse_kinematics as inv
import L2_log as log
import L2_heading as head
import L1_gamepad as gp #for CheckButton
import L3_gamepad_lidar_test as fd


# Import External programs
import numpy as np
import time

import L2_vector as vec
import L1_encoder as enc 


def post_lab(myVelocities0, myVelocities1):
	xDot = myVelocities0
	thetaDot = myVelocities1
	print("x:", xDot, "theta:", thetaDot)
	log.tmpFile(xDot, "x_dot")
	log.tmpFile(thetaDot, "theta_dot")
	
def manual_nav():
	c = inv.getPdTargets()		#polls the gamepad for input and returns a detailed numpy array of the current state of all buttons and joysticks	
	sc.driveOpenLoop(c)		#Takes the joystick inputs from the gamepad and creates a duty cycle for both wheel motors
  
# if the distance is less than 0.3 meters away the robot will stop
def fail_safe():
    if (distance <= 0.3):
        myVelocities = np.array([0, 0]) #input your first pair
        post_lab(myVelocities[0], myVelocities[1])
        myPhiDots = inv.convert(myVelocities)
        sc.driveOpenLoop(myPhiDots)
        time.sleep(0.5) # input your duration (s)


#def logger():
#    print("logging")
#    log.tmpFile(fd.objDistance, "distance")
#    log.tmpFile(fd.objAngle, "angle")
#    log.tmpFile(fd.dxObj, "dx")
#    log.tmpFile(fd.dyObj, "dy")
#    dcJackVoltage = adc.getDcJack()
#    log.tmpFile(dcJackVoltage,"DC_Jack_Voltage")
#    temp = bmp.temp()
#    log.tmpFile(temp,"temperature")        



if __name__ == "__main__":
  while (1):
    #declares variables
    print("In loop")


    myVector = vec.getNearest()
    distance = myVector[0]
    angle = myVector[1]
        
    myXY = vec.polar2cart(myVector[0], myVector[1])
    dx = myXY[0]
    dy = myXY[1]
    #logger()
  
    if ((int(distance *1000) <= 400)):
        print("distance under 0.4")
        #moving to avoid object to the left
        if ((angle >= 0) & (angle < 80)):

            myVector = vec.getNearest()
            distance = myVector[0]
            angle = myVector[1]

            print("object between 0 and 30 degrees")
            while ((angle >= 0) & (angle < 90)):
                print("\n\n\n\n\r (angle >= 0) & (angle < 90) ")
                myVelocities = np.array([0, -2]) #input your first pair
                post_lab(myVelocities[0], myVelocities[1])
                myPhiDots = inv.convert(myVelocities)
                sc.driveOpenLoop(myPhiDots)
                time.sleep(0.5) # input your duration (s)
                myVector = vec.getNearest()
                distance = myVector[0]
                angle = myVector[1]

                if ((int(distance * 1000 < 400)) & ((angle >= 0) & (angle < 90))):
                    myVelocities = np.array([0, 0]) #input your first pair
                    post_lab(myVelocities[0], myVelocities[1])
                    myPhiDots = inv.convert(myVelocities)
                    sc.driveOpenLoop(myPhiDots)
                    print("Im stuck in loop 1")
                    time.sleep(0.5) # input your duration (s)
                    break
                else:
                    continue




        #moving to avoid object to the right
        elif ((angle <= 0) & (angle > -80)):
            print("object between 0 and -30 degrees")
            myVector = vec.getNearest()
            distance = myVector[0]
            angle = myVector[1]



            while ((angle <= 0) & (angle > -90)):
                print("\n\n\n\n\r (angle <= 0) & (angle > -90)")
                myVelocities = np.array([0, 2]) #input your first pair
                post_lab(myVelocities[0], myVelocities[1])
                myPhiDots = inv.convert(myVelocities)
                sc.driveOpenLoop(myPhiDots)
                time.sleep(0.5) # input your duration (s)
                myVector = vec.getNearest()
                distance = myVector[0]
                angle = myVector[1]


                if (((int(distance * 1000) < 400)) & ((angle <= 0) & (angle > -90))):

                    myVelocities = np.array([0, 0]) #input your first pair
                    post_lab(myVelocities[0], myVelocities[1])
                    myPhiDots = inv.convert(myVelocities)
                    sc.driveOpenLoop(myPhiDots)
                    print("Im stuck in loop 2")
                    time.sleep(0.5) # input your duration (s)
                    break
                else:
                    continue
    # if the above statement is false then the robot will run the command to use the gamepad to control the robot.
    else:
        manual_nav()
        time.sleep(0.2)