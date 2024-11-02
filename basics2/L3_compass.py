# L3_compass.py
# By Kristen Stubenazy & Steven Michaud
# Date: 2/23/2022
# Team 18
# Get the heading and cardinal direction of the robot, export to Node-RED

# Import Internal Programs
import L2_heading as head
import L2_log as log
import L1_adc as adc

# Import External programs
import numpy as np
import time

def getHeading():
    axes = head.getXY()
    axesScaled = head.scale(axes)
    h = head.getHeading(axesScaled)
    headingDegrees = round(h*180/np.pi, 2)
    return headingDegrees
    
def getCardinal(heading):
    cardinal = ""
    if -22.5 < heading < 22.5:
        cardinal = "North"
    elif 22.5 < heading < 67.5:
        cardinal = "Northwest"
    elif -67.5 < heading < -22.5:
        cardinal = "Northeast"
    elif 67.5 < heading < 112.5:
        cardinal = "West"
    elif -112.5 < heading < -67.5:
        cardinal = "East"
    elif 112.5 < heading < 157.5:
        cardinal = "Southwest"
    elif -157.5 < heading < -112.5:
        cardinal = "Southeast"
    else:
        cardinal = "South"
    return cardinal
    

# Run the main loop
if __name__ == "__main__":
    while True:
        dcJackVoltage = adc.getDcJack()
        log.tmpFile(dcJackVoltage,"DC_Jack_Voltage")
        headingDegrees = getHeading()
        cardinal = getCardinal(headingDegrees)
        print("Heading:", headingDegrees, "\t\tDirection:", cardinal)
        log.tmpFile(headingDegrees, "headingDegrees")
        log.stringTmpFile(cardinal, "cardinalDirection")
        time.sleep(0.2)
    
    # compass = heading.headingDegrees()              # call the function from within L1_mpu.py
    # print("Compass:", compass)
    # log.tmpFile(compass,"compass.txt")                       # y axis is stored in the second element
    # #axes = np.array([xAccel, yAccel])               # store just 2 axes in an array
    # log.NodeRed2(compass)                              # send the data to txt files for NodeRed to access.
    # # log.tmpFile(xAccel,"xAccel.txt")              # another way to lof data for NodeRed access
    # # log.tmpFile(yAccel,"yAccel.txt")
    # time.sleep(0.2)
