#objective: rename all the txt files which have "Copy" in their name with "toBeDeleted"

import os
directory = r"D:\neural slides"

for fileName in os.listdir(directory):
    if fileName.endswith(".txt") and "Copy" in fileName :
        oldPath= os.path.join(directory,fileName)
        newName=fileName.replace('Copy','toBeDeleted')
        newPath = os.path.join(directory, newName)
        os.rename(oldPath,newPath)











