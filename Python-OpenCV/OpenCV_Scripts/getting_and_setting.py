from __future__ import print_function
import argparse
import cv2

# use argparse to handle paring the command line arguements
ap = argparse.ArgumentParser()
ap.add_argument("-i", "--image", required=True, help="Path to the Image")
args = vars(ap.parse_args())

# load an image off a disk
image = cv2.imread(args["image"])

# show the image
cv2.imshow("Original", image)

# openCV stores pixes in blue-green-red (reverse order)

# grab pixel at (0,0)
(b, g, r,) = image[0, 0]

# prints out the value of the pixel
print("Pixel at (0,0) - Red: {}, Green: {}, Blue: {}".format(r, g, b))

# change the pixel value of (0,0)
image[0, 0] = (0, 0, 255)

# after changing pixel- regrab it and check that it has changed
(b, g, r) = image[0, 0]
print("Pixel at (0, 0) - Red: {}, Green: {}, Blue: {}".format(r, g, b))

# ******geting a rectangular section of the image

# specify the y:y and x:x values of square
corner = image[0:100, 0:100]
cv2.imshow("Corner", corner)

# change the colr of the region
image[0:100, 0:100] = (0, 255, 0)

(b, g, r,) = image[90, 219]
print("Pixel at (90,219) - Red: {}, Green: {}, Blue: {}".format(r, g, b))

cv2.imshow("Updated", image)
cv2.waitKey(0)
