# coding:utf8
from ftplib import FTP


def upload(f, remote_path, local_path):
    fp = open(local_path, "rb")
    buf_size = 1024
    f.storbinary("STOR {}".format(remote_path), fp, buf_size)
    fp.close()


def download(f, remote_path, local_path):
    fp = open(local_path, "wb")
    buf_size = 1024
    f.retrbinary('RETR {}'.format(remote_path), fp.write, buf_size)
    fp.close()


if __name__ == "__main__":
    ftp = FTP()
    ftp.connect("192.168.5.133", 21)      # 第一个参数可以是ftp服务器的ip或者域名，第二个参数为ftp服务器的连接端口，默认为21
    ftp.login(xjt, 123456789)     # 匿名登录直接使用ftp.login()
    ftp.cwd("F:/second")                # 切换到f:/second
    upload(ftp, "ftp_word.zip", "word.zip")   # 将当前目录下的word.zip文件上传到ftp服务器的f:f:/second目录，命名为ftp_word.zip
    upload(ftp, "ftp_txt.zip", "txt.zp")  
    ftp.quit()