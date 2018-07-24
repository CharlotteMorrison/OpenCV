#imports
from imutils.video import VideoStream
import argparse
import datetime
import imutils
import time
import cv2

#adjust the cv2.threshold  and the --min-area

#construct arguement parser and parse arguments
ap = argparse.ArgumentParser()

#to use local video file add path
ap.add_argument("-v", "--video", help="path to the video file")

#get the camera stream, set a minimum sizer for motion changes (avoid noise/shadows)
ap.add_argument("-a", "--min-area", type=int, default=200, help="minimum area size")
args = vars(ap.parse_args())

#if no video file, then use webcam
if args.get("video", None) is None:
    vs = VideoStream(src=0).start()
    time.sleep(2.0)
else:
    vs = cv2.VideoCapture(args["video"])

#intialize the first frame in the video stream
firstFrame = None

#loop over frames of video
while True:
    #get the current fram and initialize the occupied/unoccupied text
    frame = vs.read()
    frame = frame if args.get("video", None) is None else frame[1]
    text = "Unoccupied"  #used to monitor if room is occupied or not

    #if the frame could not be grabbed, we are at the end/cannot be read
    if frame is None:
        break

    #resize the frame, covert to grayscale, and blur it
    frame = imutils.resize(frame, width=500) #convert it to smaller image
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY) #convert to grayscale (color not needed for motion detec)
    gray = cv2.GaussianBlur(gray, (21,21),0) #smooth the image, removes high freq noise

    #if the first frame is None, initialize it
    if firstFrame is None:
        firstFrame = gray
        continue

    #compute the absolute difference from first frame to current frame
    frameDelta = cv2.absdiff(firstFrame, gray)
    thresh = cv2.threshold(frameDelta, 15, 255, cv2.THRESH_BINARY)[1]

    #dialate the threshold image to fill holes, find contours on threshold image
    thresh = cv2.dilate(thresh, None, iterations=2)
    cnts = cv2.findContours(thresh.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    cnts = cnts[0] if imutils.is_cv2() else cnts[1]

    #loop over the contours
    for c in cnts:
        #if the contour is too small, ignore
        if cv2.contourArea(c) < args["min_area"]:
            continue
        #compute the bounding box for the contour, draw it on the frame and update text
        (x, y, w, h) = cv2.boundingRect(c)
        cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)
        text = "Occupied"

    #draw the text and timestamp on the frame
    cv2.putText(frame, "Room Status: {}".format(text), (10, 20),
                cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 0, 255), 2)
    cv2.putText(frame, datetime.datetime.now().strftime("%A %d %B %Y %I:%M:%S%p"),
                (10, frame.shape[0] - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.35, (0, 0, 255), 1)

    #show the fram and record if a key is pressed
    cv2.imshow("Security Feed", frame)
    cv2.imshow("Thresh", thresh)
    cv2.imshow("Frame Delta", frameDelta)
    key = cv2.waitKey(1) & 0xFF

    #if q is pressed, quit
    if key == ord("q"):
        break

#clean up camera and close window
vs.sto if args.get("video", None) is None else vs.release()
cv2.destroyAllWindows()
