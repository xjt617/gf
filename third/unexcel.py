import msoffcrypto


def extractFile(file,passwords):
    try:
        file.load_key(password=passwords)
        file.decrypt(open("/home/xjt/gfsy/third/8_third.xlsx","wb"))
        print('[+] Found password '+passwords + '\n')
    except:
        pass







def main():
    file = msoffcrypto.OfficeFile(open("/home/xjt/gfsy/third/8.xlsx", "rb"))
    passFile=open('/home/xjt/gfsy/third/out_7.txt')
    for line in passFile.readlines():
        password=line.strip('\n')
        passwords=password.split( )
        #print(passwords)
        for i in range(1):	
            extractFile(file,passwords[i])


if __name__ == '__main__':
    main()

