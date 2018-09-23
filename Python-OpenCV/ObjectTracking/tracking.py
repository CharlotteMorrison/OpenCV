import numpy as np
import argparse
import time
import cv2

ap = argparse.ArgumentParser()
ap.add_argument("-v", "--video", required=False,
                help="path to video file (optional)")
args = vars(ap.parse_args())

# track something blue- could use any color
# setting the upper and lower bounds of the color
# colors are in reverse order in cv2
blueLower = np.array([100, 67, 0], dtype="uint8")
blueUpper = np.array([255, 128, 50], dtype="uint8")

if not args.get("video", False):
    camera = cv2.VideoCapture(0)

else:
    camera = cv2.VideoCapture(args["video"])

while True:
    (grabbed, frame) = camera.read()
    if not grabbed:
        break

    # checks if the pixes in the frame are in the range
    # if upper, set to white, if lower set to black
    blue = cv2.inRange(frame, blueLower, blueUpper)
    # blur the image to make contours more accurate
    blue = cv2.GaussianBlur(blue, (3, 3), 0)

    (_, cnts, _) = cv2.findContours(blue.copy(), cv2.RETR_EXTERNAL,
                                    cv2.CHAIN_APPROX_SIMPLE)

    if len(cnts) > 0:
        cnt = sorted(cnts, key=cv2.contourArea, reverse=True)[0]

        rect = np.int32(cv2.boxPoints(cv2.minAreaRect(cnt)))
        cv2.drawContours(frame, [rect], -1, (0, 255, 0), 2)

    cv2.imshow("Tracking", frame)
    cv2.imshow("Binary", blue)

    time.sleep(0.025)

    if cv2.waitKey(1) & 0xFF == ord("q"):
        break

camera.release()
cv2.destroyAllWindows()
