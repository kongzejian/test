import cv2
import numpy as np
import glob

def imgBrightness(img1, c, b):
    rows, cols, channels = img1.shape
    blank = np.zeros([rows, cols, channels], img1.dtype)
    rst = cv2.addWeighted(img1, c, blank, 1 - c, b)
    return rst
nums=1
for files in glob.glob(r'C:\Users\kongzejian\PycharmProjects\map\angle_data_set\right\*.jpg'):
    img=cv2.imread(files)
    opfile=r'C:\Users\kongzejian\PycharmProjects\map\angle_data_set\right'
    for j in range(5,15,1):
        o=imgBrightness(img,j/10,0)
        image_path=opfile+'('+str(nums)+')'+'.jpg'
        cv2.imwrite(image_path,o)
        nums+=1
        print(nums)