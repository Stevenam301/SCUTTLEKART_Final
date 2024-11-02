# L3_telemetry.py
# This program grabs data from the onboard sensors and log data in files
# for NodeRed access and integrate into a custom "flow".
# Access nodered at 192.168.8.1:1880 (by default, it's running on the Blue)

# Import Internal Programs
import L1_mpu as mpu
import L1_adc as adc
import L1_bmp as bmp
import L2_log as log

# Import External programs
import numpy as np
import time

# Run the main loop
while True:
    accel = mpu.getAccel()                          # call the function from within L1_mpu.py
    (xAccel) = accel[0]                             # x axis is stored in the first element
    (yAccel) = accel[1]                             # y axis is stored in the second element
    (zAccel) = accel[2]
    #print("x axis:", xAccel, "y axis:", yAccel)     # print the two values
    #axes = np.array([xAccel, yAccel])               # store just 2 axes in an array
    #log.NodeRed2(axes)                              # send the data to txt files for NodeRed to access.
    # log.uniqueFile(xAccel,"xAccel.txt")           # another way to log data for NodeRed access
    # log.uniqueFile(yAccel,"yAccel.txt")
    log.tmpFile(xAccel,"xAccel.txt")              # another way to log data for NodeRed access
    log.tmpFile(yAccel,"yAccel.txt")
    log.tmpFile(zAccel,"zAccel.txt")
    
    #post lab questions
    dcJackVoltage = adc.getDcJack()                     # call the getDcJack function from within L1_adc.py
    #print("DC Jack Voltage: ", dcJackVoltage)           # print the dc jack voltage to the terminal 
    log.tmpFile(dcJackVoltage,"DC_Jack_Voltage")        # log the dc jack voltage to the tmp file directory
    
    temp = bmp.temp()
    log.tmpFile(temp,"temperature.txt")
    pres = bmp.pressure()
    log.tmpFile(pres,"pressure.txt")
    al = bmp.altitude()
    log.tmpFile(al,"altitude.txt")
    time.sleep(0.2)
