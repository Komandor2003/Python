#!/usr/bin/env python
# coding: utf-8

# Алгоритм FCFS. Построить таблицу выполнения процессов. Выполнить расчет среднего времени ожидания и полного времени выполнения при исполнении: 
# 
# p0, p1, p2, p3, p4, p5;
# p5, p4, p3, p2, p1, p0;
# 
# предложить оптимальный порядок исполнения.
# 
# 
# Р0	Р1	Р2	P3	P4	P5
# 3	9	3	5	3	1
# 

# Алгоритм FCFS. Построить таблицу выполнения процессов. Выполнить расчет среднего времени ожидания и полного времени выполнения при исполнении: 
# 
# p0, p1, p2, p3, p4, p5;
# p5, p4, p3, p2, p1, p0;
# 
# предложить оптимальный порядок исполнения.
# p0	p1	p2	P3	P4	P5
# 7	1	4	9	4	5
# 

# In[74]:


z1_1 = [0,1,2,3,4,5]
z1_2 = [5,4,3,2,1,0]
z1_vi= [3,9,3,5,3,1]

z2_1 = [0,1,2,3,4,5]
z2_2 = [5,4,3,2,1,0]
z2_vi= [7,1,4,9,4,5]

z3=[0,1,2]
z3_vi=[13,4,1]


# In[ ]:





# In[2]:


z = [0,1,2,3,4,5]


from tabulate import tabulate as table
import math


def v_proc(a, b):
    r = sum(a)
    otv = [[f'p{j}' for i in range(r + 1)] for j in range(-1, len(z))]
    f1 = 0
    for i in range (r + 1):
        otv[0][i] = i
    otv[0][0] = "Время"
    for i in range(1, len(b)+1):
        tmp = b[i-1] + 1
        for j in range(1, r+1):
            if j <= f1 :
                otv[tmp][j] = ("Г")
            elif a[tmp - 1] > 0:
                otv[tmp][j] = ("И")
                a[tmp - 1] -= 1 
                f1 += 1
            else:
                otv [tmp][j] = ("")
    return(otv)

def sr_vr_oj(c,d):
    otv2 = 0
    tmp = 0
    for i in range(len(d) - 1):
        tmp += c[d[i]]
        otv2 += tmp
    otv2 = (otv2)/len(d)
    otv2 = math.ceil(otv2)
    return f'Среднее время ожидания : {otv2}'

def sr_p_vr_v(q,w):
    tmp = 0
    otv1 = 0
    for i in range(len(w)):
        tmp +=  q[w[i]]
        otv1 += tmp
    otv1 = otv1/len(w)
    otv1 = math.ceil(otv1)
    return f'Среднее полное время выполнения : {otv1}'



def my_sort(vi,z):
    for i in range(len(z) - 1):
        for j in range(len(z)-i-1):
            if z[j] > z[j+1]:
                z[j], z[j+1] = z[j+1], z[j]
    for i in range(len(vi) - 1):
        for j in range(len(vi)-i-1):
            if vi[j] > vi[j+1]:
                z[j], z[j+1] = z[j+1], z[j]
                vi[j], vi[j+1] = vi[j+1], vi[j]
    return(vi, z)

print("Неоптимизированный процесс выполнения : ")
vi = [7,1,4,9,4,5]
print(table(v_proc(vi, z)))
vi = [7,1,4,9,4,5]
print(sr_vr_oj(vi,z))
print(sr_p_vr_v(vi,z))

print()
    
vi = [7,1,4,9,4,5]

my_sort(vi, z)
print("Оптимизированный процесс выполнения : ")
vi = [7,1,4,9,4,5]
print(table(v_proc(vi, z)))
vi = [7,1,4,9,4,5]
print(sr_vr_oj(vi,z))
print(sr_p_vr_v(vi,z))


# In[ ]:




