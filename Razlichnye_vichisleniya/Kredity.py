#!/usr/bin/env python
# coding: utf-8

# задание 3.1

# In[1]:


import math

def p(t):
    x = (math.pi/2) - math.atan((2000-t)/45)
    N = 172/45 * x
    return N


s = input().split()
for i in s:
    p1 = p(int(i))
    print(f"{int(i):5d} - {p1:6.3f} миллиард(ов)")


# задание 3.2

# In[2]:


def p(t, s, n, k):
    p = s / n + (s - (t - 1) * s / n) * k / (12 * 100)
    return p


s = int(input())  # сумма
n = int(input())  # срок
k = int(input())  # процент
s1 = s
a1 = 0

for t in range(1, n + 1):
    m = p(t, s, n, k)
    print(f"{t:2d} месяц - {m:8.2f}руб")
    a1 += m
print(f"Доход банка - {(a1 - s):6.2f}руб")


# задание 3.3

# In[3]:


def t(a, b):
    return (a + b) / 2


t1 = input().split()
t2 = input().split()
s = float(input())

for i in range(len(t1)):
    s1 = t(float(t1[i]), float(t2[i]))
    if s1 > s:
        print(i)


# задание 3.4

# In[4]:


fx = input().split()
fy = input().split()
rc = int(input())
r = int(input())
rcx, rcy = fx[rc], fy[rc]
c = 0
d = []
for i in range(len(fx)):
    c1 = ((int(fx[i]) - int(rcx)) ** 2 + (int(fy[i]) - int(rcy)) ** 2) ** 0.5
    d.append(c1)

for i in d:
    if i < r:
        c += 1
print(c)


# задание 3.5

# In[7]:


# months = '150 132 110 186 103 229 179 224 230 113 224 202'.split()
# n = 148
# a, b = 3.67, 4.83

months = input().split()
n = int(input())
a = float(input())
b = float(input())

summa_kv = 0
cost = 0

for i in months:
    cost_now = int(i)
    if cost_now > n:
        cost += n * a + (cost_now-n) * b
    else:
        cost += cost_now * a
    summa_kv += cost_now

print(f"Сумма:{summa_kv:6d} кВт ч, стоимость {cost:7.2f} руб")


# задание 3.6

# In[8]:


def diff(t, s, n, k):
    p = s / n + (s - (t - 1) * s / n) * k / (12 * 100)
    return p


def annuit(s, n, k):
    ka = k / (12 * 100)
    return ((ka * (1 + ka) ** n) / ((1 + ka) ** n - 1)) * s

s = int(input())  # сумма кредита
n = int(input())  # срок месяцы
k = int(input())  # процент
all_month = 0
month_ann = annuit(s, n, k)

for t in range(1, n + 1):
    month = diff(t, s, n, k)
    print(f"{t:2d} месяц - (диф.) {month:8.2f} руб - (анн.) {month_ann:8.2f} руб")
    all_month += month
print(f"Доход банка - (диф.) {(all_month - s):6.2f}руб - (анн.) {(month_ann * n - s):6.2f} руб")


# In[ ]:




