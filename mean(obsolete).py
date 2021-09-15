''' WIP Statistics dataset program
Author: Nathan Vrieland '''
from datetime import datetime
from Histogram import Histogram
import math

statList = [10, 8, 6, 4, 8, 3, 2, 1, 20, 23, 1, 15, 29, 35, 2, 1, 6, 8, 23, 32, 35]

# Histogram settings
classWidth = 5
histogramStart = 0
histogramCharacter = chr(9608)

# take mean
avg = sum(statList) / len(statList)
print("mean: " + str(avg))

# take median
statList.sort()
if len(statList) % 2 == 0:
    med = (statList[(len(statList) // 2) - 1] + statList[(len(statList) // 2)]) / 2
else:
    med = statList[(len(statList) // 2)]
print("median: " + str(med))

# take mode
dic = {}
for i in statList:
    exist = False
    for j in dic:
        if i == j:
            dic[j] += 1
            exist = True
    if not exist:
        dic.update({i: 1})
mode = max(dic, key=dic.get)
if dic[mode] == 1:
    print("the mode does not exist")
else:
    print("mode: " + str(mode)) # TODO add logic for multiple modes

# take standard deviation
sumSqr = 0
for i in statList:
    sumSqr += (i - avg) ** 2
standDev = math.sqrt(sumSqr / (len(statList) - 1))
popStandDev = math.sqrt(sumSqr / len(statList))
print("sample standard deviation: " + str(standDev))
print("population standard deviation: " + str(popStandDev))

hist = Histogram(statList, classWidth, histogramStart)
hist.out(histogramCharacter)

with open("log.txt", 'w') as logFile:
    logTime = str(datetime.today())
    logFile.write(logTime.center(40, '#'))
    logFile.write('\n' + str(statList) +
                  "\nmean: " + str(avg) +
                  "\nmedian: " + str(med) +
                  "\nmode: " + str(mode) +
                  "\nsample standard deviation: " + str(standDev) +
                  "\npopulation standard deviation: " + str(popStandDev) + '\n' +
                  hist.getString(histogramCharacter))
