import numpy as np
import cv2

# construct a numpy array 300 x 300 pixels, and allocate for 3 channels for RGB,
# dtype is unsigned 8-bit integer to hold the RGB values/ could use other values
canvas = np.zeros((300, 300, 3), dtype = "uint8")

green = (0, 255, 0)
red = (0, 0, 255)

# draw a line

cv2.line(canvas, (0, 0), (300, 300), green)
cv2.imshow("Canvas", canvas)
cv2.waitKey(0)


# added pixel width on the end
cv2.line(canvas, (300, 300), (0, 0), red, 3)
cv2.imshow("Canvas", canvas)
cv2.waitKey(0)

#rectangles
cv2.rectangle(canvas, (10, 10), (60, 60), green)
cv2.imshow("Canvas", canvas)
cv2.waitKey(0)

cv2.rectangle(canvas, (50, 200), (200, 225), red, 5)
cv2.imshow("Canvas", canvas)
cv2.waitKey(0)

blue = (255, 0, 0)
cv2.rectangle(canvas, (200, 50), (225, 125), blue, -1)
cv2.imshow("Canvas", canvas)
cv2.waitKey(0)

# reinitialize canvas blank
canvas = np.zeros((300, 300, 3), dtype = "uint8")

# create the center point (middle of canvas)
(centerX, centerY) = (canvas.shape[1] // 2, canvas.shape[0] // 2)
white = (255, 255, 255)

# draw concentric circles, starting at radius 0 incrementing by 25 until 175 (doesn't include 175)
for r in range(0, 175, 25):
    cv2.circle(canvas, (centerX, centerY), r, white)

cv2.imshow("Canvas", canvas)
cv2.waitKey(0)

# draw some random circles
for i in range(0,20):
    radius = np.random.randint(5, high = 200)
    color = np.random.randint(0, high = 256, size = (3,)).tolist()
    pt =np.random.randint(0, high = 300, size = (2,))
    cv2.circle(canvas, tuple(pt), radius, color, -1)

cv2.imshow("Canvas", canvas)
cv2.waitKey(0)

