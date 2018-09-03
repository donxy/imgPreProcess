import os
file_path = 'G:\数据集\caiji'
file_all_nmae = os.listdir(file_path)
print(file_all_nmae)
i = 1

for n1 in file_all_nmae:
    print(n1)
    j = '%05d'%i
    print(i)
    new_name = 'bzdybox_'+str(j) + '.jpg'
    os.rename(file_path + '/' +n1,file_path + '/' + new_name)
    print('img%d'%i,'rename successed')
    i += 1