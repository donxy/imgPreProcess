import cv2
import numpy as np

path1 =r'H:\picture\background\backg1.jpg'
path2 =r'H:\picture\logo\logo.jpg'

src1 = cv2.imread(path1)
src2 = cv2.imread(path2)

#image resize
img1 = cv2.resize(src1 ,dsize=(640,480))
img2 = cv2.resize(src2,dsize =(100,100))
cv2.imshow('src1',img1)
cv2.imshow('src2',img2)

rows,cols, channels = img2.shape
rdr = np.random.randint(0,540)
rdc = np.random.randint(0,480)

img1[rdr:(rdr+rows) , rdc:(rdc+cols)] = img2


cv2.imshow('img',img1)

cv2.waitKey(0)
cv2.destroyAllWindows()


