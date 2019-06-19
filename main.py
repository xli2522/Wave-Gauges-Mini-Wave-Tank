from DataReader import *
from DataPoltter import *

''' Height conversion is fixed to 2, currently not functional.
        Log:
        Beta Version 0.2
        Modified on 18 July 2019 by Xiyuan Li'''

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


