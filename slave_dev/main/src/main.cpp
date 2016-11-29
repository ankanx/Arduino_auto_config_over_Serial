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
char temp_buffer[buffer_size];
// Check buffer
const int check_size = 1;
char check[check_size];
// Reading init pos
int start_pos = 1;

boolean readValue =false;

String sparc_name = "";
String sparc_type = "";
String sparc_uuid = "";
String sparc_ssid = "";
String sparc_password = "";

int value = 0;
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

      inputString.remove(0, 1);
      inputString.toCharArray(buffer,buffer_size);
      Serial.println(buffer);
      Serial.println("Writing to EEPROM!");

      // Read and write values seperated by ':'
      // Each value gets 50 bytes
      for (int i = 0; i < buffer_size;i++){
        // Advance 50 bytes
        value = value + 50;
        // If new value
        if(buffer[i] == ':'){

          int z = 0;
          readValue = false;

          // Erase buffer.
          for (int x = 0; x < buffer_size; x++) {
            temp_buffer[x] = 0;
          }
          // Read and store a value
          while (!readValue){
            if (buffer[i] == ':'){
              readValue = true;
              i = i-1;
            }else{
            temp_buffer[z] = buffer[i];
            EepromUtil::eeprom_write_string(start_pos + value,temp_buffer);
            Serial.println(temp_buffer);
            i++;
            z++;

            }
          }
        }
      }


      // clear the string:
      inputString = "";
      readValue = false;
      value = 0;
      stringComplete = false;
      finished_config = true;
    }
    // Erase command!
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
    // UUID
    EepromUtil::eeprom_read_string(start_pos,buffer,buffer_size);
    // Manditory to ensure whole buffer is printed.
    Serial.print("first store:");
    Serial.print(buffer);
    Serial.println();
    // Erase buffer.
    for (int i = 0; i < buffer_size; i++) {
      buffer[i] = 0;
    }

    // Name
    EepromUtil::eeprom_read_string(start_pos+50,buffer,buffer_size);
    Serial.print("Third store:");
    Serial.print(buffer);
    Serial.println();
    for (int i = 0; i < buffer_size; i++) {
      buffer[i] = 0;
    }

    // Type
    EepromUtil::eeprom_read_string(start_pos+100,buffer,buffer_size);
    Serial.print("Second store:");
    Serial.print(buffer);
    Serial.println();

    for (int i = 0; i < buffer_size; i++) {
      buffer[i] = 0;
    }

    // Location
    EepromUtil::eeprom_read_string(start_pos+150,buffer,buffer_size);
    Serial.print("Second store:");
    Serial.print(buffer);
    Serial.println();

    for (int i = 0; i < buffer_size; i++) {
      buffer[i] = 0;
    }

    // SSID
    EepromUtil::eeprom_read_string(start_pos+200,buffer,buffer_size);
    Serial.print("Second store:");
    Serial.print(buffer);
    Serial.println();

    for (int i = 0; i < buffer_size; i++) {
      buffer[i] = 0;
    }

    // PASSWORD
    EepromUtil::eeprom_read_string(start_pos+250,buffer,buffer_size);
    Serial.print("Second store:");
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
