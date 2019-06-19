How this system work:
(Last Edited June 2019 by Xiyuan Li)

                                        *********** SD CARD ************
                                    ***********                  ************
                                                         |
                                                         |
                                                         |
                                                      \  |  /
                                                       \   /
                                                        \ /
                                                         ^
What Arduino board does:
(1) Loads SD card
(2) picks up signal from wave probes,
(3) writes voltage value to a .txt file with time stamp in the front and signal source signature behind.
(4) counts the operation time, prompt its status on lcd screen.

Note: Arduno does not compute wave height as voltage-height conversion function changes every time depending on
the 0 height level. Related information needs to be entered into the python program following its prompts.

What the Python program package does:
(1) Loads all the time, voltage, signal source information into dictionaries
    (each signal source has its own dictionary).
(2) Generates .txt files with time, voltage, and wave height.
(3) Generates pictures of voltage as a function of time.
(4) Many other data manipulation methods.

*For programmers: You can chose to only inspect data from a specific time interval and generate pictures accordingly.
 Look into the program to find definition of this method.





                                        *********** USB Live ************
                                    ***********                  ************
                                                         |
                                                         |
                                                         |
                                                      \  |  /
                                                       \   /
                                                        \ /
                                                         ^

What Arduino board does:
(1) picks up signal from wave probes,
(2) writes voltage value to series monitor with time stamp in the front and signal source signature behind,
    separated by " ".
(3) counts the operation time

Note: Arduno does not compute wave height, as voltage-height conversion function changes every time depending on
the 0 height level. To get height-time graph, related information needs to be entered into the python program

What the Python program package does:
(1) Loads all the time, voltage, signal source information into lists
    (each signal source has its own list).
(2) Generates .txt files with time and voltage.
(3) Generates pictures of voltage as a function of time.
(4) Other data manipulation methods.

*For programmers: You can chose to only inspect data from a specific time interval and generate pictures accordingly.
 Look into the program code to find definition of this interval method.

Step-by-Step INSTRUCTION:

* Setting up the wave height gauges and probes:
1) Connect power supply to the six-pin cable.
2) Connect six-pin cable to wave height gauge (model AWP-24-3)
3) Open the shield of AWP-24-3, find reset button and push and hold for 4 seconds and release.
4) Now the indication LED should be steady burn red. Put wave probe to the maximum height
   you want to measure.
6) Make sure water level and wave probes are steady, push the reset button once and wait.
7) After no more than 5 seconds, the indication LED should start blinking once every 9 seconds.
8) After the calibration step, raise the wave probe to about one-half of the length under water. Make sure
   crests and troughs of wave will not exceed the height you used for calibration or the bottom of the
   probe.
5) Take the + and - output wires and connect them to the inverting Op-Amp circuit. (See figure)

* Setting up the Inverting Op-Amp Circuit

 The circuit:
 * 10k resistor + 220 resistor to inverting input
 * 220 resistor from inverting input to output
 * 6*10k resistors + 1k resistor + 330 resistor + 220 resistor to non-inverting input
 * 9v power supply to + power input (through the series of resistors)
 * + output of wave gauge to inverting input through 10k and 220 resistors
 * - output directly to Arduino GND


Connect the white wire to +, connect the green wire to -
Finally, test the circuit with actual wave gauge output, make sure the voltage out of the circuit is between 0-5 V.


*Connecting the Inv. Op-Amp Circuit to Arduino:

**Note: the - and + output of probes in this section means the - and + coming out of the respective Inv. Op-Amp circuit.

 The circuit:
 * - output(s) to GNDs
 * + *output of probe 1 to analog pin A0
 * + *output of probe 2 to analog pin A4

*Connecting the LCD Display to Arduino:

 The circuit:
 * LCD RS pin to digital pin 12
 * LCD Enable pin to digital pin 11
 * LCD D4 pin to digital pin 5
 * LCD D5 pin to digital pin 4
 * LCD D6 pin to digital pin 3
 * LCD D7 pin to digital pin 2
 * LCD R/W pin to ground
 * LCD VSS pin to ground
 * LCD VCC pin to 5V
 * 10K resistor:
 * ends to +5V and ground
 * wiper to LCD VO pin (pin 3)

**NOTE: It may be hard to figure out how to connect everything to Arduino UNO R3 with limited space on the first try,
        please find an example of compact circuit connection in the folder.

* Connecting Arduino to a computer:

1) Connect Arduino to a computer via USB.
2) Open Arduino software, select the correct board type (UNO R3) and USB port address.
3) Open the .ino program and lick the upload button.
4) Open Serial Monitor in the software, choose show time stamp, click Clear Output and push the reset button
   on the board at the same time to start a new recording. Time elapsed will be shown on the LCD screen.

*Note: As data was designed to be reflected on one graph, the suggested maximum recording time is 100 seconds, however,
 this is just a suggestion, exceeding this time by several times will not affect the functionality of the system.

5) To stop recording, remove USB connection.
6) Then select all the data in the Serial Monitor window, copy and paste data to data_Arduino_output.txt
   and run the main Python program.

* Note: The default output contains two graphs of data from the two probes and a graph which includes data from both probes.




                                    *********** For programmers: ************
                                    ***********                  ************
                                                         |
                                                         |
                                                         |
                                                      \  |  /
                                                       \   /
                                                        \ /
                                                         ^

What's in this program package
DataADT.py
DataReader.py
plotter.py
main.py
read_analog_wave.ino

*****************************************
DataADT.py
List of methods:

    __init__(self, time, voltage, s_signal)
    **IMPORTANT: Height parameter is not shown here, it will be computed using voltage
                 during the initialization process of a data item.

    setTime(self, time)

    setVoltage(self, voltage)

    setSignal(self, s_signal)

    setHeight(self, height)

    getTime(self)

    getVoltage(self)

    getSignal(self)

    getHeight(self)

    __repr__(self)

*****************************************
DataReader.py
List of functions:

    validSource(self, SourceSignature)
        Check to see if sensors are named correctly as different sensors
        are used distinguish water height at different points.

    conversion10(self)
        Converts 10 bits analog data to voltage value. Updates each dataCat item.

    deleteTimeBefore(self, timeStamp)
        Delete all the data before this time stamp, exclusive.

    deleteTimeAfter(self, timeStamp)
        Delete all the data after this time stamp, exclusive.

    printDataCatalogue(self)
        Print the string representation of data items in the catalogue.

    getTimeList(self):
            Print all the time stamp for reference.

    saveDataCatalogue(self):
        Generates a .txt file with data items explained.
        This is a "reader-friendly" version of the output.

    saveForPlotter(self):
        Generates a .txt file with all parameters separated by " " and \n
        This is used for plotter.py or other programs to plot graphs.

******************************************
main.py
Makes use of functions in DataReader.py and prompts user to enter information needed to plot graphs.

******************************************
DataPlotter.py

Note: data visualization makes use of simple plot from matplotlib py package.

List of functions:
    __init__(self, data)
        Initialize the dataPlotter and transfer data from data.txt to dataCat.
    drawVoltageTime(self)
        Draw the Voltage/Time Graph
    drawVTogether(self)
        Draw graphs from two probes in one figure

******************************************
read_analog_wave.ino

	void setup()
	Sets up the port and LCD

	void loop()
	Generates a string with data information for probe1 and probe2 and export to serial output window.

	*Note: delay = 10 ms. Arduino picks up 100*2(probes) data each second.
	*Note: probe1 = analog pin A0; probe2 = analog pin A4


