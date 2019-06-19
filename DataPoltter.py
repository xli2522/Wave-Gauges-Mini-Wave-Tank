
from matplotlib import pyplot as plt
import datetime
from DataADT import DataADT
time = datetime.datetime.now()
"""
    Created on May 12th 2019 by Xiyuan Li

    **Important: methods in class DataReader are designed to read specific format of .txt file.
        Log:
        Beta Version 0.2
        Modified on 18 June 2019 by Xiyuan Li
"""


dataCat = []
dataCat3 = []
dataCat4 = []
title = []
class dataPlotter(DataADT):

    def __init__(self, data):
        title.append(str(data))
        print(data)
        if str(data) == "probe1Plotter.txt":
            data = open(data, "r")
            print(data)
            for line in data:
                line = line.strip("\n")
                line = line.split(" ")
                dataCat.append(line)
                dataCat3.append(line)

        elif str(data) == "probe2Plotter.txt":
            data = open(data, "r")
            for line in data:
                line = line.strip("\n")
                line = line.split(" ")
                dataCat.append(line)
                dataCat4.append(line)

        super().__init__("", 0.0, "")
        print(dataCat)
        data.close()

    def drawVoltageTime(self):

        x = []
        y = []
        for i in dataCat:
            x.append(float(i[0]))
            y.append(float(i[2]))

        # Data for plotting

        fig, ax = plt.subplots()
        if str(title) == "['probe1Plotter.txt']":
            ax.plot(x, y)
        else:
            ax.plot(x, y, 'r')

        ax.set(xlabel='time (1/10s)', ylabel='voltage (v)',
               title='Voltage / Time' + str(title) )
        ax.grid()

        fig.savefig(str(title) + str(time) + ".png")
        dataCat.clear()
        title.clear()
        plt.show()

    def drawVTogether(self):
        a = []
        b = []
        c = []
        d = []
        for i in dataCat3:
            a.append(float(i[0]))
            b.append(float(i[2]))
        for i in dataCat4:
            c.append(float(i[0]))
            d.append(float(i[2]))

        # Data for plotting

        fig, ax = plt.subplots()

        ax.plot(a,b)
        ax.plot(c,d,"r")

        ax.set(xlabel='time (1/10s)', ylabel='voltage (v)',
               title= 'Voltage/Time  B: P1  R: P2' )
        ax.grid()

        fig.savefig("Probe1+Probe2" + str(time) + ".png")
        dataCat3.clear()
        dataCat4.clear()
        plt.show()


