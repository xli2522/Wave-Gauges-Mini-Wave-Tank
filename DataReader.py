import datetime

from DataADT import DataADT

"""
    Created on May 10th 2019 by Xiyuan Li
    **Important: methods in class DataReader are designed to read .txt file with specific format.
        Log: 
        Beta Version 0.2
        Modified on 18 July 2019 by Xiyuan Li'''
"""

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






