from threading import Thread
import cv2


class WebcamVideoStream:
    def __init__(self, src=0):
        self.stream = cv2.VideoCapture(src)
        (self.grabbed, self.frame) = self.stream.read()

        self.stopped = False

    def start(self):
        # start the thread to read frames from stream
        Thread(target=self.update, args=()).start()
        return self

    def update(self):
        # keep looping until the thread is stopped
        while True:
            if self.stopped:
                return
            (self.grabbed, self.frame) = self.stream.read()

    def read(self):
        # return frame most recently read
        return self.frame

    def stop(self):
        # stop the thread
        self.stopped = True
