#!/usr/bin/env python
# coding: utf-8

# In[1]:


from timeit import default_timer as timer
import time
indent = 0
res = []
def printing(function):
    import functools
    @functools.wraps(function)
    def wraper(*args, **kwargs):
        global indent
        start = timer()
        start3 = time.perf_counter()
        indent += 1
        print("    " * indent + f'{function.__name__}{args}')
        res.append(sum(args))
        result = function(*args, **kwargs)
        indent -= 1
        end = timer()
        end3 = time.perf_counter()
        print("    " * indent + f'{res[indent]}, time1 = {(end - start):.9f}, time2 = {(end3 - start3):.9f}')
        return (result)
    return wraper


# In[2]:


import functools
def decor(function):
    @functools.wraps(function)
    def wrapper(*args, **kwargs):
        print(f"тут будут значения передаваемы функции {args}")
        result = function(*args, **kwargs)
        print (f"а это результат : {result}")
        print("все, конец, метеорит летит!")
        print()
        return(result)
    return wrapper


# In[7]:


@decor
def foo(a,b,c):
    return (a * b + c)


# In[8]:


foo(1,2,3)
r = True


# In[ ]:





# In[ ]:




