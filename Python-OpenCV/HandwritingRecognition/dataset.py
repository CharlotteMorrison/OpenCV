# dataset to train the machine learning model
# using MNIST sample (full dataset available from Kaggle)
import imutils
import numpy as np
import mahotas
import cv2


def load_digits(datasetpath):
    # this dataset contains pixel intensities from 0-255
    data = np.genfromtxt(datasetpath, delimiter=",", dtype="uint8")
    target = data[:, 0]
    data = data[:, 1:].reshape(data.shape[0], 28, 28)

    return data, target


def deskew(image, width):
    (h, w) = image.shape[:2]
    moments = cv2.moments(image)

    skew = moments["mu11"] / moments["mu02"]
    m = np.float32([[1, skew, -0.5 * w * skew], [0, 1, 0]])
    image = cv2.warpAffine(image, m, (w, h),
                           flags=cv2.WARP_INVERSE_MAP | cv2.INTER_LINEAR)

    image = imutils.resize(image, width=width)

    return image


def center_extent(image, size):
    (eW, eH) = size

    if image.shape[1] > image.shape[0]:
        image = imutils.resize(image, width=eW)
    else:
        image = imutils.resize(image, height=eH)

    extent = np.zeros((eH, eW), dtype="uint8")

    offsetx = (eW - image.shape[1]) // 2
    offsety = (eH - image.shape[0]) // 2

    extent[offsety:offsetx + image.shape[0], offsetx:offsety + image.shape[1]] = image

    cm = mahotas.center_of_mass(extent)
    (cY, cX) = np.round(cm).astype("int32")
    (dX, dY) = ((size[0] // 2) - cX, (size[1] // 2) - cY)
    m = np.float32([[1, 0, dX], [0, 1, dY]])
    extent = cv2.warpAffine(extent, m, size)

    return extent
