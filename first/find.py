f = open('password2.txt','r')
data = f.read()

data_list = list(data)

while ' ' in data_list:
    data_list.remove(' ')
while '\n' in data_list:
    data_list.remove('\n')
    
password_list = ''.join(data_list)
ls= []
print('please input:')
a = input()
a = int(a)
while a>1024 or a<1:
    print('ERROR,please input')
    a = input()
    a = int(a)
    
b = int((a-1)*8)
for i in range(0,8):
    ls.append(password_list[b+i])

password = ''.join(ls)
print(password)


f.close()
