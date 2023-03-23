#!/usr/bin/env python
# coding: utf-8

# # Коммивояжёр

# ![dorogi.jpg](attachment:dorogi.jpg)

# In[6]:


import time
from tabulate import tabulate
import networkx as nx
import itertools
import matplotlib.pyplot as plt

def add_edge (f_item, s_item, graph=None):
        graph.add_edge(f_item, s_item)
        graph.add_edge(s_item, f_item)
        
        
        
def o_resh(puti, graph, alf):

    gor = graph.nodes
    min_len = 9999999999
    for i in itertools.permutations(gor):
        len_ = 0
        flag = True
        l = list(i)
        l.append(l[0])
        for j in range(len(l)-1):
            m1 = int(alf.index(l[j]))
            m2 = int(alf.index(l[j+1]))
            if str(puti[m1][m2]) != "*":
                len_+= int(puti[m1][m2])
            else :
                flag = False
                break
        if flag == False:
            continue
        if len_ < min_len:
            min_len = len_
            put_ = i
    return(min_len, put_)

alf = 'ABCDEFGHIJKLMNOP*'
kol = int(input("введите кол-во путей вершин : "))

putiv = [[alf[j-1] if i == 0 else ((alf[i-1]) if j == 0 else ("*" if j == i else " ")) for j in range(kol + 1)] for i in range(kol + 1)]
print(tabulate(putiv))
puti = [["" for j in range(kol)] for i in range(kol)]

graph = nx.Graph()
    
for i in range (kol):
    
    for j in range (i, kol):
        
        if i == j:
            
            puti[i][j] = "*"
            
            continue
            
        puti[i][j] = input(f"введите длинну дороги между {alf[i]} и {alf[j]} если дороги нет введите '*' : ")
        puti[j][i] = puti[i][j]
        putiv[i+1][j+1], putiv[j+1][i+1] = puti[i][j], puti[j][i]
        
        print(tabulate(putiv))
        
        if puti[i][j] != "*":
            
            graph.add_edge(alf[i], alf[j], distance = puti[i][j])
            
start = time.time()    

n = o_resh(puti, graph, alf)

for i in range(len(n)):
    
    if i == 0:
        
        print(f'длина кратчайщего пути = {n[i]}')
    
    else:
       
        print("кратчайщий путь", end = "")
        
        for j in range(len(n[i])):
            
            print(f' ==> {n[i][j]}', end = "")
            
    print(f' ==> {n[1][0]}')
    
graph1 = nx.Graph()

for i in range(len(n[1])):
    
    graph1.add_edge(n[1][i-1], n[1][i], distance = puti[alf.index(n[1][i-1])][alf.index(n[1][i])])
    
nx.draw(graph1,
        node_color='green',
        node_size=1000,
        with_labels=True)

edge_labels = nx.get_edge_attributes(graph1, 'distance')

pos = nx.spring_layout(graph1)

nx.draw_networkx_edge_labels(graph1,
                            pos,
                            edge_labels = edge_labels)
    
stop = time.time()

print(stop - start, " sec")


# 

# In[ ]:




