"""
ESP32-CAM Client
================

Handles HTTP communication between:

Laptop
  ↓ HTTP
ESP32-CAM
  ↓ UART
Arduino Mega
"""

import requests

from config.settings import ESP32_IP, ESP32_PORT
from communication.protocol import is_valid_command


class ESPClient:

    def __init__(self, ip=ESP32_IP, port=ESP32_PORT):
        self.base_url = f"http://{ip}:{port}"

        self.stream_url = self.base_url + "/stream"
        self.sensor_url = self.base_url + "/sensors"
        self.command_url = self.base_url + "/command"


    def get_sensor_data(self):
        """
        Gets latest IR sensor data from ESP32-CAM.
        """

        try:
            response = requests.get(
                self.sensor_url,
                timeout=1
            )

            response.raise_for_status()

            return response.json()

        except requests.RequestException:
            return {
                "fl": 0,
                "fr": 0,
                "l": 0,
                "r": 0,
                "ir_event": False
            }



    def send_command(self, command):
        """
        Sends movement command to ESP32-CAM.

        Commands:
        F = Forward
        B = Backward
        L = Left
        R = Right
        S = Stop
        """

        if not is_valid_command(command):
            raise ValueError(
                f"Invalid command: {command}"
            )

        try:
            requests.post(
                self.command_url,
                data=command,
                timeout=1
            )

        except requests.RequestException:
            pass