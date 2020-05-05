import numpy as np
import matplotlib.pyplot as plt
import os

dir = "patches"
image_paths = os.listdir(dir)

length = len(image_paths)
img_paths = np.empty(length, dtype=object)

i=0
for file in image_paths:
	img_paths[i] = "patches/" + file
	print (img_paths[i])
	i+=1

# print (img_paths)
np.random.shuffle(img_paths)
split_idx = int(img_paths.shape[0] * 0.7)
train_paths = img_paths[:split_idx]
test_paths = img_paths[split_idx:]

train_paths_ = np.copy(train_paths)
test_paths_ = np.copy(test_paths)

for i in range(train_paths.size):
	train_paths_[i] = train_paths[i][12:]
	train_paths_[i] = "" + train_paths_[i]
	print (train_paths_[i])

print ("split")

for i in range(test_paths.size):
	test_paths_[i] = test_paths[i][12:]
	test_paths_[i] = "" + test_paths_[i]
	print (test_paths_[i])

train_csv = np.stack((train_paths,train_paths_), axis=1)
test_csv = np.stack((test_paths,test_paths_), axis=1)

np.savetxt("train.csv", train_csv, delimiter=",", fmt="%s")
np.savetxt("test.csv", test_csv, delimiter=",", fmt="%s")