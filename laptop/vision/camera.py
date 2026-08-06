"""
ROVERT Camera Module
====================

Handles receiving video frames from the ESP32-CAM stream.
"""

import cv2
import threading
import time


class CameraStream:

    def __init__(self, stream_url):

        self.stream_url = stream_url

        self.capture = cv2.VideoCapture(stream_url)

        self.latest_frame = None

        self.running = True

        self.lock = threading.Lock()

        self.thread = threading.Thread(
            target=self._update,
            daemon=True
        )

        self.thread.start()



    def _update(self):

        """
        Continuously reads frames in the background.
        This prevents old buffered frames creating lag.
        """

        while self.running:

            if not self.capture.isOpened():
                self.capture = cv2.VideoCapture(
                    self.stream_url
                )

                time.sleep(0.5)
                continue


            success, frame = self.capture.read()


            if success:

                with self.lock:
                    self.latest_frame = frame

            else:
                time.sleep(0.05)



    def get_frame(self):

        """
        Returns the newest available frame.
        """

        with self.lock:

            if self.latest_frame is None:
                return None

            return self.latest_frame.copy()



    def stop(self):

        """
        Stops camera thread.
        """

        self.running = False

        self.capture.release()