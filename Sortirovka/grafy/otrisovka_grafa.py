#!/usr/bin/env python
# coding: utf-8

# In[6]:


import networkx as nx
import matplotlib.pyplot as plt

graph = nx.Graph()

def add_edge(f_item, s_item, graph=None):
    graph.add_edge(f_item, s_item)
    graph.add_edge(s_item, f_item) 

add_edge('A', 'B', graph=graph)
add_edge('B', 'C', graph=graph)
add_edge('B', 'D', graph=graph)
add_edge('D', 'E', graph=graph)

nx.draw_circular(graph,
         node_color='red',
         node_size=1000,
         with_labels=True)


# In[ ]:




