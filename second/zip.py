#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import os
import zipfile

def get_zip_file(input_path, result):
    files = os.listdir(input_path)
    for file in files:
        if os.path.isdir(input_path + '/' + file):
            get_zip_file(input_path + '/' + file, result)
        else:            
            result.append(input_path + '/' + file)

 

 

def zip_file_path(input_path, output_path, output_name):
    """
    input_path: 压缩的文件夹路径
    output_path: 解压（输出）的路径
    output_name: 压缩包名称
    """
    f = zipfile.ZipFile(output_path + '/' + output_name, 'w', zipfile.ZIP_DEFLATED)
    filelists = []
    get_zip_file(input_path, filelists)
    for file in filelists:
        f.write(file)
    # 调用了close方法才会保证完成压缩
    f.close()
    return output_path + r"/" + output_name

if __name__ == '__main__':

    zip_file_path(r"/home/xjt/gfsy/32", '/home/xjt/gfsy', '32.zip')

