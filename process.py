import cv2
import numpy as np
import os

dir1_path = r'H:\picture\background'
dir3_path = r'H:\picture\logo'
dir_save = r'H:picture\img'
all_img1 = os.listdir(dir1_path)

all_img3 = os.listdir(dir3_path)

bg_cols =960
bg_rows = 720

def random_get_img(dirpath,img_num):
    all = os.listdir(dirpath)
    imgname_c = np.random.choice(all,img_num)
    return imgname_c
def random_fg_process(img):
    sizerows = np.random.randint(100,200)
    sizecols = np.random.randint(100,200)
    img_resize = cv2.resize(img,dsize=(sizecols,sizerows))

    return img_resize,sizecols,sizerows


save_inv = 0
for i in all_img1:
    save_inv += 1
    rer = 0
    rec = 0
    src = cv2.imread(dir1_path+'/'+ i)
    img_back = cv2.resize(src, dsize=(bg_cols,bg_rows))

    fg_num = np.random.randint(1,3)
    img_c = random_get_img(dir3_path,fg_num)
    local = []
    for fg in range(fg_num):
        print(fg)
        IOU = True
        img_fg = cv2.imread(dir3_path+'/'+img_c[fg])
        img_re , c , r = random_fg_process(img_fg)
        while(IOU):
            rer = np.random.randint(0,bg_rows-r)
            rec = np.random.randint(0,bg_cols-c)
            a=rec+c
            b=rer+r
            split = img_c[fg].split('_')
            x = (rec+a)/(2*bg_cols)
            y = (rer+b)/(2*bg_rows)
            w = c/bg_cols
            h = r/bg_rows
            if local:
                for IOU_i in range(fg):
                    if (abs(x-local[IOU_i][1])<((w+local[IOU_i][3])/2.0)) and (abs(y-local[IOU_i][2])<((h+local[IOU_i][4])/2.0)):
                        IOU = True
                        break

                    IOU = False
            else:
                IOU = False

        temp = [int(split[0]),x,y,w,h]
        print(temp)

        local.append(temp)

        img_back[rer:b,rec:a] = img_re

###save file
    print(local)
    out_file = open(dir_save + '/' + 'img' + str('%05d'%save_inv) + '.txt', 'w')
    for line in local:
        cls_id = line[0]
        bb = line[1:5]
        out_file.write(str(cls_id) + " " + " ".join([str('%.6f' % a) for a in bb]) + '\n')
    out_file.close()
    #cv2.imshow('img_back', img_back)
    cv2.imwrite(dir_save+'/'+'img'+str('%05d'%save_inv)+'.jpg',img_back)
    print('img%d'%save_inv,'process successed')

    #cv2.waitKey(0)





