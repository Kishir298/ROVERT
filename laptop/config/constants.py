"""
ROVERT Constants
================
Constants used throughout the laptop software.
These values rarely change.
"""

# ==========================================================
# Movement Commands
# ==========================================================

FORWARD = "F"
BACKWARD = "B"
LEFT = "L"
RIGHT = "R"
STOP = "S"

# ==========================================================
# HTTP API Endpoints
# ==========================================================

STREAM_ENDPOINT = "/stream"
SENSORS_ENDPOINT = "/sensors"
COMMAND_ENDPOINT = "/command"

# ==========================================================
# Robot Status
# ==========================================================

STATUS_IDLE = "IDLE"
STATUS_RUNNING = "RUNNING"
STATUS_AVOIDING = "AVOIDING"
STATUS_SEARCHING = "SEARCHING"
STATUS_COLLECTING = "COLLECTING"
STATUS_RETURNING = "RETURNING"
STATUS_ERROR = "ERROR"

# ==========================================================
# Object Detection States
# ==========================================================

OBJECT_DETECTED = "OBJECT_DETECTED"
NO_OBJECT = "NO_OBJECT"

# ==========================================================
# Sensor States
# ==========================================================

OBSTACLE = 1
CLEAR = 0

# ==========================================================
# Mission States
# ==========================================================

MISSION_NOT_STARTED = "NOT_STARTED"
MISSION_ACTIVE = "ACTIVE"
MISSION_PAUSED = "PAUSED"
MISSION_COMPLETE = "COMPLETE"
MISSION_ABORTED = "ABORTED"
