class DataADT:
    """
    Created on May 10th 2019 by Xiyuan Li

    **Important: methods in class Data are designed to help DataReader access and modify information.
        Beta Version 0.2

    """
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




