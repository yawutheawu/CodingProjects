#include <WiFi.h>
#include <ESPmDNS.h>
#include <ESP32Servo.h>

#define PulseHigh 16

Servo PulseServo;

// Network Info
const char* ssid = "PLACEHOLDERSSID";
const char* password = "PLACEHOLDERPASSWORD";
const String WebName = "yubipulser";
const int offpos = 0;
const int onpos = 90;
int pausedelay = 1000;

// Set web server port number to 80
WiFiServer server(80);

// Variable to store the HTTP request
String header;

void setup() {
  // Set pin mode
  // pinMode(PulseHigh,OUTPUT);
  // digitalWrite(PulseHigh,HIGH);
  Serial.begin(9600);
  Serial.println(ssid);
  WiFi.begin(ssid, password);
  while (WiFi.status() != WL_CONNECTED) {
    delay(500);
    Serial.print(".");
  }
  // Print local IP address and start web server
  Serial.println("");
  Serial.println("WiFi connected.");
  Serial.println("IP address: ");
  Serial.println(WiFi.localIP());
  server.begin();
  if (!MDNS.begin(WebName)) {
    Serial.println("Error setting up MDNS responder!");
    return;
  }
  Serial.println("mDNS responder started");
  PulseServo.attach(PulseHigh);
}

void loop() {
  WiFiClient client = server.available();
  if (client) {
    Serial.println("New Client Detected.");
    String currentLine = "";
    while (client.connected()) {
      char c = client.read();
      Serial.write(c);
      header += c;
      if (c == '\n') {
        if (currentLine.length() == 0) {
          client.println("HTTP/1.1 200 OK");
          client.println("Content-type:text/html");
          client.println("Connection: close");
          client.println();
          if (header.indexOf("GET /Pulse/on") >= 0) {
            trigger();
          };

          // Display the HTML web page
          client.println("<!DOCTYPE html><html>");
          client.println("<head><meta name=\"viewport\" content=\"width=device-width, initial-scale=1\">");
          client.println("<link rel=\"icon\" href=\"data:,\">");
          // CSS to style the on/off buttons
          // Feel free to change the background-color and font-size attributes to fit your preferences
          client.println("<style>html { font-family: Helvetica; display: inline-block; margin: 0px auto; text-align: center;}");
          client.println(".button { background-color: #4CAF50; border: none; color: white; padding: 16px 40px;");
          client.println("text-decoration: none; font-size: 30px; margin: 2px; cursor: pointer;}");
          client.println(".button2 {background-color: #555555;}</style></head>");

          // Web Page Heading
          client.println("<body><h1>Yubikey Remote Activation</h1>");

          //Button
          client.println("<p><a href=\"/Pulse/on\"><button class=\"button\">Send Pulse</button></a></p>");

          client.println("</body></html>");

          client.println();

          break;

        } else {
          currentLine = "";
        }
      } else if (c != '\r') {
        currentLine += c;
      }
    }
  }

  // Clear the header variable
  header = "";
  // Close the connection
  client.stop();
  // Serial.println("Client disconnected.");
  // Serial.println("");
}


void trigger() {
  Serial.println("Pulsing YubiKey");
  digitalWrite(PulseHigh, LOW);
  PulseServo.write(onpos);
  Serial.print("Wrote ONPOS to PIN ");
  Serial.print(PulseHigh);
  delay(pausedelay);
  PulseServo.write(offpos);
  Serial.print("Wrote OFFPOS to PIN ");
  Serial.print(PulseHigh);
}