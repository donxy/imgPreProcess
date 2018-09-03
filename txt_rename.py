import os
file_path = r'H:\\picture\\img1'
file_all_name = os.listdir(file_path)
print(file_all_name)
for f in file_all_name:
    print(f)
    fi = open(file_path + '/' + f, 'r')
    for line in fi:

        split=line.split()
        cls_id = int(split[0]) - 60

        (split)