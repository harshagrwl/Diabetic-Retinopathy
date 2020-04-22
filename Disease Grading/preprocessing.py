import os
import numpy as np
import matplotlib.pyplot as plt
import cv2

#image_path = "H:/Research Projects/Diabetic Retinopathy/idrid/B. Disease Grading/B. Disease Grading/1. Original Images/a. Training Set"
#image_path = "D:\\ML\\DR\\datasets\\B. Disease Grading\\1. Original Images\\a. Training Set"


#Process for all th images
def process(i):
    img = cv2.imread(i)
    img = img[0:3000,300:3670]
    width = 300
    height = 300
    dim = (width, height)

    # resize image
    resized = cv2.resize(img, dim, interpolation = cv2.INTER_AREA)
    blurred = cv2.blur(resized, ksize=(15, 15))
    diff = resized - blurred
    return diff
