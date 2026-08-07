from communication.esp_client import ESPClient
from vision.camera import CameraStream
from vision.detector import ObjectDetector

import argparse



def main():

    parser = argparse.ArgumentParser(
        description="ROVERT Control System"
    )


    parser.add_argument(
        "--ip",
        required=True,
        help="ESP32-CAM IP address"
    )


    args = parser.parse_args()


    print("Starting ROVERT...")


    esp = ESPClient(
        args.ip
    )


    camera = CameraStream(
        esp.stream_url
    )


    detector = ObjectDetector()


    print(
        f"Connected to ESP32-CAM: {args.ip}"
    )

    print(
        "ROVERT initialized successfully."
    )


    try:

        while True:

            frame = camera.get_frame()


            if frame is None:
                continue


            detections = detector.detect(
                frame
            )


            print(
                detections
            )


    except KeyboardInterrupt:

        print(
            "\nStopping ROVERT..."
        )


    finally:

        camera.stop()



if __name__ == "__main__":

    main()
