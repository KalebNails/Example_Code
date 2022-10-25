
// Author: ~Kaleb Nails
// created: 9/23/2022
// modified: 10/25/2022
// original name: Testreciever
//
// Note: This is very similiar to a tutorial found online (no longer have the link,
// this is part of a new effort to streamline documention). As such some of the original comments remain
// and are not entirely relevent or accurate. 
//
// Purpose: To recieve incoming data from the CDP network, turn it into a Json, then send it to a USB
// connected computer over serial port. The corresponding python code to recieve it is called:
// CDP_JSON_Float_Reiever.py
// The code running on the sending hellteck is called: 
//CDP_Wireless_Float_sender.ino

#include <ArduinoJson.h>
#include <arduino-timer.h>
#include <string>

/* CDP Headers */
#include <PapaDuck.h>
#include <CdpPacket.h>

#define LORA_FREQ 915.0 // Frequency Range. Set for US Region 915.0Mhz
#define LORA_TXPOWER 20 // Transmit Power
// LORA HELTEC PIN CONFIG
#define LORA_CS_PIN 18
#define LORA_DIO0_PIN 26
#define LORA_DIO1_PIN -1 // unused
#define LORA_RST_PIN 14






// Use pre-built papa duck
PapaDuck duck;

auto timer = timer_create_default();




void quackJson(std::vector<byte> packetBuffer) {

  CdpPacket packet = CdpPacket(packetBuffer);
  const int bufferSize = 4 * JSON_OBJECT_SIZE(4);
  StaticJsonDocument<bufferSize> doc;

  // Here we treat the internal payload of the CDP packet as a string
  // but this is mostly application dependent. 
  // The parsingf here is optional. The Papa duck could simply decide to
  // forward the CDP packet as a byte array and let the Network Server (or DMS) deal with
  // the parsing based on some business logic.

  std::string payload(packet.data.begin(), packet.data.end());
  std::string sduid(packet.sduid.begin(), packet.sduid.end());
  std::string dduid(packet.dduid.begin(), packet.dduid.end());

  std::string muid(packet.muid.begin(), packet.muid.end());
  std::string path(packet.path.begin(), packet.path.end());


  doc["DeviceID"] = sduid;
  doc["MessageID"] = muid;
  doc["Payload"].set(payload);
  doc["path"].set(path);
  doc["hops"].set(packet.hopCount);
  doc["duckType"].set(packet.duckType);
  doc["topic"].set((packet.topic));

  String jsonstat;
  serializeJson(doc, Serial);
  Serial.println("");

}



// The callback method simply takes the incoming packet and
// converts it to a JSON string, before sending it out over WiFi
void handleDuckData(std::vector<byte> packetBuffer) {

  //Serial.print('recieved');
  quackJson(packetBuffer);
}

void setup() {
  
  // We are using a hardcoded device id here, but it should be retrieved or
  // given during the device provisioning then converted to a byte vector to
  // setup the duck NOTE: The Device ID must be exactly 8 bytes otherwise it
  // will get rejected
  std::string deviceId("PAPADUCK");
  std::vector<byte> devId;
  devId.insert(devId.end(), deviceId.begin(), deviceId.end());

  // the default setup is equivalent to the above setup sequence
// duck.setupSerial(115200);
  Serial.begin(115200);
  duck.setupRadio(LORA_FREQ, LORA_CS_PIN, LORA_RST_PIN, LORA_DIO0_PIN,
                  LORA_DIO1_PIN, LORA_TXPOWER);
  duck.setDeviceId(devId);

 
  // register a callback to handle incoming data from duck in the network
  duck.onReceiveDuckData(handleDuckData);

}

void loop() {
  duck.run();
  timer.tick();
}
