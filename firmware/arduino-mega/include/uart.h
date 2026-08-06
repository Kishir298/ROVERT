#ifndef UART_H
#define UART_H


void setupUART();

void readCommand();

void sendEvent(const char* message);


#endif
