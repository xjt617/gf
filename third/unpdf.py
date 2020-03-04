# -*- coding: utf-8 -*-
#from unrar 
import PyPDF4
import optparse
from threading import Thread
def extractFile(pdfReader,password):
    if pdfReader.decrypt(password):
        print('[+] Found password ' + password +'\n')

def main():
    pdfReader = PyPDF4.PdfFileReader(open('/home/xjt/gfsy/third/first.pdf','rb'))
    passFile=open('/home/xjt/gfsy/third/password2.txt')
    #extractFile(rFile,'7j9STupy')
    for line in passFile.readlines():
        password=line.strip('\n')
        passwords=password.split( )
        #print(passwords)
        for i in range(4):
            #print(passwords)	
            #print(passwords[i])	
            extractFile(pdfReader,passwords[i])


if __name__ == '__main__':
    main()
