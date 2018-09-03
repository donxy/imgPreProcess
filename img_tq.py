import cv2
import numpy as np
import os
def get_img(dir_txt,dir_img,save_img,save_txt,save_train):
    all_txt_name = os.listdir(dir_txt)
    x = 0
    target = [0,2,7]
    train_txt = open(save_train,'w')
    for i in all_txt_name:
        txt = []
        fi = open(dir_txt+'/'+i,'r')
        flag_p = 0
        for line in fi:
            split = line.split()
            cls_id = int(split[0])
            if cls_id in target:
                txt.append(line)
                flag_p = 1

        if flag_p == 1:
            dict = {'0':'3','2':'4','7':'5','5':'6','6':'7','8':'8','16':'9','24':'10','26':'11','28':'12','39':'13','41':'14'}
            fi_w = open(save_txt+'/'+i,'w')
            for l in txt:
                split_l = l.split()
                a = split_l[0]
                split_l[0] = dict[a]

                fi_w.write(split_l[0] + " " + " ".join([str(a) for a in split_l[1:5]]) + '\n')
            fi_w.close()
            img_name = i.split('.')[0] + '.jpg'
            #print(img_path)
            img = cv2.imread(dir_img +'/'+img_name)
            #cv2.imshow('person',img)
            #cv2.waitKey(0)
            cv2.imwrite(save_img +'/' +img_name,img)
            train_txt.write(save_img +'/' +img_name + '\n')
            x += 1
        print('x',x)
    train_txt.close()

dir_txt = r'G:\coco\labels\val2014'
dir_img = r'G:\coco\images\val2014'
save_img = r'G:\obj_14\images\val'
save_txt = r'G:\obj_14\images\val'
save_train = r'G:\obj\val.txt'
get_img(dir_txt,dir_img,save_img,save_txt,save_train)















