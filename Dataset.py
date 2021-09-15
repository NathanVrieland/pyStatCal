from Histogram import Histogram
import math


class Dataset:

    def __init__(self, data, histWidth=5, histStart=0, histChar=chr(9608)):
        self.data = data
        self.mean = self.__mean()
        self.median = self.__median()
        self.mode = self.__mode()
        self.sStandDev = self.__sampleDev()
        self.pStandDev = self.__popDev()
        self.histogram = Histogram(self.data, histWidth, histStart)
        self.char = histChar

    def __mean(self):
        avg = sum(self.data) / len(self.data)
        return avg

    def __median(self):
        if len(self.data) % 2 == 0:
            med = (self.data[(len(self.data) // 2) - 1] + self.data[(len(self.data) // 2)]) / 2
        else:
            med = self.data[(len(self.data) // 2)]
        return med

    def __mode(self):
        dic = {}
        for i in self.data:
            exist = False
            for j in dic:
                if i == j:
                    dic[j] += 1
                    exist = True
            if not exist:
                dic.update({i: 1})
        mode = max(dic, key=dic.get)
        if dic[mode] == 1:
            return False
        else:
            return mode  # TODO add logic for multiple modes

    def __sampleDev(self):
        sumSqr = 0
        for i in self.data:
            sumSqr += (i - self.mean) ** 2
        standDev = math.sqrt(sumSqr / (len(self.data) - 1))
        return standDev

    def __popDev(self):
        sumSqr = 0
        for i in self.data:
            sumSqr += (i - self.mean) ** 2
        popStandDev = math.sqrt(sumSqr / len(self.data))
        return popStandDev

    def getString(self):
        return str('\n' + str(self.data) +
            "\nmean: " + str(self.mean) +
            "\nmedian: " + str(self.median) +
            "\nmode: " + str(self.mode) +
            "\nsample standard deviation: " + str(self.sStandDev) +
            "\npopulation standard deviation: " + str(self.pStandDev) + '\n' +
            self.histogram.getString(self.char))

    def getGUIString(self):
        return str("mean: " + str(self.mean) +
                   "\nmedian: " + str(self.median) +
                   "\nmode: " + str(self.mode) +
                   "\nsample standard deviation: " + str(self.sStandDev) +
                   "\npopulation standard deviation: " + str(self.pStandDev))


if __name__ == "__main__":
    statList = [10, 8, 6, 4, 8, 3, 2, 1, 20, 23, 1, 15, 29, 35, 2, 1, 6, 8, 23, 32, 35]
    test = Dataset(statList)
    print(test.getString())