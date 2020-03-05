# -*- coding:utf-8 -*-


source_dir = r'C:\Users\yangyi\Desktop\网络攻防\out8.txt'
target_dir = r'C:\Users\yangyi\Desktop\网络攻防\拆分后的小字典\\'

flag = 0

name = 1

dataList = []

with open(source_dir,'r') as f_source:
    for line in f_source:
        flag+=1
        dataList.append(line)
        if flag == 2000000:
            with open(target_dir+"out_"+str(name)+".txt",'w+') as f_target:
                 for data in dataList:
                      f_target.write(data)
            name+=1
            flag = 0
            dataList = []
 
with open(target_dir+"out_"+str(name)+".txt",'w+') as f_target:
    for data in dataList:
        f_target.write(data)

