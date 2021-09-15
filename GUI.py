import tkinter as tk
from Dataset import Dataset
from datetime import datetime


class GUI:

    def __init__(self, window):
        self.window = window
        self.window.title("Stat Program")
        self.binLabel = tk.Label(text="bin Width")
        self.startLabel = tk.Label(text="start point")
        self.startLabel.grid(row=2, column=0)
        self.binLabel.grid(row=2, column=1)

        self.binWidth = tk.StringVar()
        self.histStart = tk.StringVar()
        self.binIn = tk.Entry(textvariable=self.binWidth)
        self.startIn = tk.Entry(textvariable=self.histStart)
        self.startIn.grid(row=3, column=0)
        self.binIn.grid(row=3, column=1)
        self.startIn.insert(0,"0")
        self.binIn.insert(0,"5")

        self.data = tk.StringVar()
        self.pyin = tk.Entry(textvariable=self.data)
        self.pyin.grid(row=0, columnspan=2)
        self.out = None

        self.combutton = tk.Button(text='compute', command=self.compute)
        self.combutton.grid(row=1, columnspan=2)

        self.dataset = None

        self.window.mainloop()

    def compute(self):
        datastr = self.data.get()
        dataset = datastr.split(',')
        for i in range(len(dataset)):
            dataset[i] = float(dataset[i])
        self.dataset = Dataset(dataset, int(self.binWidth.get()), int(self.histStart.get()))
        print(self.dataset.getString())
        self.out = tk.Label(text=self.dataset.getGUIString(), anchor='w')
        self.out.grid(row=4, columnspan=2)
        self.save()

    def save(self):
        with open("log.txt", 'w') as logFile:
            logFile.write(str(datetime.today()).center(40, '#'))
            logFile.write(self.dataset.getString())

if __name__ == "__main__":
    root = tk.Tk()
    app = GUI(root)