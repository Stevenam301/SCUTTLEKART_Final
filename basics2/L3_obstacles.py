# L3_obstacles.py
# Team Number: 18
# Team Names: Kristen Stubenazy & Steven Michaud
# Date:3/10/2022
# Code purpose: Log distance and angle of nearest object
#Log dx and dy too (Lab 6)

# Import Internal Programs
import L1_lidar as lidar
import L2_vector as vec
import L2_log as log

# Import External programs
import numpy as np
import time


while 1:
    #Task 3
    myVector = vec.getNearest()
    distance = myVector[0]
    angle = myVector[1]
    log.tmpFile(distance, "distance")
    log.tmpFile(angle, "angle")
    #Task 4
    myXY = vec.polar2cart(myVector[0], myVector[1])
    dx = myXY[0]
    dy = myXY[1]
    log.tmpFile(dx, "dx")
    log.tmpFile(dy, "dy")
    time.sleep(0.2)