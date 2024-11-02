# This program continously retrieves the DC jack voltage and displays it to the terminal
# The program also logs the data to a text file located in the tmp directory

# Import Internal Programs
import L1_adc as adc
import L2_log as log

# Import External Libraries
import time

while True:
    dcJackVoltage = adc.getDcJack()                     # call the getDcJack function from within L1_adc.py
    print("DC Jack Voltage: ", dcJackVoltage)           # print the dc jack voltage to the terminal 
    log.tmpFile(dcJackVoltage,"DC_Jack_Voltage")        # log the dc jack voltage to the tmp file directory
    time.sleep(0.2)