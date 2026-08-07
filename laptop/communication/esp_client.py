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

from config.settings import ESP32_IP, ESP32_PORT, REQUEST_TIMEOUT
from communication.protocol import is_valid_command



class ESPClient:


    def __init__(
        self,
        ip=ESP32_IP,
        port=ESP32_PORT
    ):


        self.ip = ip
        self.port = port

        self.update_urls()



    def update_urls(self):

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

        self.ip = new_ip

        self.update_urls()

        print(
            f"ESP32 IP changed to {self.ip}"
        )



    def test_connection(self):

        try:

            response = requests.get(
                self.base_url,
                timeout=REQUEST_TIMEOUT
            )

            return response.status_code == 200


        except requests.RequestException:

            return False



    def get_sensor_data(self):

        try:

            response = requests.get(
                self.sensor_url,
                timeout=REQUEST_TIMEOUT
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


        if not is_valid_command(command):

            raise ValueError(
                f"Invalid command: {command}"
            )



        try:

            requests.post(

                self.command_url,

                data=command,

                timeout=REQUEST_TIMEOUT

            )



        except requests.RequestException:


            print(
                "Failed to send command"
            )
