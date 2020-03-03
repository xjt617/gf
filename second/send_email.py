import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.application import MIMEApplication

sender = '****@163.com'
password = '*******'
reciver = '1******@163.com'

message = MIMEText('hello,ziqiiii','plain','utf-8')       
message['From'] = sender     
message['To'] = reciver

zipFile = r'C:\Users\123.zip'
zipApart = MIMEApplication(open(zipFile, 'rb').read())
zipApart.add_header('Content-Disposition', 'attachment', filename=zipFile)

msg = MIMEMultipart()
msg.attach(zipApart)
msg.attach(message)
msg['Subject'] = 'title' 

try:
    server = smtplib.SMTP('smtp.163.com')
    server.login(sender,password)
    server.sendmail(sender, reciver, msg.as_string())
    print('success')
    server.quit()
 
except smtplib.SMTPException as e:
    print('error',e) 
