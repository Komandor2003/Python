#!/usr/bin/env python
# coding: utf-8

# In[10]:


#вытесняющий
import copy
from prettytable import PrettyTable
mytable = PrettyTable()
N = int(input('Введите количество процессов: '))
processes = []
for i in range(N):
    process = input('Введите через пробел время появления и продолжительность процесса: ').split(' ')
    process = list(map(lambda x: int(x), process))
    processes.append(process)
max_time = max(i[0] for i in processes)
mytable.add_column('Время',[f'P{i}' for i in range(N)])
work_line = []
processes = list(enumerate(processes, start=1))
processes_full = copy.deepcopy(processes)
i = 0
avr_time = 0
full_time = 0
while processes != [] or work_line != []:
    for j in processes:
        if j[1][0] == i:
            work_line.append(j)
    for j in work_line:
        if j in processes:
            processes.remove(j)
    current_min = min(q[1][1] for q in work_line if work_line != [])
    current_work = None
    for w in work_line:
        if w[1][1] == current_min:
            if current_work != None:
                if current_work[0] > w[0]:
                    current_work = copy.deepcopy(w)
                    w[1][1] -= 1
                    work_line.append(current_work)
            else:
                current_work = copy.deepcopy(w)
                w[1][1] -= 1
                work_line.append(current_work)
        if w[1][1] == 0:
            work_line.remove(w)
    print_line = [' ' for i in range(N)]
    for e in work_line:
        if e == current_work:
            print_line[e[0]-1] = 'И'
        else:
            print_line[e[0]-1] = 'Г'
    work_line.pop(-1)
    mytable.add_column(str(i + 1), print_line)
    for y in print_line:
        if y == 'Г':
            avr_time += 1
            full_time += 1
        elif y == 'И':
            full_time += 1
    i += 1
print(mytable)
print('Среднее время ожидания: %.2f' % (avr_time / N))
print('Среднее полное время выполнения: %.2f' % (full_time / N))


# # №2
# 0 - 6, 3 - 5, 6 - 7, 0 - 2
# # №3
# 4 - 6, 2 - 5, 8 - 2, 0 - 5

# In[12]:


#невытесняющий
from prettytable import PrettyTable
mytable = PrettyTable()
N = int(input('Введите количество процессов: '))
processes = []
for i in range(N):
    processes.append(int(input(f'Введите продолжительность процесса {i} : ')))
mytable.add_column('Время',[f'P{i}' for i in range(N)])
processes = list(enumerate(processes, start=1))
processes = list(map(lambda x: list(x), processes))
i = 0
avr_time = 0
full_time = 0
while processes != []:
    print_line = [' ' for i in range(N)]
    min_time = min(i[1] for i in processes)
    for e in processes:
        print_line[e[0] - 1] = 'Г'
        if e[1] == min_time and 'И' not in print_line:
            print_line[e[0] - 1] = 'И'
            e[1] -= 1
    for e in processes:
        if e[1] == 0:
            processes.remove(e)
    mytable.add_column(str(i + 1), print_line)
    for y in print_line:
        if y == 'Г':
            avr_time += 1
            full_time += 1
        elif y == 'И':
            full_time += 1
    i += 1
print(mytable)
print('Среднее время ожидания: %.2f' % (avr_time / N))
print('Среднее полное время выполнения: %.2f' % (full_time / N))


# # №1
# 5, 3, 7, 4
# # №3
# 8, 1, 4, 3
