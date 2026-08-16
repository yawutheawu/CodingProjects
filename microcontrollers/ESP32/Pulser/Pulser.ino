#include <Arduino.h>

#define PulseHigh 16
#define Debug false

void setup() {
  // Set pin mode
  pinMode(PulseHigh,OUTPUT);
  if (Debug) {
    Serial.begin(9600);
  };
}

void loop() {
  delay(2500);
  digitalWrite(PulseHigh,HIGH);
  if (Debug) {
    Serial.print("Set Pin ");
    Serial.print(PulseHigh);
    Serial.println(" to High");
  };
  delay(100);
  digitalWrite(PulseHigh,LOW);
  if (Debug) {
    Serial.print("Set Pin ");
    Serial.print(PulseHigh);
    Serial.println(" to Low");
  };
}