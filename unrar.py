# -*- coding: utf-8 -*-
import rarfile
import optparse
from threading import Thread
def extractFile(rFile,password):
    try:
        rFile.extractall(pwd=password)
        print('[+] Found password ' + password +'\n')
    except:
        pass

def main():
    rFile=rarfile.RarFile("/root/password.rar")
    passFile=open("/root/password.txt")
    '''extractFile(rFile,'7j9STupy')'''
    for line in passFile.readlines():
        password=line.strip('\n')
        passwords=password.split( )
        #print(passwords)
        for i in range(4):
            #print(passwords)	
            #print(passwords[i])	
            extractFile(rFile,passwords[i])

'''def main():
    zFile=rarfile.RarFile('/home/xjt/gfsy/zip/password.rar')
    i=('7j9STupy')

    zFile.extractall(pwd=i)'''


if __name__ == '__main__':
    main()
