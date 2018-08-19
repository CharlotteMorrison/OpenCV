import numpy as np
import argparse
import imutils
import cv2

ap = argparse.ArgumentParser()
ap.add_argument("-i", "--image", required=True, help="Path to the image.")
args = vars(ap.parse_args())

image = cv2.imread(args["image"])
cv2.imshow("Original", image)
cv2.waitKey(0)

resized = imutils.resize(image, height=50)
cv2.imshow("Resize 1", resized)
cv2.waitKey(0)

resized = imutils.resize(image, height=250)
cv2.imshow("Resize 2", resized)
cv2.waitKey(0)

resized = imutils.resize(image, height=100)
cv2.imshow("Resize 3", resized)
cv2.waitKey(0)
