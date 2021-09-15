class Histogram:
    
    def __init__(self, data, width, start = 0):
        self.data = data
        self.width = width
        
        minn = start
        maxx = start + width

        self.hist = []
        count = 0
        while maxx <= (max(data) + width):
            self.hist.append([minn, maxx, 0])
            for j in data:
                if minn <= j < maxx:
                    self.hist[count][2] += 1
            count += 1
            minn += self.width
            maxx += self.width

        self.histString = ""
        for i in range(len(self.hist)):
            self.histString += "{0:3d}-{1:3d}: ".format(self.hist[i][0], self.hist[i][1])
            # TODO add histogram scaling
            for j in range(self.hist[i][2]):
                self.histString += '*'
            self.histString += '\n'

    def out(self, char = '-'):
        print(self.histString.replace('*', char))

    def toFile(self, filename, char = '-'):
        with open(filename, 'w') as outFile:
            outFile.write(self.histString.replace('*',char))

    def getString(self, char = '-'):
        return self.histString.replace('*', char)


if __name__ == "__main__":
    test = Histogram([1,2,3,2,3,5,1,3,4,1,2,5,6,7,1,0],1)
    test.out('-')
        