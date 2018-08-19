import numpy as np
import argparse
import cv2

ap = argparse.ArgumentParser()
ap.add_argument("-i", "--image", required=True, help="Path to the image.")
args = vars(ap.parse_args())

image = cv2.imread(args["image"])
cv2.imshow("Original", image)
cv2.waitKey(0)

# find the height and width if not known.
height, width, channels = image.shape
print(height, width, channels)

cropped = image[30:120, 30:120]

cv2.imshow("Doggo Crop", cropped)
cv2.waitKey(0)