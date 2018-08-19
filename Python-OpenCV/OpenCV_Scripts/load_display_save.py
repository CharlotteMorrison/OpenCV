from __future__ import print_function
import argparse
import cv2

# use argparse to handle paring the command line arguements
ap = argparse.ArgumentParser()
ap.add_argument("-i", "--image", required=True, help="Path to the Image")
args = vars(ap.parse_args())

# load an image off a disk
image = cv2.imread(args["image"])

# examine the image
print("width: {} pixels".format(image.shape[1]))
print("height: {} pixels".format(image.shape[0]))
print("channels: {}".format(image.shape[2]))

# show the image on the screen, param1 is the name of screen, param2 is the image on disk
cv2.imshow("Image", image)

# write image as a .png file
cv2.imwrite("sample.jpg", image)

# wait for a keypress to exit (0=anykey)
cv2.waitKey(0)
