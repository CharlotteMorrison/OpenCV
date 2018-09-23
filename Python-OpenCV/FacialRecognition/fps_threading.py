# this is for use on the raspeberry pi- not configured for windows

from __future__ import print_function
from webcamvideostream import WebcamVideoStream
from fps import FPS
import argparse
import imutils
import cv2

ap = argparse.ArgumentParser()
ap.add_argument("-n", "--num-frames", type=int, default=100,
                help="# of frames to loop over for FPS test")
ap.add_argument("-d", "--display", type=int, default=-1,
                help="whether or not frames should be displayed")
args = vars(ap.parse_args())

# grab a pointer to the video and initialize the FPS counter
print("[INFO] sampling frames from the webcam...")
stream = cv2.VideoCapture(0)
fps = FPS().start()

# loop over some frames
while fps._numFrames < args["num_frames"]:
    # grab frame, resize to max width of 400px
    (grabbed, frame) = stream.read()
    frame = imutils.resize(frame, width=400)

    # check to see if the frame should be displayed
    if args["display"] > 0:
        cv2.imshow("Frame", frame)
        key = cv2.waitKey(1) & 0xFF

    # update the FPS counter
    fps.update()

# stop the timer and display FPS info
fps.stop()
print("[INFO] elasped time: {:.2f}".format(fps.elapsed()))
print("[INFO] approx. FPS: {:.2f}".format(fps.fps()))

# cleanup
stream.release()
cv2.destroyAllWindows()

# create a threaded video stream, use FPS counter
print("[INFO] sampling THREADED frames from a webcam...")
vs = WebcamVideoStream(src=0).start()
fps = FPS().start()


# ************this is not working**********
# I believe this is a windows issue, this is for
# the raspberry pi, so will test on there before
# doing too much more here.

# loop over frames using threaded stream
while fps._numFrames < args["num_frames"]:
    # grab frame and resize to 400 px
    frame = vs.read()
    frame = imutils.resize(frame, width=400)

    # check to see if the frame should be displayed
    if args["display"] > 0:
        cv2.imshow("Frame", frame)
        key = cv2.waitKey(1) & 0xFF

    # update the FPS counter
    fps.update()

# stop the timer and display FPS information
fps.stop()
print("[INFO] elasped time: {:.2f}".format(fps.elapsed()))
print("[INFO] approx. FPS: {:.2f}".format(fps.fps()))

# cleanup
cv2.destroyAllWindows()
vs.stop()
