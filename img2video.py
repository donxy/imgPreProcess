import cv2
import os

def img2video(img_path,video_path,size):
    img_list = os.listdir(img_path)
    fps = 12
    fourcc = cv2.VideoWriter_fourcc('D', 'I', 'V', 'X')
    video = cv2.VideoWriter(video_path,fourcc,fps,size)
    for i in img_list:

        if i.endswith('.jpg'):
            ip = img_path + '/' +i
            img = cv2.imread(ip)
            img1 = cv2.resize(img, size)
            video.write(img1)
            print(i)
    video.release()

def video2img(video_path,i,img_save_path):
    vd = cv2.VideoCapture(video_path)
    flag = vd.isOpened()
    c = 0
    while(flag):
        c += 1
        video,frame = vd.read()
        if c%60 == 0:
            cv2.imshow('vd',frame)
            cv2.waitKey(1000)
            cv2.imwrite(img_save_path+'/'+i+str(c/60)+'.jpg',frame)
            print(c)
    vd.release()


# img_path = r'E:\picture\car'
# video_path = r'E:\picture\car.mp4'
# size = (640,640)
# img2video(img_path,video_path,size)
video_path = r'G:/数据集'
img_save_path = r'G:/数据集/caiji'
dir_list = os.listdir(video_path)
for i in dir_list:
    if i.split('.')[-1] == 'avi':
        print(i)
        video2img(video_path+'/'+i,i.split('.')[0],img_save_path)