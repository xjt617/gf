f = open('out.txt','w')

l = []
for i in range(0,62):
    if i<26:
        l.append(chr(i+97))
    elif i<52 and i>25:
        l.append(chr(i+65-26))
    elif i>51:
        l.append(chr(i+48-52))

def f1():
    for j in range(0,62):
        lb = [l[j]]
        password = ''.join(lb)
        f.write(password)
        f.write('\n')

def f2():
    for j in range(0,62):
        for k in range(0,62):
            lb = [l[j],l[k]]
            password = ''.join(lb)
            f.write(password)
            f.write('\n')

def f3():
    for j in range(0,62):
        for k in range(0,62):
            for n in range(0,62):
                lb = [l[j],l[k],l[n]]
                password = ''.join(lb)
                f.write(password)
                f.write('\n')

def f4():
    for j in range(0,62):
        for k in range(0,62):
            for n in range(0,62):
                for m in range(0,62):
                    lb = [l[j],l[k],l[n],l[m]]
                    password = ''.join(lb)
                    f.write(password)
                    f.write('\n')

print('please input:')
a ,b = input().split(' ')
while int(a)>int(b) or int(a)>4 or int(b)>4 or int(a)==0 or int(b)==0:
    print('ERROR，please input')
    a , b = input().split(' ')
a = int(a)
b = int(b)

if a==b:
    if a==1:
        f1()
    elif a==2:
        f2()
    elif a==3:
        f3()
    else:
        f4()
else:
    if a==1 and b==2:
        f1()
        f2()
    elif a==1 and b==3:
        f1()
        f2()
        f3()
    elif a==1 and b==4:
        f1()
        f2()
        f3()
        f4()
    elif a==2 and b==3:
        f2()
        f3()
    elif a==2 and b==4:
        f2()
        f3()
        f4()
    else:
        f3()
        f4()
        
        
f.close()

