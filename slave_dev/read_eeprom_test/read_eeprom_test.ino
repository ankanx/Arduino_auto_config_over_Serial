#include <EepromUtil.h>
#include <EEPROM.h>

String inputString = "";         // a string to hold incoming data
boolean stringComplete = false;  // whether the string is complete
boolean written = false;
const int BUFSIZE = 50;
char buf[BUFSIZE];
void setup() {
  // initialize serial:
  Serial.begin(9600);
  // reserve 200 bytes for the inputString:
  inputString.reserve(200);
}

void loop() {

    delay(1000);
    EepromUtil::eeprom_read_string(1,buf,BUFSIZE);
    Serial.print(buf);
    Serial.println();
  
  
}

/*
  SerialEvent occurs whenever a new data comes in the
 hardware serial RX.  This routine is run between each
 time loop() runs, so using delay inside loop can delay
 response.  Multiple bytes of data may be available.
 */
void serialEvent() {
  while (Serial.available()) {
    // get the new byte:
    char inChar = (char)Serial.read(); 
    // add it to the inputString:
    inputString += inChar;
    // if the incoming character is a newline, set a flag
    // so the main loop can do something about it:
    if (inChar == '\n') {
      stringComplete = true;
    } 
  }
}


