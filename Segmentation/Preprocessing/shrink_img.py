from PIL import Image
from skimage import data, io, filters
import numpy as np
import scipy.misc as misc
from sklearn import manifold, datasets

image_path = "\\ML\\DR\\unet\\data\\membrane\\train\\image\\"
save_path = 'C:\\Users\\Akshara\\Downloads\\test_img\\'
n=1 #number of images

for i in range (1,n+1):
	path='IDRiD_'+str(i)+'.jpg'
	img= io.imread(image_path+path)
	
	image = np.array(img)
	resize_image = misc.imresize(image,[320, 320], interp='nearest')
	print(resize_image.shape)
	path=str(i-1)+'.tif'
	io.imsave(save_path+path,resize_image)
print("Done")
