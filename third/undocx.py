import msoffcrypto


def extractFile(file,passwords):
    try:
        file.load_key(password=passwords)
        file.decrypt(open("/home/xjt/gfsy/third/123_third.docx", "wb"))
        print('[+] Found password '+password + '\n')
    except:
        pass








def main():
    file = msoffcrypto.OfficeFile(open("/home/xjt/gfsy/third/123.docx", "rb"))
    passFile=open('/home/xjt/gfsy/third/pa1.txt')
    for line in passFile.readlines():
        password=line.strip('\n')
        passwords=password.split( )
        #print(passwords)
        for i in range(4):	
            extractFile(file,passwords[i])


if __name__ == '__main__':
    main()

