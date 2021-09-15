from Dataset import Dataset
from datetime import datetime
# enter dataset here
statList = [20,24,27,28,29,30,32,33,34,36,38,39,40,40]
# histogram settings
classWidth = 3
startPoint = min(statList)

com = Dataset(statList, classWidth, startPoint) # compute data XD
print(com.getString()) # output dat computed data

# save that computed data
with open("log.txt", 'w') as logFile:
    logFile.write(str(datetime.today()).center(40, '#'))
    logFile.write(com.getString())