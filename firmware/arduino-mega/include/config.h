#ifndef CONFIG_H
#define CONFIG_H

// =============================
// L298N Motor Driver Pins
// =============================

// Left motor
#define LEFT_IN1 22
#define LEFT_IN2 23
#define LEFT_EN 26

// Right motor
#define RIGHT_IN1 24
#define RIGHT_IN2 25
#define RIGHT_EN 27


// =============================
// HW201 IR Sensors
// =============================

#define IR_FRONT_LEFT  A0
#define IR_FRONT_RIGHT A1
#define IR_LEFT        A2
#define IR_RIGHT       A3

#define IR_ACTIVE_STATE LOW


// =============================
// UART
// =============================

#define ESP_SERIAL Serial1
#define ESP_BAUD 115200


// =============================
// Motor Speed
// =============================

#define MOTOR_SPEED_NORMAL 180
#define MOTOR_SPEED_TURN 160


// =============================
// Timing
// =============================

#define SENSOR_REPORT_INTERVAL 500


#endif
