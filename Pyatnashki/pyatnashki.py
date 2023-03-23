#!/usr/bin/env python
# coding: utf-8

# In[1]:


def game(m) :
    table=[[m[0],m[1],m[2],m[3]],[m[4],m[5],m[6],m[7]],[m[8],m[9],m[10],m[11]],[m[12],m[13],m[14],m[15]]]
    
    print (tabulate(table, tablefmt="grid"))
    print ('Введите число которое хотите передвинуть и нажмите Enter')
    b = int(input())
    i = 0
    while b != m[i] :
        i = i + 1
        
    if i == 0:
        if m[i+1] == '':
            m[i+1] = m[i]
            m[i] = ''
        elif m[i+4] == '':
            m[i+4] = m[i]
            m[i] = ''
        else:
            print('это число невозможно подвинуть, введите другое') 
            
            
    elif i == 1 or i == 2:
        if m[i+1] == '' :
            m[i+1] = m[i]
            m[i] = ''
        elif m[i+4] == '' :
            m[i+4] = m[i]
            m[i] = ''
        elif m[i-1] == '' :
            m[i-1] = m[i]
            m[i] = ''
        else:
            print('это число невозможно подвинуть, введите другое')
        
    elif i == 3:
        if m[i-1] == '' :
            m[i-1] = m[i]
            m[i] = ''
        elif m[i+4] == '' :
            m[i+4] = m[i]
            m[i] = ''
        else:
            print('это число невозможно подвинуть, введите другое')
            
    elif i == 4 or i == 8 :
        if m[i+1] == '' :
            m[i+1] = m[i]
            m[i] = ''
        elif m[i+4] == '' :
            m[i+4] = m[i]
            m[i] = ''
        elif m[i-4] == '' :
            m[i-4] = m[i]
            m[i] = ''
        else:
            print('это число невозможно подвинуть, введите другое')
            
    elif i == 5 or i == 6 or i == 9 or i == 10:
        if m[i-1] == '' :
            m[i-1] = m[i]
            m[i] = ''
        elif m[i-4] == '' :
            m[i-4] = m[i]
            m[i] = ''
        elif m[i+4] == '' :
            m[i+4] = m[i]
            m[i] = ''
        elif m[i+1] == '' :
            m[i+1] = m[i]
            m[i] = ''
        else:
            print('это число невозможно подвинуть, введите другое')
        
    elif i == 7 or i == 11:
        if m[i-1] == '' :
            m[i-1] = m[i]
            m[i] = ''
        elif m[i-4] == '' :
            m[i-4] = m[i]
            m[i] = ''
        elif m[i+4] == '' :
            m[i+4] = m[i]
            m[i] = ''
        else:
            print('это число невозможно подвинуть, введите другое')
        
    elif i == 12:
        if m[i+1] == '' :
            m[i+1] = m[i]
            m[i] = ''
        elif m[i-4] == '' :
            m[i-4] = m[i]
            m[i] = ''
        else:
            print('это число невозможно подвинуть, введите другое')
        
    elif i == 13 or i == 14:
        if m[i+1] == '' :
            m[i+1] = m[i]
            m[i] = ''
        elif m[i-4] == '' :
            m[i-4] = m[i]
            m[i] = ''
        elif m[i-1] == '' :
            m[i-1] = m[i]
            m[i] = ''
        else:
            print('это число невозможно подвинуть, введите другое')
    elif i == 15:
        if m[i-1] == '' :
            m[i-1] = m[i]
            m[i] = ''
        elif m[i-4] == '' :
            m[i-4] = m[i]
            m[i] = ''
        else:
            print('это число невозможно подвинуть, введите другое')
        
    t = 1
    for i in range(15) :
        if m[i] != i+1 or m[15] != '':
            t = 0
    if t == 0:
        return(game(m))
    else :
        table=[[m[0],m[1],m[2],m[3]],[m[4],m[5],m[6],m[7]],[m[8],m[9],m[10],m[11]],[m[12],m[13],m[14],m[15]]]
        print (tabulate(table, tablefmt="grid"))
        return('Вы победили!')


# In[ ]:





# In[2]:


from tabulate import tabulate


# In[3]:


pip install tabulate


# In[4]:


print('Добро пожаловать в игрy "Пятнашки"')


# In[5]:


print('нажмите Enter')
q = input()


# In[ ]:


import random
m = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,'']
random.shuffle(m)
print('игра будет окончена когда все числа будут расставлены в порядке возрастания и пустая клетка будет в правом нижнем углу')
print (game(m))

