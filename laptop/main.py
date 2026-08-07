"""
ROVERT Main Controller
======================

Controls:

Laptop
 |
 | HTTP
 |
ESP32-CAM
 |
 | UART
 |
Arduino Mega
"""

import time

from communication.esp_client import ESPClient
from vision.camera import CameraStream
from vision.detector import ObjectDetector


def main():

    print("Starting ROVERT...")

    # -----------------------------
    # ESP32 Connection
    # -----------------------------

    esp = ESPClient(
        ip="192.168.1.100"   # change this to ESP32 IP
    )

    if esp.test_connection():
        print("ESP32 connected")
    else:
        print("ESP32 not connected")


    # -----------------------------
    # Vision System
    # -----------------------------

    camera = CameraStream(
        esp.stream_url
    )

    detector = ObjectDetector()

    print("Vision system loaded")


    # -----------------------------
    # Main Loop
    # -----------------------------

    try:

        while True:


            # Get camera frame

            frame = camera.get_frame()


            if frame is not None:

                detections = detector.detect(frame)

                print(
                    "Objects:",
                    detections
                )


            # Get sensors

            sensors = esp.get_sensor_data()

            print(
                "Sensors:",
                sensors
            )


            # Example movement logic

            if sensors["ir_event"]:

                esp.send_command("S")

            else:

                esp.send_command("F")


            time.sleep(0.1)



    except KeyboardInterrupt:

        print("\nStopping ROVERT...")


        camera.stop()



if __name__ == "__main__":

    main()
