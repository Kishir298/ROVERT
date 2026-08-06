#include <Arduino.h>
#include "motors.h"
#include "config.h"


void setupMotors()
{
    pinMode(LEFT_IN1, OUTPUT);
    pinMode(LEFT_IN2, OUTPUT);
    pinMode(LEFT_EN, OUTPUT);

    pinMode(RIGHT_IN1, OUTPUT);
    pinMode(RIGHT_IN2, OUTPUT);
    pinMode(RIGHT_EN, OUTPUT);

    stopMotors();
}


void moveForward()
{
    digitalWrite(LEFT_IN1,HIGH);
    digitalWrite(LEFT_IN2,LOW);

    digitalWrite(RIGHT_IN1,HIGH);
    digitalWrite(RIGHT_IN2,LOW);

    analogWrite(LEFT_EN,MOTOR_SPEED_NORMAL);
    analogWrite(RIGHT_EN,MOTOR_SPEED_NORMAL);
}



void moveBackward()
{
    digitalWrite(LEFT_IN1,LOW);
    digitalWrite(LEFT_IN2,HIGH);

    digitalWrite(RIGHT_IN1,LOW);
    digitalWrite(RIGHT_IN2,HIGH);

    analogWrite(LEFT_EN,MOTOR_SPEED_NORMAL);
    analogWrite(RIGHT_EN,MOTOR_SPEED_NORMAL);
}



void turnLeft()
{
    digitalWrite(LEFT_IN1,LOW);
    digitalWrite(LEFT_IN2,HIGH);

    digitalWrite(RIGHT_IN1,HIGH);
    digitalWrite(RIGHT_IN2,LOW);

    analogWrite(LEFT_EN,MOTOR_SPEED_TURN);
    analogWrite(RIGHT_EN,MOTOR_SPEED_TURN);
}



void turnRight()
{
    digitalWrite(LEFT_IN1,HIGH);
    digitalWrite(LEFT_IN2,LOW);

    digitalWrite(RIGHT_IN1,LOW);
    digitalWrite(RIGHT_IN2,HIGH);

    analogWrite(LEFT_EN,MOTOR_SPEED_TURN);
    analogWrite(RIGHT_EN,MOTOR_SPEED_TURN);
}



void stopMotors()
{
    digitalWrite(LEFT_IN1,LOW);
    digitalWrite(LEFT_IN2,LOW);

    digitalWrite(RIGHT_IN1,LOW);
    digitalWrite(RIGHT_IN2,LOW);

    analogWrite(LEFT_EN,0);
    analogWrite(RIGHT_EN,0);
}
