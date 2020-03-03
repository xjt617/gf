#!/usr/bin/python
# -*- coding: UTF-8 -*-

import os
import shutil
import string

f = open('fileout.txt','w')
path_new = r'C:\Users\123'
l = []

def file_name(path):
    for root,dirs,files in os.walk(path):
        for file in files:
            if os.path.splitext(file)[1] == '.txt':
                file_path = os.path.join(root,file)
                f.write(file_path + '\n')
                l.append(file_path)
    return l

if __name__ == '__main__':
    file_name('D:\\')
    for file in l:
        shutil.copy(file,path_new)

f.close()
