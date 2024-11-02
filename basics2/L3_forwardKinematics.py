# L3_forwardKinematics
# By Kristen Stubenazy & Steven Michaud
# Date: 3/3/2022
# Team 18
# gets the pdl, pdr and xDot, thetaDot from L2 kinematics to print and go to Node-RED

# Import Internal Programs
import L2_log as log
import L1_adc as adc
import L2_kinematics as kin

# Import External programs
import numpy as np
import time

# Run the main loop
if __name__ == "__main__":
    while True:
        dcJackVoltage = adc.getDcJack()
        log.tmpFile(dcJackVoltage,"DC_Jack_Voltage")
        encoders = kin.getPdCurrent()
        phiL = encoders[0]
        phiR = encoders[1]
        log.tmpFile(phiL, "pdl")
        log.tmpFile(phiR, "pdr")
        velocities = kin.getMotion()
        x_dot = velocities[0]
        theta_dot = velocities[1]
        print("PDL:", phiL, "PDR:", phiR, "x:", x_dot, "theta:", theta_dot)
        log.tmpFile(x_dot, "x_dot")
        log.tmpFile(theta_dot, "theta_dot")
        time.sleep(0.2)