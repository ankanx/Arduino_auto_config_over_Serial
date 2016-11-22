#include "Timer.h"


// Variable to check if entire message is read
boolean Complete = false;  // whether the string is complete

unsigned long lastCommand;
unsigned long timer;


// Message stored in byteArray
byte byteArray[6];

// Message size counter
int j=0;


void setup() {
// start serial at 9600 baud
Serial.begin(9600);   
}

void loop() {

   timer = millis();
 
      // If Message is complete check command for instructions
  if (Complete) {

    // Carry out Instructions
    lastCommand = millis();
    // Reset for new Message
    Complete = false;
    j=0;
  
    // Empty old message to make space for new
    for(int i = 0; i < 5; i++){
    byteArray[i] = 0;
    }
  }


}

/*
  SerialEvent occurs whenever a new data comes in the
 hardware serial RX.  This routine is run between each
 time loop() runs, so using delay inside loop can delay
 response.  Multiple bytes of data may be available.
 */
void serialEvent() {
   
     byte CR;
     byte LF;
  while (Serial.available()) {
    // get the new byte:
    byte inByte = (byte)Serial.read();

    // Store message byte in Array
    byteArray[j] = inByte;
    //Serial.write(byteArray[j]);
    
      // Increment in wait for new byte
      j++;
      
    // Look for CRLF message complete
    if (inByte == 0x0d){
      CR = 0x0d;
    }
    if (inByte == 0x0a){
      LF = 0x0a;
    }
    
    if(inByte == 0x04 && CR == 0x0d && LF == 0x0a)
    {
      
       // Got CRLF
       Complete = true;
     }

  }
}

