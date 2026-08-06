#ifndef IR_H
#define IR_H


void setupIR();

bool irTriggered(int pin);

bool obstacleDetected();

void sendSensorReport();


#endif
