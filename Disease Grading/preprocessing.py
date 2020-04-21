import os
import numpy as np
import matplotlib.pyplot as plt
import cv2

image_path = "H:/Research Projects/Diabetic Retinopathy/idrid/B. Disease Grading/B. Disease Grading/1. Original Images/a. Training Set"

def loadImages(path):
    
    image_files = sorted([os.path.join(path, file)
                          for file in os.listdir(path)])
    return image_files

#Process for all th images
def process(data):
    for i in data:
        img = cv2.imread(i)
        img = img[0:3000,300:3670]
        

def main():
    global image_path
    '''The var Dataset is a list with all images in the folder '''
    dataset = loadImages(image_path)
    print('number of FILES in dir', len(dataset))

    #print(cv2.imread(dataset[0]).shape)
    
    print("List of files the first 3 in the folder:\n",dataset[:3])
    img = cv2.imread(dataset[52])
    plt.imshow(img)
    plt.show()
    crop = img[0:3000,300:3670]
    plt.imshow(crop)
    plt.show()
    width = 300
    height = 300
    dim = (width, height)
 
    # resize image
    resized = cv2.resize(crop, dim, interpolation = cv2.INTER_AREA)
    plt.imshow(resized)
    plt.show()
    
    blurred = cv2.blur(resized, ksize=(15, 15))
    diff = resized - blurred
    plt.imshow(diff)
    plt.show()
    

 
main()