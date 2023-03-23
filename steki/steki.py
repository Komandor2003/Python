#!/usr/bin/env python
# coding: utf-8

# In[29]:


from collections import deque
class Stack(deque):
    def push(self, a):
        self.append(a)
    def delete(self):
        return(self.pop())
    def clean(self, a):
        for i in range(a):
            c.delete()
    def rever(self, m, a, q):
        for i in range(a):
            q.push(m.delete())
        return(q)
    
from random import randint as ran
c = Stack()
for i in range(20) :
    c.push(ran(20, 30))
print(c)
flag = c.delete()
k = len(c)
m = Stack()
for i in range(k):
    tmp = c.delete()
    if tmp == flag:
        continue
    else:
        m.push(tmp)
c.clean(len(c))
c.rever(m, len(m), c)
# c.push(flag) ???
print(c)


# In[ ]:




