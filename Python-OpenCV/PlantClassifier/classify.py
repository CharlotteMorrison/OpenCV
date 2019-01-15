from __future__ import print_function
from rgbhistogram import RGBHistogram
from sklearn.preprocessing import LabelEncoder
from sklearn.ensemble import RandomForestClassifier
from sklearn.cross_validation import train_test_split
from sklearn.metrics import classification_report
import numpy as np
import argparse
import glob
import cv2

ap = argparse.ArgumentParser()
ap.add_argument("-i", "--images", required=True,
                help="path to image dataset")
ap.add_argument("-m", "--masks", required=True,
                help="path to the image masks")
args = vars(ap.parse_args())

imagepaths = sorted(glob.glob(args["images"] + "/*.png"))
maskpaths = sorted(glob.glob(args["masks"] + "/*.png"))

data = []
target = []

desc = RGBHistogram([8, 8, 8])

for (imagepath, maskpath) in zip(imagepaths, maskpaths):
    image = cv2.imread(imagepath)
    mask = cv2.imread(maskpath)
    mask = cv2.cvtColor(mask, cv2.COLOR_BGR2GRAY)

    features = desc.describe(image, mask)

    data.append(features)
    target.append(imagepath.split("_")[-2])

targetnames = np.unique(target)
le = LabelEncoder()
target = le.fit_transform(target)

(traindata, testdata, traintarget, testtarget) = train_test_split(
    data, target, test_size=0.3, random_state=42)

model = RandomForestClassifier(n_estimators=25, random_state=84)
model.fit(traindata, traintarget)

print(classification_report(testtarget, model.predict(testdata),
                            target_names=targetnames))

for i in np.random.choice(np.arange(0, len(imagepaths)), 10):
    imagepath = imagepaths[i]
    maskpath = maskpaths[i]

    image = cv2.imread(imagepath)
    mask = cv2.imread(maskpath)
    mask = cv2.cvtColor(mask, cv2.COLOR_BGR2GRAY)

    features = desc.describe(image, mask)

    flower = le.inverse_transform(model.predict([features]))[0]
    print(imagepath)
    print("I thing the flower is a {}.".format(flower.upper()))
    cv2.imshow("image", image)
    cv2.waitKey(0)
