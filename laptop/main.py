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


import sys
import time

from communication.esp_client import ESPClient
from vision.camera import CameraStream
from vision.detector import ObjectDetector



def main():


    print("Starting ROVERT...")



    # -----------------------------
    # ESP32 IP Configuration
    # -----------------------------

    if len(sys.argv) > 1:

        esp_ip = sys.argv[1]

    else:

        esp_ip = "192.168.1.100"



    print(
        f"Using ESP32 IP: {esp_ip}"
    )



    # -----------------------------
    # ESP32 Connection
    # -----------------------------
    esp = ESPClient()



    if esp.test_connection():

        print("ESP32 connected")

        esp_connected = True


    else:

        print("ESP32 not connected")

        esp_connected = False



    # -----------------------------
    # Camera System
    # -----------------------------

    camera = None



    if esp_connected:


        camera = CameraStream(
            esp.stream_url
        )


        print(
            "Camera connected"
        )


    else:


        print(
            "Camera disabled (ESP32 offline)"
        )



    # -----------------------------
    # Object Detection
    # -----------------------------

    detector = ObjectDetector()


    print(
        "Vision system loaded"
    )



    # -----------------------------
    # Main Loop
    # -----------------------------

    try:


        while True:



            # Camera frame

            if camera:

                frame = camera.get_frame()


            else:

                frame = None




            # Object detection

            if frame is not None:


                detections = detector.detect(
                    frame
                )


                print(
                    "Objects:",
                    detections
                )




            # Sensor data

            sensors = esp.get_sensor_data()



            print(
                "Sensors:",
                sensors
            )




            # Movement logic

            if sensors.get("ir_event"):


                esp.send_command(
                    "S"
                )


            else:


                esp.send_command(
                    "F"
                )




            time.sleep(0.1)




    except KeyboardInterrupt:


        print(
            "\nStopping ROVERT..."
        )




    finally:


        if camera:

            camera.stop()



        print(
            "ROVERT stopped."
        )




if __name__ == "__main__":

    main()
