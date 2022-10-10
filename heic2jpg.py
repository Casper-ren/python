# -*- coding: utf-8 -*-
"""
Created on Mon Oct 10 13:37:19 2022

@author: cyr
"""
import os
from PIL import Image
from pillow_heif import register_heif_opener
register_heif_opener()
# original_dir = r'./heic/'
# target_dir = f'{original_dir}-JPG'
# if not os.path.exists(target_dir):
#     os.makedirs(target_dir)
# image = Image.open('./IMG_6853.HEIC.heic')
# image.save("IMG_6853.HEIC.jpg", format="jpeg")

import glob
 
#获取指定目录下的所有图片

# for root, dirs, files in os.walk(original_dir):   
#     print(root,dirs,files)
#     for file in files:
#         print(file)
#         file_name = file.split('.')[0]
#         original_img_path = f'{original_dir}/{file}'
#         image = Image.open(original_img_path)
#         image.save(f"{target_dir}/{file_name}.jpg", format="jpeg")



import os
 
def GetFiles(file_dir,file_type,IsCurrent=False):
    '''
        功能：获取指定文件路径&文件类型下的所有文件名
        传入：
            file_dir   文件路径,
            file_type  文件类型,
            IsCurrent  是否只获取当前文件路径下的文件，默认False
        返回：含文件名的列表
    '''
    file_list = []
    for parent, dirnames, filenames in os.walk(file_dir):
        for filename in filenames:
            if filename.endswith(('.%s'%file_type)):  # 判断文件类型
                file_list.append(os.path.join(parent, filename))
                
        if IsCurrent == True:
            break
    return file_list
 
dir_ = r"C:\Users\cyr\Desktop\he" #获取当前路径
files = GetFiles(dir_,"heic")
for file in files:
    print(file)
    file_name = file.split('.')[0]
    original_img_path = f'{file}'
    image = Image.open(original_img_path)
    image.save(f"{file_name}.jpg", format="jpeg")
# print(glob.glob(r"C:\Users\cyr\Desktop\新建文件夹\*.heic"))
# for filename in glob.glob(r"C:\Users\cyr\Desktop\新建文件夹\*.heic"):
#     image = Image.open(filename)
#     newname=filename+'.jpg'
#     image.save(filename, format="jpeg")
