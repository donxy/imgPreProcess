import cv2
import numpy as np
import  os

RED = [0, 0, 255]
rect = (0, 0, 1, 1)
drawing = False
rectangle = False
rect_over = False
rect_or_mask = 100
thickness = 2

def rectangle_roi(event,x,y,flag,param):
    global img,img2,dst,drawing,mask,rectangle,rect,rect_or_mask,ix,iy,rect_over

    if event == cv2.EVENT_RBUTTONDOWN:
        rectangle = True
        ix , iy = x , y
    elif event == cv2.EVENT_MOUSEMOVE:
        if rectangle == True:
            img = img2.copy()
            cv2.rectangle(img,(ix,iy),(x,y), RED ,thickness)
            rect = (min(ix,x),min(iy,y),abs(ix -x),abs(iy-y))
            rect_or_mask = 0

    elif event == cv2.EVENT_RBUTTONUP:
        rectangle = False
        rect_over = True
        cv2.rectangle(img,(ix,iy),(x,y),RED,thickness)
        rect = (min(ix,x),min(iy,y),abs(ix-x),abs(iy-y))
        rect_or_mask = 0

dir1_path = r'H:\picture\background'
dir_fg_path = r'H:\picture\logo'
dir_save_path = r'H:\picture\logo'

all_img1 =os.listdir(dir_fg_path)

for i in all_img1:
    print(i)
    img1 =cv2.imread(dir_fg_path+'/'+i)
    img = cv2.resize(img1,(640,480))
    img2 = img.copy()
    cv2.namedWindow('input')
    cv2.setMouseCallback('input',rectangle_roi)
    print("Draw a rectangle around the object using right mouse button \n")
    while(1):
        cv2.imshow('input',img)
        k = cv2.waitKey(1)
        if k == 27:
            break
        elif k == ord('r'):
            print('resetting \n')
            rect = (0,0,1,1)
            drawing = False
            rectangle = False
            rect_or_mask = 100
            rect_over = False
            img = img2.copy()
        elif k == ord('n'):
            if(rect_or_mask == 0):
                x1,y1,x2,y2 = rect
                dst = img[(y1+2):(y1+y2)-2,(x1+2):(x1+x2-2)]
                cv2.imshow('dst',dst)
                cv2.waitKey(0)

        elif k == ord('s'):
            x1,y1,x2,y2 = rect
            dst = img[(y1 + 2):(y1 + y2) - 2, (x1 + 2):(x1 + x2 - 2)]
            roi_title = i
            cv2.imwrite(dir_save_path+'/'+roi_title,dst)

    #cv2.waitKey(0)

