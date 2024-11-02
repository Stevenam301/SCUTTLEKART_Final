# made a new program called L3_gamepad_lidar_test.py, this program should 
#adapt the gamepads ability to control the robot and use the lidar to stop it if gets too close to something.

# Import Internal Programs
import L1_lidar as lidar
import L1_bmp as bmp
import L1_adc as adc
import L1_encoder as enc 
import L1_gamepad as gp
import L2_speed_control as sc
import L2_inverse_kinematics as inv
import L2_log as log
import L2_heading as head
import L2_vector as vec
#import L3_Functions as func

# Import External programs
import numpy as np
import time

def post_lab(myVelocities0, myVelocities1):
    x_dot = myVelocities0
    theta_dot = myVelocities1
    #print("x:", x_dot, "theta:", theta_dot)
	
def manual_nav():
	c = inv.getPdTargets()		#polls the gamepad for input and returns a detailed numpy array of the current state of all buttons and joysticks	
	sc.driveOpenLoop(c)		#Takes the joystick inputs from the gamepad and creates a duty cycle for both wheel motors

# if the distance is less than 0.3 meters away the robot will stop
def fail_safe():
    if (objDistance <= 0.3):
        myVelocities = np.array([0, 0]) #input your first pair
        post_lab(myVelocities[0], myVelocities[1])
        myPhiDots = inv.convert(myVelocities)
        sc.driveOpenLoop(myPhiDots)
        time.sleep(0.5) # input your duration (s)
        
def logger():
    log.tmpFile(objDistance, "distance")
    log.tmpFile(objAngle, "angle")
    log.tmpFile(dxObj, "dx")
    log.tmpFile(dyObj, "dy")
    dcJackVoltage = adc.getDcJack()
    log.tmpFile(dcJackVoltage,"DC_Jack_Voltage")
    temp = bmp.temp()
    log.tmpFile(temp,"temperature")

def CheckButton(): #update states
  global Ly, Lb, Lx
  global Color_Choice, Color_Detect, mode, Obstacle_Detect
  GpI = gp.getGP()
  if (GpI[4] == 1): #Y button toggle orange/blue "color choice"
    if (Ly == True):
      Color_Choice = not Color_Choice
      print("Color Choice toggled")
      Ly = 0
  else:
    Ly = 1
    
  if (GpI[5] == 1): #B button toggle "color detect"
    if (Lb == 1):
      Color_Detect = not Color_Detect
      print("Color Detect toggled")
      Lb = 0
  else:
    Lb = 1
    
  if (GpI[6] == 1): #A button pump raw data "mode"
    mode=1
  else:
    mode=0
    
  if (GpI[7] == 1): #X button toggle "obstacle detect"
    if (Lx == 1):
      Obstacle_Detect = not Obstacle_Detect
      print("Obstacle Detect toggled")
      Lx = 0
  else:
    Lx = 1


#global variables
d_gp_mov = np.array([0, 0])    #directional vector the gamepad controls wants
d_lidar_mov = np.array([0, 0])
d_color_mov = np.array([0, 0])
d_final_mov = np.array([0, 0])
sys_status = "setup"
# xDot = 0
# thetaDot = 0
Color_Choice = Color_Detect = mode = Obstacle_Detect = False #for CheckButton
Ly = Lb = Lx = True #for CheckButton


if __name__ == "__main__":
    print("Running L3_gamepad_lidar_test.py")
    while 1:
        #print("In loop")
        #no matter state, use, or otherwise - going to read all input
        CheckButton()                       #read from game controller face buttons buttons
        d_gp_mov = inv.populate_gp()        #translate stick positions into [xDot, ThetaDot]
        #read from LIDAR closest obstacle
        objVector = vec.getNearest()
        objDistance = objVector[0]
        objAngle = int(round(objVector[1]))
        objXY = vec.polar2cart(objVector[0], objVector[1])
        dxObj = objXY[0]
        dyObj = objXY[1]
        #TODO: read from camera HSV data

        logger()
        print("object distance:", objDistance)

        if (mode == 0): #aka free-running mode
            d_final_mov = d_gp_mov
            #IF read state- want LIDAR input? true
            #check if distance of closest object is too close
            if (int((objDistance * 100)) < 40):  #0.4 m or 40 cm
                #print("distance under 0.4m")
                if ((objAngle >= -30) & (objAngle < 30)):
                    #print("object between 0 and 30 degrees")
                    #Is driver going towards object?
                    xDotGp = d_gp_mov[0]
                    if (int((xDotGp * 100)) > 0): #if robot trying to move forward, stop it
                        d_lidar_mov = np.array([0, 0])
                        d_final_mov = d_lidar_mov;
                elif ((objAngle >= -90) & (objAngle < -30)):
                  thetaDotGp = d_gp_mov[1]
                  if ((thetaDotGp < 0) or (thetaDotGp > (-np.pi/2))): #wont accept any input
                      d_lidar_mov = np.array([0, 0])
                      d_final_mov = d_lidar_mov;
                elif ((objAngle <= 90) & (objAngle > 30)):
                  thetaDotGp = d_gp_mov[1]
                  if ((thetaDotGp > 0) or (thetaDotGp < (np.pi/2))):
                      d_lidar_mov = np.array([0, 0])
                      d_final_mov = d_lidar_mov;
                #elif() #TODO: write other angles

            #Actually finally execute movement
            x_dot = d_final_mov[0]
            theta_dot = d_final_mov[1]
            log.tmpFile(x_dot, "x_dot")
            log.tmpFile(theta_dot, "theta_dot")
            myPhiDots = inv.convert(d_final_mov)            
            sc.driveOpenLoop(myPhiDots)
        else:
            print("mode 1")
        time.sleep(0.1)
            #END IF state mode=0

        # #IF state mode = 1
        # if (distance <= 0.35):
        #     print("distance under 0.4m")
        #     #moving to avoid object to the left
        #     if ((angle >= 0) & (angle < 30)):
        #         print("object between 0 and 30 degrees")
        #         while (angle < 70):
        #             myVelocities = np.array([0, 2]) #input your first pair
        #             post_lab(myVelocities[0], myVelocities[1])
        #             myPhiDots = inv.convert(myVelocities)
        #             sc.driveOpenLoop(myPhiDots)
        #             time.sleep(2) # input your duration (s)
        #             myVector = vec.getNearest()
        #             distance = myVector[0]
        #             angle = myVector[1]
    
        #     #moving to avoid object to the right
        #     elif ((angle <= 0) & (angle > -30)):
        #         print("object between 0 and -30 degrees")
        #         while (angle > -70):
        #             myVelocities = np.array([0, -2]) #input your first pair
        #             post_lab(myVelocities[0], myVelocities[1])
        #             myPhiDots = inv.convert(myVelocities)
        #             sc.driveOpenLoop(myPhiDots)
        #             time.sleep(2) # input your duration (s)
        #             myVector = vec.getNearest()
        #             distance = myVector[0]
        #             angle = myVector[1]
          

        # if the above statement is false then the robot will run the command to use the gamepad to control the robot.
        # else:
        #     manual_nav()
        #     time.sleep(0.2)



