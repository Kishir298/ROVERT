"""
ROVERT Main Control System
==========================

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
        ip="192.168.1.100"
    )


    esp_connected = esp.test_connection()


    if esp_connected:
        print("ESP32 connected")
    else:
        print("ESP32 not connected")


    # -----------------------------
    # Vision System
    # -----------------------------

    camera = None


    if esp_connected:

        camera = CameraStream(
            esp.stream_url
        )

        print("Camera connected")

    else:

        print("Camera disabled (ESP32 offline)")


    detector = ObjectDetector()

    print("Vision system loaded")


    # -----------------------------
    # Main Loop
    # -----------------------------

    try:

        while True:


            # -----------------------------
            # Camera Detection
            # -----------------------------

            if camera:

                frame = camera.get_frame()

            else:

                frame = None



            if frame is not None:

                detections = detector.detect(frame)

                print(
                    "Objects:",
                    detections
                )



            # -----------------------------
            # Sensor Data
            # -----------------------------

            sensors = esp.get_sensor_data()


            print(
                "Sensors:",
                sensors
            )



            # -----------------------------
            # Movement Logic
            # -----------------------------

            if sensors["ir_event"]:

                esp.send_command("S")

            else:

                esp.send_command("F")



            time.sleep(0.1)



    except KeyboardInterrupt:

        print("\nStopping ROVERT...")



    finally:

        if camera:

            camera.stop()



        print("ROVERT stopped.")



if __name__ == "__main__":

    main()