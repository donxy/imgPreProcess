import numpy as np
import cv2
from matplotlib import pyplot as plt
def get_img(path):
    img = cv2.imread(path)
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    return img,gray

def Gaussian_Blur(gray):
    blurred = cv2.GaussianBlur(gray,(9,9),0)

    return blurred

def sobel_gradient(blurred):
    grad_x = cv2.Sobel(blurred,ddepth=cv2.CV_32F,dx=1,dy=0)
    grad_y = cv2.Sobel(blurred,ddepth=cv2.CV_32F,dx=0,dy=1)

    gradient = cv2.subtract(grad_x,grad_y)
    gradient = cv2.convertScaleAbs(gradient)

    return grad_x,grad_y,gradient

def Thresh_and_blur(gradient):
    blurred = cv2.GaussianBlur(gradient,(9,9),0)
    (_, thresh) = cv2.threshold(blurred,90,255,cv2.THRESH_BINARY)

    return thresh


    

def work():
    img_path = r'D:\image\sign\sign1.jpg'
    srcImg,grayImg = get_img(img_path)
    blurImg = Gaussian_Blur(grayImg)
    grad_x,grad_y,gradImg = sobel_gradient(blurImg)
    thresh = Thresh_and_blur(gradImg)


    #imgshow
    plt.subplot(221), plt.imshow(srcImg)
    plt.title('Original Image'), plt.xticks([]), plt.yticks([])
    plt.subplot(222), plt.imshow(grayImg)
    plt.title('Gray Image'), plt.xticks([]), plt.yticks([])
    plt.subplot(223), plt.imshow(blurImg)
    plt.title('Blur Image'), plt.xticks([]), plt.yticks([])
    plt.subplot(224), plt.imshow(gradImg)
    plt.title('Grad Image'), plt.xticks([]), plt.yticks([])

    plt.show()

work()