#!/usr/bin/env python
# coding: utf-8

# 1. Дан массив размерности 20 из элементов от 1 до 100. Разбить его по индексу к и отсортировать левую часть по убыванию, правую часть по возрастанию.

# In[1]:


import array
def sort1(ar):
    a = ar
    for i in range(len(a)):
        idxMin = i
        for j in range(i+1, len(a)):
            if a[j] < a[idxMin]:
                idxMin = j
        tmp = a[idxMin]
        a[idxMin] = a[i]
        a[i] = tmp
    return a

def sort2(ar):
    a = ar
    for i in range(len(a)):
        idxMax = i
        for j in range(i+1, len(a)):
            if a[j] > a[idxMax]:
                idxMax = j
        tmp = a[idxMax]
        a[idxMax] = a[i]
        a[i] = tmp
    return a

def main_sort(ar):
    n=len(ar)//2
    return sort2(ar[:n])+ sort1(ar[n:])



ar = array.array('i', [4,5,3,7,87,12,32,43,67,0,22,56,43,14,15,90,45,53,99,30])

print(main_sort(ar))


# 2. В одномерном массиве из 20 элементов со значениями от -20 до 30 выполнить сортировку четных элементов по возрастанию, нечетных элементов по убыванию. 

# In[2]:


ar1 = array.array('i', [4,5,3,7,-7,12,-3,-4,-2,0,22,-15,-10,14,15,-11,-20,-18,28,30])
def main_sort1(ar):
    res=[]
    a = sort1([ar[x] for x in range(0,len(ar),2)])
    b = sort2([ar[x] for x in range(1,len(ar),2)])
    for i in range(len(a)):
        res.append(a[i])
        res.append(b[i])
    return res
print(main_sort1(ar1))


# 3. Дан двумерный массив размерности n, содержащий значения от -5 до 15. Столбцы с четными индексами отсортировать по возрастанию, если на главной диагонали стоит число меньше 0, и по убыванию, если на глвной диагонали стоит число больше 0.

# In[4]:


import numpy as np
import random
n=int(input('n = '))
ar2 = np.random.randint(-3, 15, size=(n,n))
temp = ar2.transpose()
print(ar2)
ar3=[]
for i in range(0,n,2):
    if ar2[i][i]<0:
        temp[i]=sort1(temp[i])
    else:
        temp[i]=sort2(temp[i])
temp2 = temp.transpose()
print(temp2)


# In[ ]:




