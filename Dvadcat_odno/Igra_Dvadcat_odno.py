#!/usr/bin/env python
# coding: utf-8

# In[9]:


from random import randint
import random
m = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]
random.shuffle(m)
print("игра двадцать одно очко")
n = 6
ig = 0
chet = [0, 0]
chet[0] += m[randint(0, 10)] + m[randint(0, 9)]
chet[1] += m[randint(0, 8)] + m[randint(0, 7)]
print()
igr1 = True
igr2 = True
while ig < 2:
    
    print()
    if igr1:
        print(f'счет игрока {1} = {chet[0]}')
        if int(input("игрок 1 желаете зафиксировать сумму 1 - да, 2 - нет")) == 1:
            igr1 = False
            ig += 1
    
    print
    if igr2:
        print(f'счет игрока {2} = {chet[1]}')

        if int(input("игрок 2 желаете зафиксировать сумму 1 - да, 2 - нет")) == 1:
            igr2 = False
            ig += 1

    print()
    if not igr2 and not igr1:
        break


    ran = randint(0, n)
    print(f'выпало {m[ran]}')
    if  igr1:
        chet[0] += m[ran]
    if  igr2:
        chet[1] += m[ran]
    del m[ran]
    n -= 1;
    if chet[0] > 21:
        break
    if chet[1] > 21:
        break

if chet[0] > 21:
    print("перебор у игрока 1")
    if chet[1] > 21:
        print("перебор у игрока 2")
        print("ничья")
elif chet[1] > 21:
    print("перебор у игрока 2")
elif chet[0] > chet[1]:
    print("победил игрок 1")
elif chet[0] < chet[1]:
    print("победил игрок 2")
else :
    print("ничья")


# In[ ]:




