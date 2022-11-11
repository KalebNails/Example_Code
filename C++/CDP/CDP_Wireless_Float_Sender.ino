// Kaleb Nails
// Created: 9/23/2022
// Modified: 11/11/2022
// original name: Testrawsender
//
// Purpose: To send 1 floating point number to another hellteck wirelessly using CDP.
// The other hellteck recieving is running the code:
// original reciever name: Testreciever
// New name: CDP_Wireless_Float_Reciever.ino
//




#include <MamaDuck.h>
#include <arduino-timer.h>
#include <string>

#ifdef SERIAL_PORT_USBVIRTUAL
#define Serial SERIAL_PORT_USBVIRTUAL
#endif


MamaDuck duck;


DuckDisplay* display = NULL;

const int INTERVAL_MS = 1000;
int counter = 1;
bool sentOk = false;
char Buffer[100];
#define N_FLOATS 2
uint8_t myChars[4*N_FLOATS];
float myFloats[N_FLOATS];


// LORA RF CONFIG
#define LORA_FREQ 915.0 // Frequency Range. Set for US Region 915.0Mhz
#define LORA_TXPOWER 20 // Transmit Power
// LORA HELTEC PIN CONFIG
#define LORA_CS_PIN 18
#define LORA_DIO0_PIN 26
#define LORA_DIO1_PIN -1 // unused
#define LORA_RST_PIN 14

auto timer = timer_create_default();

void setup() {
  // We are using a hardcoded device id here, but it should be retrieved or
  // given during the device provisioning then converted to a byte vector to
  // setup the duck NOTE: The Device ID must be exactly 8 bytes otherwise it
  // will get rejected
  std::string deviceId("MAMA0002");
  std::vector<byte> devId;
  devId.insert(devId.end(), deviceId.begin(), deviceId.end());
  //duck.setupWithDefaults(devId);
  //Serial.begin(115200);
  //Set the Device ID
  duck.setDeviceId(devId);
  // initialize the serial component with the hardware supported baudrate
  duck.setupSerial(115200);
  // initialize the LoRa radio with specific settings. This will overwrites settings defined in the CDP config file cdpcfg.h
  duck.setupRadio(LORA_FREQ, LORA_CS_PIN, LORA_RST_PIN, LORA_DIO0_PIN, LORA_DIO1_PIN, LORA_TXPOWER);
  // initialize the wifi access point with a custom AP name
  duck.setupWifi();
  // initialize DNS
  duck.setupDns();
  // initialize web server, enabling the captive portal with a custom HTML page
  duck.setupWebServer(true);
  // initialize Over The Air firmware upgrade
  duck.setupOTA();

  
   timer.every(INTERVAL_MS, runSensor);
   myFloats[0] = 2.6;
   myFloats[1] = 1.8;
   
   
   
}



 void loop() {



  
  //memcpy(myChars, myFloats, sizeof(myFloats));
  //myFloats[0] = (float) millis();
  timer.tick();
  
  // Use the default run(). The Mama duck is designed to also forward data it
  // receives from other ducks, across the network. It has a basic routing
  // mechanism built-in to prevent messages from hoping endlessly.
  duck.run();
  
}

bool runSensor(void *) {
  bool result;
  const byte* buffer;
  
  memcpy(myChars, myFloats, sizeof(myFloats));

  /*
  String message =  String(myChars);
  int length = message.length();
  Serial.print("[MAMA] sensor data: ");
  Serial.println(message);
  buffer = (byte*) message.c_str(); 
*/

  //memcpy(myChars, myFloats, sizeof(myFloats));
  //result = sendData(myChars, sizeof(myChars));
  int length = sizeof(myChars);
  result = sendData(myChars, length);
  if (result) {
    Serial.println("[MAMA] runSensor ok.");
  } else {
    Serial.println("[MAMA] runSensor failed.");
  }
  
  return result;
}

bool sendData(const byte* myChars, int length) {
  bool sentOk = false;
  
  // Send Data can either take a byte buffer (unsigned char) or a vector
  int err = duck.sendData(topics::status, myChars, length);//myChars, sizeof(myChars));
  if (err == DUCK_ERR_NONE) {
    counter++;
    myFloats[0]++;
    //myFloats[0] = 1.2 + float(counter);
    sentOk = true;
  }
  if (!sentOk) {
    Serial.println("[MAMA] Failed to send data. error = " + String(err));
  }
  return sentOk;
}
