#include <Adafruit_Sensor.h>

#include "DHT.h"         //include DHT library
#define DHTPIN 7         //define as DHTPIN the Pin 7 used to connect the Sensor
#define DHTTYPE DHT11    //define the sensor used(DHT11)

DHT dht(DHTPIN, DHTTYPE);//create an instance of DHT

void setup() {
  Serial.begin(9600);    //initialize the Serial communication
  dht.begin();           //initialize DHT
}

void loop() {
    float h = dht.readHumidity();    
    float t = dht.readTemperature();
    float hic = dht.computeHeatIndex(t, h, false);

    // did reading fail?
    if (isnan(h) || isnan(t) || isnan(hic)) {    
      Serial.println("Failed to read from DHT sensor!");
      return;
    }
    
    Serial.print(t, 2);
    Serial.print("\t");
    Serial.print(h, 2);
    Serial.print("\t");
    Serial.println(hic, 2);
    delay(2000);
}
