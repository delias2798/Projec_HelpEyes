#include <ESP8266WiFi.h>
#include <WiFiClient.h>

#define NAME "Aoartamento_ASIP"
#define PASS "12345678"

const char* host = "172.16.2.39";
int counter = 0;


void setup() {
  Serial.begin(9600);
  Serial.println();

  /* Set Client up as station */
  WiFi.mode(WIFI_STA);

  WiFi.begin(NAME, PASS);

  /* Connect to the network */
  Serial.print("Connecting");
  while(WiFi.status() != WL_CONNECTED)
  {
    delay(2000);
    Serial.print(".");
  }
  Serial.println();

  Serial.println("Connected, IP address: ");
  Serial.println(WiFi.localIP());
}

void loop() {
  if(counter == 0) {
    WiFiClient client;

    Serial.printf("\n[Connecting to %s ... ", host);
    if (client.connect(host, 9595)){
    
    Serial.println("connected]");

    Serial.println("[Sending a request]");
    client.println("Hello from Arduino");

    Serial.println("[Response:]");
    while (client.connected() || client.available()){
      if (client.available())
      {
        String line = client.readStringUntil('\n');
        Serial.println(line);
      }
    }
    client.stop();
    Serial.println("\n[Disconnected]");
    counter++;
  }
  else
  {
    Serial.println("connection failed!]");
    client.stop();
  }
  delay(5000);
  } else {
    Serial.println("ONE CONECCTION DONE");
    delay(5000);
  }
}
