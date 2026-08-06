"""
ROVERT Object Detector
======================

YOLO-based object detection module.

Uses YOLOv8 for detecting objects from
ESP32-CAM frames.
"""

from ultralytics import YOLO

from config.settings import (
    YOLO_MODEL,
    CONFIDENCE_THRESHOLD,
    CLOSE_OBJECT_AREA_THRESHOLD
)


class ObjectDetector:

    def __init__(self, model_path=YOLO_MODEL):

        self.model = YOLO(model_path)



    def detect(self, frame):

        """
        Runs YOLO detection on a frame.

        Returns:
            list of detected objects
        """

        detections = []

        results = self.model.predict(
            frame,
            verbose=False,
            conf=CONFIDENCE_THRESHOLD
        )


        for result in results:

            for box in result.boxes:

                class_id = int(box.cls[0])

                name = self.model.names[class_id]

                confidence = float(box.conf[0])


                x1, y1, x2, y2 = (
                    box.xyxy[0].tolist()
                )


                detections.append({

                    "name": name,

                    "confidence": confidence,

                    "bbox": [
                        x1,
                        y1,
                        x2,
                        y2
                    ]

                })


        return detections



    def obstacle_detected(self, frame):

        """
        Checks if an object is close enough
        to trigger avoidance.

        Uses bounding box size as an estimate.
        """

        height, width = frame.shape[:2]

        frame_area = height * width


        objects = self.detect(frame)


        for obj in objects:

            x1, y1, x2, y2 = obj["bbox"]


            object_area = (
                (x2 - x1) *
                (y2 - y1)
            )


            area_ratio = (
                object_area /
                frame_area
            )


            if area_ratio >= CLOSE_OBJECT_AREA_THRESHOLD:

                return True


        return False