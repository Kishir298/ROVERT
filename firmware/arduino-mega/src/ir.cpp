#include <Arduino.h>

#include "ir.h"
#include "config.h"


void setupIR()
{
    pinMode(IR_FRONT_LEFT,INPUT);
    pinMode(IR_FRONT_RIGHT,INPUT);
    pinMode(IR_LEFT,INPUT);
    pinMode(IR_RIGHT,INPUT);
}



bool irTriggered(int pin)
{
    return digitalRead(pin)==IR_ACTIVE_STATE;
}



bool obstacleDetected()
{
    return 
    irTriggered(IR_FRONT_LEFT) ||
    irTriggered(IR_FRONT_RIGHT) ||
    irTriggered(IR_LEFT) ||
    irTriggered(IR_RIGHT);
}



void sendSensorReport()
{
    ESP_SERIAL.print("SENSORS:");

    ESP_SERIAL.print(irTriggered(IR_FRONT_LEFT));
    ESP_SERIAL.print(",");

    ESP_SERIAL.print(irTriggered(IR_FRONT_RIGHT));
    ESP_SERIAL.print(",");

    ESP_SERIAL.print(irTriggered(IR_LEFT));
    ESP_SERIAL.print(",");

    ESP_SERIAL.println(irTriggered(IR_RIGHT));
}
