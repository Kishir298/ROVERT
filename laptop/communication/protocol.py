"""
ROVERT Communication Protocol
=============================

Defines the messages exchanged between:

Laptop
  ↓ HTTP
ESP32-CAM
  ↓ UART
Arduino Mega
"""


# ==========================================================
# Movement Commands
# ==========================================================

COMMAND_FORWARD = "F"
COMMAND_BACKWARD = "B"
COMMAND_LEFT = "L"
COMMAND_RIGHT = "R"
COMMAND_STOP = "S"


VALID_COMMANDS = {
    COMMAND_FORWARD,
    COMMAND_BACKWARD,
    COMMAND_LEFT,
    COMMAND_RIGHT,
    COMMAND_STOP
}


# ==========================================================
# Sensor Data Keys
# ==========================================================

IR_FRONT_LEFT = "fl"
IR_FRONT_RIGHT = "fr"
IR_LEFT = "l"
IR_RIGHT = "r"

IR_EVENT = "ir_event"


# ==========================================================
# Message Validation
# ==========================================================

def is_valid_command(command):
    """
    Checks if a movement command is supported.
    """
    return command in VALID_COMMANDS