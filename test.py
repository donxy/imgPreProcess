import numpy as np
import os

dir_read = r'H:picture\car'
dir_save1 = r'H:picture'

save_inv = 1
fi = open(dir_save1+'/'+'train_logo.txt','w')
file_name = os.listdir(dir_read)
for n in file_name:
    print(n)
    split = n.split('.')
    if split[-1] == 'jpg':
        fi.write('data/img/'+n+'\n')

fi.close()



