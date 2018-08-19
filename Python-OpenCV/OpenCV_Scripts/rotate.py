import numpy as np
import argparse
import imutils
import cv2

ap = argparse.ArgumentParser()
ap.add_argument("-i", "--image", required=True, help="Path to the image.")
args = vars(ap.parse_args())

image = cv2.imread(args["image"])
cv2.imshow("Original", image)

rotated = imutils.rotate(image, 190)
cv2.imshow("Rotated by 180 Degrees", rotated)

cv2.waitKey(0)
