import matplotlib.pyplot as plt

from skimage.feature import hog
from skimage import data, exposure, io
from numpy import asarray

from PIL import Image
import numpy as np
import os
import csv

fileList = []


def createFileList(myDir, format='.png'):
    print(myDir)
    for root, dirs, files in os.walk(myDir, topdown=False):
        for name in files:
            if name.endswith(format):
                fullName = os.path.join(root, name)
                fileList.append(fullName)
    return fileList


myFileList = createFileList('./images/park_')

# image = io.imread('test.png')

for file in fileList:
    print(file)

    image = io.imread(file)

    fd, hog_image = hog(image, orientations=8, pixels_per_cell=(8, 8),
                        cells_per_block=(2, 2), visualize=True)

    # print(hog_image)
    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(8, 4), sharex=True, sharey=True)

    ax1.axis('off')
    ax1.imshow(image, cmap=plt.cm.gray)
    ax1.set_title('Input image')

    # print(hog_image)
    data_ = asarray(hog_image)
    # flatten 함수를 통해 2차원 배열을 1차원으로 축소시켜준다.
    data_ = data_.flatten()
    print(data_)

    # with 함수로 함수를 열어주고 해당되는 값들을 csv 파일에 한줄씩 넣어준다.
    with open("img_csv_data_hog.csv", 'a', newline='') as f:
        writer = csv.writer(f)
        writer.writerow(data_)
