from matplotlib import pyplot as plt
import datetime
time = datetime.datetime.now()

"""
    Created on May 12th 2019 by Xiyuan Li
    **Important: methods in class DataReader are designed to read specific format of .txt file.
        Log:
        Beta Version 0.2.1
        Modified on 24 June 2019 by Xiyuan Li
"""

class DataADT:

    ##Variables need to be changed accordingly
    #each time before use.
    #IMPORTANT

    variable1 = 2.0
    variable2 = 1.0

    def __init__(self, time, voltage, s_signal):
        self._time = time
        self._voltage = voltage
        self._s_signal = s_signal
        """
           Wave height function needs verification.
           ********** IMPORTANT FIX
           """
        self._height = 2
            #"%.2f" % int(voltage * (self.variable1 / self.variable2))

    '''
           time: time stamp
           voltage: voltage detected by analog input
           value: wave height computed by Arduino program
           s_signal: signal source signature when multiple sensors are used
    '''

    '''
    **Do not recommend using the following setter methods to manipulate data (except when logging data) 
    as they could affect the outcome. 
    
    '''
    def setTime(self, time):
        self._time = time

    def setVoltage(self, voltage):
        self._voltage = voltage

    def setSignal(self, s_signal):
        self._s_signal = s_signal

    def setHeight(self, height):
        self._height = height

    '''
    Getter methods
    '''

    def getTime(self):
        return self._time

    def getVoltage(self):
        return self._voltage

    def getSignal(self):
        return self._s_signal

    def getHeight(self):
        return self._height

    def __repr__(self):
        print("Time:", self.getTime(), ",", "Voltage", self.getVoltage(),
              ",", "Source:", self.getSignal(), ",", "Height", self.getHeight())

########################DataReader##########################
dataCat1 = []
dataCat2 = []

class dataReader(DataADT):


    def __init__(self, data):   # initialize data
        data = open(data, "r")

        for line in data:
            line = line.strip("\n")
            line = line.split(" ")
            if str(line[3]) == "sensor1":
                dataCat1.append(line)
            elif str(line[3]) == "sensor2":
                dataCat2.append(line)


        super().__init__("", 0.0, "")
        self.conversion10(dataCat1)
        self.conversion10(dataCat2)

        data.close()


    '''def valiSource(self, SourceSignature): # find if a sensor exist
        for item in dataCat:
            if item[2] == SourceSignature:
                print("Sensor", item[2], "found")
                return
            else:
                continue
        print("Sensor information not found.")
        return'''

    def getTimeList(self, dataCat):

        for item in dataCat:
            print(item[0])

        return

    def conversion10(self, dataCat):
        for item in dataCat:
            item[2] = "%.2f" % float(int(item[2])*5/1023)
        return

    def deleteTimeBefore(self, timeStamp, dataCat):
        count = -1
        for item in dataCat:
            count = count + 1
            if item[0] == timeStamp:
                i = 0
                print("Time stamp found.")
                while i < count:
                    dataCat.pop(0)
                    i = i + 1

                print("Deleted", i, "data item from" + str(dataCat))
                return
            else:
                continue

        print("Time not found.")
        return

    def deleteTimeAfter(self, timeStamp, dataCat):
        count = -1
        for item in dataCat:
            count = count + 1
            if item[0] == timeStamp:
                print("Time stamp found.")
                i = 0
                length = len(dataCat)
                while count < length - 1:
                    dataCat.pop()
                    count = count + 1
                    i = i + 1
                print("Deleted", i, "data item from" + str(dataCat))
                return
            else:
                continue

        print("Time not found.")
        return


    def printDataCatalogue(self, dataCat):
        print(dataCat)
        for item in dataCat:
            super().__init__(item[0],item[2],str(dataCat))
            super().__repr__()

    def saveDataCatalogue(self, file, dataCat):


        try:
            savefile = open(file, "w+")
            count = 0
            saveDataCatalogue = "Western University Physics and Astronomy \n" + \
                                "Generated at:" + str(datetime.datetime.now()) + "\n" + \
                                "Wave tank data log \n"

            savefile.write(saveDataCatalogue)

            for i in dataCat:
                height = i[2]
                savefile.write("Time Stamp: " + i[0] + " " + "Voltage: " +
                                i[2] + " " + "Height: " + height + "\n")

                count = count + 1

            return count

        except Exception:
            return -1

        finally:
            savefile.close()



    def saveForPlotter(self, file, dataCat):

        try:
            savefile = open(file, "w")
            count = 0

            for i in dataCat:
                height = i[2]
                time = str(count*0.1)
                savefile.write(time + " " + i[2] + " " + height + "\n")
                count = count + 1

            return count
        except Exception:
            return -1

        finally:
            savefile.close()

#########################DataPlotter##############################
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
        
def main():
    print()
    #print("Look up sensor information")
    #sensorSig = input("Enter the file title. (Sensor signature)")

    cc = dataReader("data_Arduino_output.txt")
    # Save your data to this .txt file


    #cc.valiSource(sensorSig)
    cc.getTimeList(dataCat1)
    cc.getTimeList(dataCat2)
    #cc.printDataCatalogue(dataCat1)
    #cc.printDataCatalogue(dataCat2)
    #cc.deleteTimeBefore("14:05:46.020", dataCat1)
    #cc.deleteTimeAfter("14:06:00.731", dataCat2)
    cc.saveDataCatalogue("probe1Data.txt", dataCat1)
    cc.saveForPlotter("probe1Plotter.txt", dataCat1)
    cc.saveDataCatalogue("probe2Data.txt", dataCat2)
    cc.saveForPlotter("probe2Plotter.txt", dataCat2)

    #cc.printDataCatalogue()

    dp1 = dataPlotter("probe1Plotter.txt")
    dp1.drawVoltageTime()

    dp2 = dataPlotter("probe2Plotter.txt")
    dp2.drawVoltageTime()

    dp2.drawVTogether() #call the most recent name (it includes all 2 sets of data)
    #dp.drawVoltageTime()
    return



main()


