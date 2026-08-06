#include <Arduino.h>

#include "uart.h"
#include "motors.h"


void setupUART()
{
    Serial.begin(115200);
    Serial1.begin(115200);
}



void readCommand()
{

    if(!Serial1.available())
        return;


    String cmd = Serial1.readStringUntil('\n');

    cmd.trim();


    if(cmd=="CMD:F")
        moveForward();

    else if(cmd=="CMD:B")
        moveBackward();

    else if(cmd=="CMD:L")
        turnLeft();

    else if(cmd=="CMD:R")
        turnRight();

    else if(cmd=="CMD:S")
        stopMotors();

}



void sendEvent(const char* message)
{
    Serial1.println(message);
}
