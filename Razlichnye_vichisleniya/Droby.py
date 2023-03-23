#!/usr/bin/env python
# coding: utf-8

# In[23]:


def NOK(a, b):
    if a > b:
        g = a
    else:
        g = b
    while(True):
        if (g%a == 0) and (g%b == 0) :
            nok = g
            break
        g += 1
    return(nok)

n = input().split()
m = n.copy()
flag = True

try:
    q = []
    for i in range(len(n)):
#         print(n[i])
        if "/" not in n[i]:
            continue
        elif n[i] != "+" and n[i] != "*":
            try :
                tmp10 = int(n[i-1])
                for j in range(len(n[i])):
                    if n[i][j] == "/":
                        tmp = j
#                 print(n[i-1], n[i][tmp + 1:])
                tmp1 = int(n[i-1]) * int(n[i][tmp + 1:]) + int(n[i][:tmp])
                n[i] = str(tmp1) + "/" + n[i][tmp+1:]
                q.append(i)
            except :
                continue
    z = 1
    for i in q:
        del n[i-z]
        z += 1


    if n[1] == "*":
        tmp3 = int(n[0][:n[0].index('/')]) * int(n[2][:n[2].index('/')])
        tmp4 = int(n[0][n[0].index('/') + 1:]) * int(n[2][n[2].index('/') + 1:])
        otv = str(tmp3) + '/'  + str(tmp4)
    elif n[1] == "+":
        v = NOK(int(n[0][n[0].index('/') + 1:]), int(n[2][n[2].index('/') + 1:]))
        tmp5 = v // int(n[0][n[0].index('/') + 1:])
        tmp6 = v // int(n[2][n[2].index('/') + 1:])
        tmp3 = (int(n[0][:n[0].index('/')]) * tmp5) + (int(n[2][:n[2].index('/')]) * tmp6)
        tmp4 = int(n[0][n[0].index('/') + 1:]) * tmp5
        otv = str(tmp3) + '/'  + str(tmp4)
    else :
        print("ошибка, неверный ввод данных")
        flag = False


    if  flag != False:
        for i in m:
            print(i, end = " ")
        print("=", otv)
except:
    print("ошибка, неверный ввод данных")


# In[ ]:




