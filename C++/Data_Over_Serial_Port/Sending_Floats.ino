

//Kaleb Nails
//Created: 9/18/2022
//Modified: 10/25/2022
//Purpose: This shows a method of sending floating (or any type) data points over serial ports.
//Original name: Packetresponse


//THIS IS THE WORKING EXAMPLE

#include <PacketSerial.h>
PacketSerial myPacketSerial;
#define N_FLOATS 4
char Buffer[100];

//uint8_t myPackets[2] = {245,255};
uint8_t myChars[4*N_FLOATS];
float myFloats[N_FLOATS];

void setup() {
  // put your setup code here, to run once:
 

  //Serial.begin(115200);
  myPacketSerial.begin(115200);
  //myPacketSerial.setPacketHandler(&onPacketRecieved);

  float input; // to int creates 1 thing, say int input[100]; 
 
  
  myFloats[0] = 1.23;
  myFloats[1] = 2.34;
  myFloats[2] = 5.67;
  
  
  //myPacketSerial.update();
  //uint8_t sent = {8};
  
}

void loop() {
  
  myFloats[3] = (float) millis();
  
  memcpy( myChars , myFloats , sizeof(myFloats) );
  
  //myPacketSerial.send(myPackets,2);
  myPacketSerial.send( myChars, sizeof(myFloats) );
  delay (10);
        
 /*
  Serial.setTimeout(1000);

  
  if (Serial.available())
    {
      
      int nBytes = Serial.readBytesUntil('\x00', Buffer, 100); this workedish
      //input = Serial.readBytes(Buffer, 4);
      //Serial.print(input);
      Serial.write(Buffer,nBytes); this somewhat worled
      
      
      delay(100);
    }
    */
}
