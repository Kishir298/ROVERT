/*
ROVERT ESP32-CAM Firmware
=========================

Functions:
- WiFi connection
- HTTP server
- Camera streaming
- Sensor endpoint
- UART communication with Arduino Mega
*/


#include <WiFi.h>
#include <WebServer.h>
#include "esp_camera.h"


// =============================
// WiFi Settings
// =============================

const char* WIFI_SSID = "YOUR_WIFI_NAME";
const char* WIFI_PASSWORD = "YOUR_WIFI_PASSWORD";


// =============================
// Server
// =============================

WebServer server(80);


// =============================
// UART
// =============================

#define RXD2 3
#define TXD2 1


// =============================
// Camera Pins
// AI Thinker ESP32-CAM
// =============================

#define PWDN_GPIO_NUM     32
#define RESET_GPIO_NUM    -1
#define XCLK_GPIO_NUM      0
#define SIOD_GPIO_NUM     26
#define SIOC_GPIO_NUM     27

#define Y9_GPIO_NUM       35
#define Y8_GPIO_NUM       34
#define Y7_GPIO_NUM       39
#define Y6_GPIO_NUM       36
#define Y5_GPIO_NUM       21
#define Y4_GPIO_NUM       19
#define Y3_GPIO_NUM       18
#define Y2_GPIO_NUM        5

#define VSYNC_GPIO_NUM    25
#define HREF_GPIO_NUM     23
#define PCLK_GPIO_NUM     22



// =============================
// Sensor Data
// =============================

String sensorData = 
"{\"fl\":0,\"fr\":0,\"l\":0,\"r\":0,\"ir_event\":false}";



// =============================
// Camera Stream
// =============================

void handleStream()
{

  WiFiClient client = server.client();


  String response =
  "HTTP/1.1 200 OK\r\n"
  "Content-Type: multipart/x-mixed-replace; boundary=frame\r\n\r\n";


  server.sendContent(response);


  while(client.connected())
  {

    camera_fb_t *fb = esp_camera_fb_get();


    if(!fb)
      continue;


    server.sendContent(
      "--frame\r\nContent-Type: image/jpeg\r\n\r\n"
    );


    client.write(
      fb->buf,
      fb->len
    );


    server.sendContent(
      "\r\n"
    );


    esp_camera_fb_return(fb);


  }

}



// =============================
// HTTP Endpoints
// =============================


void handleRoot()
{
  server.send(
    200,
    "text/plain",
    "ROVERT ESP32 ONLINE"
  );
}



void handleSensors()
{
  server.send(
    200,
    "application/json",
    sensorData
  );
}



void handleCommand()
{

  if(server.hasArg("plain"))
  {

    String command = server.arg("plain");


    Serial2.println(command);


    server.send(
      200,
      "text/plain",
      "Command sent"
    );

  }

}



// =============================
// Setup
// =============================

void setup()
{

  Serial.begin(115200);


  Serial2.begin(
    9600,
    SERIAL_8N1,
    RXD2,
    TXD2
  );


  camera_config_t config;


  config.ledc_channel = LEDC_CHANNEL_0;
  config.ledc_timer = LEDC_TIMER_0;


  config.pin_d0 = Y2_GPIO_NUM;
  config.pin_d1 = Y3_GPIO_NUM;
  config.pin_d2 = Y4_GPIO_NUM;
  config.pin_d3 = Y5_GPIO_NUM;
  config.pin_d4 = Y6_GPIO_NUM;
  config.pin_d5 = Y7_GPIO_NUM;
  config.pin_d6 = Y8_GPIO_NUM;
  config.pin_d7 = Y9_GPIO_NUM;

  config.pin_xclk = XCLK_GPIO_NUM;
  config.pin_pclk = PCLK_GPIO_NUM;
  config.pin_vsync = VSYNC_GPIO_NUM;
  config.pin_href = HREF_GPIO_NUM;

  config.pin_sscb_sda = SIOD_GPIO_NUM;
  config.pin_sscb_scl = SIOC_GPIO_NUM;

  config.pin_pwdn = PWDN_GPIO_NUM;
  config.pin_reset = RESET_GPIO_NUM;


  config.xclk_freq_hz = 20000000;
  config.pixel_format = PIXFORMAT_JPEG;


  config.frame_size = FRAMESIZE_QVGA;
  config.jpeg_quality = 12;
  config.fb_count = 1;


  esp_camera_init(&config);



  WiFi.begin(
    WIFI_SSID,
    WIFI_PASSWORD
  );


  Serial.print("Connecting");


  while(WiFi.status() != WL_CONNECTED)
  {
    delay(500);
    Serial.print(".");
  }


  Serial.println();


  Serial.print("ESP32 IP: ");
  Serial.println(
    WiFi.localIP()
  );


  server.on(
    "/",
    handleRoot
  );


  server.on(
    "/sensors",
    handleSensors
  );


  server.on(
    "/command",
    HTTP_POST,
    handleCommand
  );


  server.on(
    "/stream",
    handleStream
  );


  server.begin();


  Serial.println(
    "ROVERT ESP32 READY"
  );

}



// =============================
// Loop
// =============================

void loop()
{

  server.handleClient();

}
