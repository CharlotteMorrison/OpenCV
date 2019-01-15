import simple_barcode_detection
import argparse
import cv2

# construct the argument and parse
ap = argparse.ArgumentParser()
ap.add_argument("-v", "--video", help="path to optional video file")
args = vars(ap.parse_args())

# if no video, grab camera reference
if not args.get("video", False):
    camera = cv2.VideoCapture(0)

# otherwise load video
else:
    camera = cv2.VideoCapture(args["video"])

# keep looping over frames
while True:
    # grab frame
    (grabbed, frame) = camera.read()

    # check for last frame
    if not grabbed:
        break

    # detect barcode
    box = simple_barcode_detection.detect(frame)

    # draw bounding box
    cv2.drawContours(frame, box, -1, (0, 255, 0), 3)

    # show frame, record if key pressed
    cv2.imshow("Frame", frame)
    key = cv2.waitKey(1) & 0xFF

    # if q, then quit
    if key == ord("q"):
        break

# cleanup and close windows
camera.release()
cv2.destroyAllWindows()
