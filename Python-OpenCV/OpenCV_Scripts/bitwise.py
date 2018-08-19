import numpy as np
import cv2

rectangle = np.zeros((300, 300), dtype="uint8")
cv2.rectangle(rectangle, (25, 25), (275, 275), 255, -1)
cv2.imshow("Rectangle", rectangle)

circle = np.zeros((300, 300), dtype="uint8")
cv2.circle(circle, (150, 159), 150, 255, -1)
cv2.imshow("Circle", circle)
cv2.waitKey(0)

# 1. AND: A bitwise AND is true if and only if both pixels are greater than zero.
# 2. OR: A bitwise OR is true if either of the two pixels are greater than zero.
# 3. XOR: A bitwise XOR is true if and only if either of the two pixels are greater than zero, but not both.
# 4. NOT: A bitwise NOT inverts the “on” and “off” pixels in an image.

bitwiseAnd = cv2.bitwise_and(rectangle, circle)
cv2.imshow("AND", bitwiseAnd)
cv2.waitKey(0)

bitwiseOr = cv2.bitwise_or(rectangle, circle)
cv2.imshow("OR", bitwiseOr)
cv2.waitKey(0)

bitwiseXor = cv2.bitwise_xor(rectangle, circle)
cv2.imshow("XOR", bitwiseXor)
cv2.waitKey(0)

bitwiseNot = cv2.bitwise_not(rectangle, circle)
cv2.imshow("NOT", bitwiseNot)
cv2.waitKey(0)
