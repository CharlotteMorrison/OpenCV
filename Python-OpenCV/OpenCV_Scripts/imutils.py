import numpy as np
import cv2


def translate(image, x, y):
    # define translation floating point matrix M
    # first row [1, 0, ?]  ? = num of pixels to left/right (neg to shift left)
    # second row [0, 1, ?] ? = num of pixels up/down (neg to shift up)
    m = np.float32([[1, 0, x], [0, 1, y]])

    # translate image, using matrix M, (width, height)
    shifted = cv2.warpAffine(image, m, (image.shape[1], image.shape[0]))

    return shifted


def rotate(image, angle, center=None, scale=1.0):
    (h, w) = image.shape[:2]

    if center is None:
        center = (w // 2, h // 2)

    m = cv2.getRotationMatrix2D(center, angle, scale)
    rotated = cv2.warpAffine(image, m, (w, h))

    return rotated


def resize(image, width=None, height=None, inter=cv2.INTER_AREA):
    dim = None
    (h, w) = image.shape[:2]

    if width is None and height is None:
        return image

    if width is None:
        r = height / float(h)
        dim = (int(w * r), height)

    else:
        r = width / float(w)
        dim = (width, int(h * r))

    resized = cv2.resize(image, dim, interpolation=inter)

    return resized

# add flipping and crop to this
