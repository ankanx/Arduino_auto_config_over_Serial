#include <EepromUtil.h>
#include <EEPROM.h>
#include <Arduino.h>

// Serial event holding string
String inputString = "";         // a string to hold incoming data
boolean stringComplete = false;  // whether the string is complete
// Temp
boolean finished_config = false;
// Read Write buffer config
const int buffer_size = 50;
char buffer[buffer_size];
// Check buffer
const int check_size = 1;
char check[check_size];
// Reading init pos
int start_pos = 1;

// Setup
void setup() {
  // initialize serial with 9600 baudrate:
  Serial.begin(9600);

  // reserve 200 bytes for the inputString:
  inputString.reserve(200);

}

// main
void loop() {
  // Print the string when a newline arrives.
  if (stringComplete) {
    // If we recive the 'C' (config) char at start
    // Save the rest of the message in EEPROM
    if (inputString.charAt(0) == 'C'){
      Serial.print("Got: ");
      Serial.println(inputString);
      inputString.toCharArray(buffer,buffer_size);
      Serial.println("Writing to EEPROM!");
      EepromUtil::eeprom_write_string(start_pos,buffer);

      //EepromUtil::eeprom_erase_all();

      // clear the string:
      inputString = "";
      stringComplete = false;
      finished_config = true;
    }

    if (inputString.charAt(0) == 'D'){
      Serial.println("Erasing Config!");
      EepromUtil::eeprom_erase_all();
      Serial.println("Erased Config!");
      // clear the string:
      inputString = "";
      stringComplete = false;
      finished_config = false;
    }
  }

  // Erase buffer.
  for (int i = 0; i < buffer_size; i++) {
    buffer[i] = 0;
  }

  if(finished_config == true){
    // To not flood the serial interface.
    delay(1000);
    EepromUtil::eeprom_read_string(start_pos,buffer,buffer_size);
    // Manditory to ensure whole buffer is printed.
    Serial.print(buffer);
    Serial.println();
  }

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
