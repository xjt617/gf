f = open('password_new2.txt','w')

l = []
for i in range(0,10):
    l.append(chr(i+48))

for j in range(0,10):
    for k in range(0,10):
        for n in range(0,10):
            for m in range(0,10):
                for z in range(0,10):
                    for x in range(0,10):
                        for q in range(0,10):
                            for p in range(0,10):
                                lb = [l[j],l[k],l[n],l[m],l[z],l[x],l[q],l[p]]
                                password = ''.join(lb)
                                t = 0
                                for u in range(0,8):
                                    for o in range(u+1,8):
                                        if password[u]==password[o]:
                                            t = 1
                                if t==0:
                                    f.write(password + '\n')

f.close()

