# Objective : Remove all the files created after the specified date (27,5,2025)

import os
import datetime

directory = r"D:\neural slides"
thresholdDate= datetime.datetime(2025,5,27)

#loop over each file in dir
for fileName in os.listdir(directory):

    #join function to get whole path
    fullPathFile= os.path.join(directory, fileName)

    #checking if it's a file and then converting time in readable format
    if os.path.isfile(fullPathFile):
        readableCTime = datetime.datetime.fromtimestamp(os.path.getctime(fullPathFile))

        if os.path.getctime(fullPathFile) > thresholdDate.timestamp():
            os.remove(fullPathFile)
            print(f"File Name:{fileName} Creation date: {readableCTime}, Threshold Date: {thresholdDate}")





