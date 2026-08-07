"""
ROVERT Configuration Settings
=============================

Stores adjustable system settings.
"""


# =============================
# ESP32-CAM Network Settings
# =============================

ESP32_IP = "192.168.1.100"

ESP32_PORT = 80


# =============================
# HTTP Communication
# =============================

REQUEST_TIMEOUT = 2


# =============================
# Vision System Settings
# =============================

# YOLO model file
YOLO_MODEL = "yolov8n.pt"


# Minimum confidence required for detections
CONFIDENCE_THRESHOLD = 0.5


# Area threshold for detecting objects close to robot
CLOSE_OBJECT_AREA_THRESHOLD = 50000
