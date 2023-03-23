#!/usr/bin/env python
# coding: utf-8

# In[25]:


from tabulate import tabulate as tab
flag = False
while flag == False:
    try :
        k = int(input("введите кол-во процессов : "))
    except :
        print("ошибка введите еще раз")
        continue
    flag = True
pr = [["процесс", "время появления в очереди", "продолжительность процесса", "приоритет процесса" ]]
o_time = 0
time = 1
proc = 2
prior = 3
i = 0
tmp = []
while i < k:
    tmp.clear()
    tmp.append(list(str(i)) + input(f"введите время появления, продолжительность и приоритет процесса Р{i} : ").split())
    if   len(tmp[0]) <= 3 or len(tmp[0]) >= 5:
        print("вы неверно ввели данные, введите заново!")
        continue
    else:
        pr.append(tmp[0][0] + tmp[0][1] + tmp[0][2] + tmp[0][3])
        o_time += int(tmp[0][proc])
        i += 1
print(tab(pr))
print(f"общее количество времени требующееся на выполнение всех процессов : {o_time}")
for i in range(k-1):
    for j in range(1, k-i):
        if int(pr[j][prior]) > int(pr[j+1][prior]):
            pr[j], pr[j+1] = pr[j+1], pr[j]
for i in range(k-1):
    for j in range(1, k-i):
        if int(pr[j][prior]) > int(pr[j+1][prior]):
            pr[j], pr[j+1] = pr[j+1], pr[j]          

otv = [[(j if i == 0 else ((f'P{i-1}') if j == 0 else "*")) for j in range (o_time + 1)] for i in range(k + 1)]
otv[0][0] = "время"
print(tab(otv))
i = 1
while i <= o_time:
    


# ## 
