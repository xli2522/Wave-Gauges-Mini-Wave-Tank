/*
  AnalogReadSerial

 testing program 
 
 @ Western University Physics and Astronomy
 
*/

/* 
 *  For SD card datalogger
 *  This program is built with reference to Tom Igoe's Datalogger program.
 *  The circuit:
 *  * analog sensors on analog ins 0 and 1
 *  * SD card attached to SPI bus as follows:
 *  * MOSI - PIN 11
 *  * MISO - PIN 12
 *  * CLK - PIN 13
 *  * CS - PIN 10 *Note by Xiyuan (pin 10 for Adafruit sd, see online for other connections)
 *  created  24 Nov 2010 
 *  modified 9 Apr 2012
 *  by Tom Igoe
 *  modified 25 June 2019
 *  by Xiyuan Li
 */

 
// include the library code:
#include <SPI.h>
#include <SD.h>

// initialize the SD reading pin
const int chipSelect = 10;
//count number of loops
int series = 0;

// Set up port and SD card 
void setup() {
  // initialize serial communication at 9600 bits per second:
  Serial.begin(9600);
  
  while (!Serial) {
    ; // wait for serial port to connect. Needed for native USB port only
  }


  Serial.print("Initializing SD card...");

  // see if the card is present and can be initialized:
  if (!SD.begin(chipSelect)) {
    Serial.println("Card failed, or not present");
    // don't do anything more:
    while (1);
  }
  Serial.println("card initialized.");
}

void loop() {
  // make a string for assembling the data to log:
  String dataString = "";
  
  // read three sensors and append to the string:
  for (int analogPin = 0; analogPin < 2; analogPin++) {
    int sensor = analogRead(analogPin);
    dataString += String(series) + " --> " + String(sensor) + " sensor" + String(analogPin+1);
    if (analogPin < 1) {
      dataString += "\n";
    }
  series += 1;
  }

  // open the file. note that only one file can be open at a time,
 
  File dataFile = SD.open("adl.txt", FILE_WRITE);

  // if the file is available, write to it:
  if (dataFile) {
    dataFile.println(dataString);
    
    dataFile.close();
    // print to the serial port too:
    Serial.println(dataString);
  }
  // if the file isn't open, pop up an error:
  else {
    Serial.println("error opening data_Arduino_output.txt");
  }
  // Delay for 10 ms for stability
  delay(10);
}
