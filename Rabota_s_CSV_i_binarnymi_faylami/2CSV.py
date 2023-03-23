#!/usr/bin/env python
# coding: utf-8

# In[55]:


import csv
def find_by_name(m):
    flag = True
    print("Надено по запросу : ")
    with open('data.csv') as f:
        reader = csv.reader(f)
        for row in reader:
            row = str(row[0]).split(';')
            if flag == True:
                FN = row.index("First Name")
                flag = False
            if row[FN] in m:
                for symb in row:
                    print(symb, end = " ")
                print()
m = input("Введите через пробел имена по которым необходимо выполнить поиск :").split()
find_by_name(m)


# In[ ]:




