"""
ROVERT ESP32 Communication Client
=================================

Handles HTTP communication between:

Laptop
  ↓ HTTP
ESP32-CAM
  ↓ UART
Arduino Mega
"""


import requests

from communication.protocol import is_valid_command



class ESPClient:


    def __init__(self, ip="192.168.1.100", port=80):

        self.ip = ip
        self.port = port

        self.update_urls()



    def update_urls(self):

        """
        Updates ESP32 endpoints after IP change.
        """

        self.base_url = (
            f"http://{self.ip}:{self.port}"
        )

        self.stream_url = (
            self.base_url + "/stream"
        )

        self.sensor_url = (
            self.base_url + "/sensors"
        )

        self.command_url = (
            self.base_url + "/command"
        )



    def change_ip(self, new_ip):

        """
        Changes ESP32 IP address.

        Example:
        esp.change_ip("192.168.1.55")
        """

        self.ip = new_ip

        self.update_urls()

        print(
            f"ESP32 IP changed to {self.ip}"
        )



    def test_connection(self):

        """
        Checks if ESP32 is reachable.
        """

        try:

            response = requests.get(
                self.base_url,
                timeout=2
            )

            return response.status_code == 200


        except requests.RequestException:

            return False



    def get_sensor_data(self):

        """
        Gets latest IR sensor data.
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
        Sends movement command to ESP32.

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

            print(
                "Failed to send command"
            )