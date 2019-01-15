import cv2
import numpy as np
import os


# iterate through all the files and create an array of file names

path = '/path to files'

folder = os.fsencode(path)

filenames = []

for file in os.listdir(folder):
    filename = os.fsdecode(file)
    if filename.endswith('.png'):
        filenames.append(filename)
filenames.sort()

# write out a quick text file with names if this shit runs slowly...
