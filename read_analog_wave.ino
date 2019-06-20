/*
  AnalogReadSerial

 testing program by Xiyuan Li
 
 @ Western University Physics and Astronomy
 
*/

 
/*
 * For LCD Display
  LiquidCrystal Library 

 This sketch prints "Recording time:" to the LCD
 and shows the time.

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

 Library originally added 18 Apr 2008
 by David A. Mellis
 library modified 5 Jul 2009
 by Limor Fried (http://www.ladyada.net)
 example added 9 Jul 2009
 by Tom Igoe
 modified 22 Nov 2010
 by Tom Igoe
 modified 7 Nov 2016
 by Arturo Guadalupi
 modified 14 Jun 2019
 by Xiyuan Li

 This original example code is in the public domain.

 http://www.arduino.cc/en/Tutorial/LiquidCrystalHelloWorld

*/
 

// include the library code:
#include <LiquidCrystal.h>
#include <SPI.h>

// initialize the library by associating any needed LCD interface pin
// with the arduino pin number it is connected to
const int rs = 12, en = 11, d4 = 5, d5 = 4, d6 = 3, d7 = 2;
LiquidCrystal lcd(rs, en, d4, d5, d6, d7);

// Set up port and SD card 
void setup() {
  
  // initialize serial communication at 9600 bits per second:
  Serial.begin(9600);
  
  // set up the LCD's number of columns and rows:

  lcd.begin(16, 2);
  // Print a message to the LCD.
  lcd.print("Recording time:");

}

void loop() {
  
  /*LCD 
   * 
   */
  // set the cursor to column 0, line 1
  // (note: line 1 is the second row, since counting begins with 0):
  lcd.setCursor(0, 1);
  // print the number of seconds since reset:
  lcd.print(millis() / 1000);
  
  /*probe1
   * 
   */
   
  // Generate data information string for probe1
  // Note probe1 should be connected to analog input pin A0
  String probe1String = "";
  int analogPin1 = 0;
  int sensor1 = analogRead(analogPin1);
  probe1String = String(sensor1) + " sensor1";

  Serial.println(probe1String);

 /*probe2
   * 
   */
   
  // Generate data information string for probe2
  // Note probe2 should be connected to analog input pin A4
  String probe2String = "";
  int analogPin2 = 4;
  int sensor2 = analogRead(analogPin2);
  probe2String = String(sensor2) + " sensor2";

  Serial.println(probe2String);
   
  // Delay for 10 ms for stability
  delay(10);
}
