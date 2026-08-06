#include <Arduino.h>

#include "config.h"

#include "motors.h"
#include "ir.h"
#include "uart.h"



unsigned long lastReport = 0;

bool emergencyStop=false;



void setup()
{

    setupUART();

    setupMotors();

    setupIR();


    Serial.println("ROVERT Mega Ready");

}



void loop()
{

    if(obstacleDetected())
    {

        if(!emergencyStop)
        {
            stopMotors();

            sendEvent("EVENT:IR_STOP");

            emergencyStop=true;
        }

    }
    else
    {
        emergencyStop=false;
    }



    readCommand();



    if(millis()-lastReport>SENSOR_REPORT_INTERVAL)
    {

        lastReport=millis();

        sendSensorReport();

    }

}
