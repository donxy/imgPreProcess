import cv2
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
img = cv2.imread('E:\picture\syz3.jpg')
#img = cv2.resize(img,(300,300))
##尺度操作
def scale_transform(img):
    img_rs2 = cv2.resize(img,(0,0),fx=0.5,fy=0.5,interpolation=cv2.INTER_NEAREST)
    #上下左右补边
    img_broder = cv2.copyMakeBorder(img,50,50,20,20,borderType=cv2.BORDER_CONSTANT,value=(0,0,0))
    #裁剪
    img_crop = img[100:200,-200:-100]
    cv2.imshow('src', img)
    cv2.imshow('broder', img_broder)
    cv2.imshow('crop', img_crop)
    cv2.waitKey(0)

##颜色操作
def color_transform(img):
    img_hsv = cv2.cvtColor(img,cv2.COLOR_RGB2HSV)
    #H空间变化，绿色比黄色要高一点
    hsv1 = img_hsv.copy()
    hsv1[:,:,0] = (hsv1[:,:,0] + 50)%180
    rgb1 = cv2.cvtColor(hsv1,cv2.COLOR_HSV2BGR)
    #减少饱和度，会降低图片鲜艳程度，即会让图片变灰
    hsv2 = img_hsv.copy()
    hsv2[:,:,1] = 0.5*hsv2[:,:,1]
    rgb2 = cv2.cvtColor(hsv2,cv2.COLOR_HSV2BGR)
    #V通道，减少亮度为原来一半
    hsv3 = img_hsv.copy()
    hsv3[:,:,2] = 0.5*hsv3[:,:,2]
    rgb3 = cv2.cvtColor(hsv3,cv2.COLOR_HSV2BGR)
    cv2.imshow('src', img)
    cv2.imshow('hsv', img_hsv)
    cv2.imshow('H_space', rgb1)
    cv2.imshow('S_space', rgb2)
    cv2.imshow('V_space', rgb3)
    cv2.waitKey(0)

def gamma_trans(img, gamma):
    # 具体做法是先归一化到1，然后gamma作为指数值求出新的像素值再还原
    gamma_table = [np.power(x / 255.0, gamma) * 255.0 for x in range(256)]
    gamma_table = np.round(np.array(gamma_table)).astype(np.uint8)

    # 实现这个映射用的是OpenCV的查表函数
    return cv2.LUT(img, gamma_table)


def hist_statis(img):
    hist_b = cv2.calcHist([img],[0],None,[256],[0,256])
    hist_g = cv2.calcHist([img],[1],None,[256],[0,256])
    hist_r = cv2.calcHist([img],[2],None,[256],[0,256])

    # 执行Gamma矫正，小于1的值让暗部细节大量提升，同时亮部细节少量提升
    img_corrected = gamma_trans(img, 0.5)

    # 分通道计算Gamma矫正后的直方图
    hist_b_corrected = cv2.calcHist([img_corrected], [0], None, [256], [0, 256])
    hist_g_corrected = cv2.calcHist([img_corrected], [1], None, [256], [0, 256])
    hist_r_corrected = cv2.calcHist([img_corrected], [2], None, [256], [0, 256])

    # 将直方图进行可视化

    fig = plt.figure()
    pix_hists = [
        [hist_b, hist_g, hist_r],
        [hist_b_corrected, hist_g_corrected, hist_r_corrected]
    ]
    pix_vals = range(256)
    for sub_plt, pix_hist in zip([121, 122], pix_hists):
        ax = fig.add_subplot(sub_plt, projection='3d')
        for c, z, channel_hist in zip(['b', 'g', 'r'], [20, 10, 0], pix_hist):
            print('c',c)
            print('z',z)
            cs = [c] * 256
            print('[c]',cs)
            ax.bar(pix_vals, channel_hist, zs=z, zdir='y', color=cs, alpha=0.618, edgecolor='none', lw=0)

            ax.set_xlabel('Pixel Values')
            ax.set_xlim([0, 256])
            ax.set_ylabel('Channels')
            ax.set_zlabel('Counts')

    plt.show()


hist_statis(img)