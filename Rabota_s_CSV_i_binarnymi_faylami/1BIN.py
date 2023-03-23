#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pickle
data = {
     'a': [1, 2.0, 3, 4+6j],
     'b': ("character string", b"byte string"),
     'c': {None, True, False}
    }
with open('data.pickle', 'wb') as f:
    pickle.dump(data, f)

with open('data.pickle', 'rb') as f:
    data_new = pickle.load(f)

print(data_new)
#{'c': {False, True, None}, 'a': [1, 2.0, 3, (4+6j)], 'b': ('character string', b'byte string')}


# In[2]:


import pickle
 
FILENAME = "user.txt"
 
name = "Tom"
age = 19
 
with open(FILENAME, "wb") as file:
    pickle.dump(name, file)
    pickle.dump(age, file)
 
with open(FILENAME, "rb") as file:
    name1 = pickle.load(file)
    age1 = pickle.load(file)
    print("Имя:", name1, "\tВозраст:", age1)


# In[2]:


import pickle
 
FILENAME = "users.txt"
 
users = [
    ["Tom", 28, True],
    ["Alice", 23, False],
    ["Bob", 34, False]
]
 
with open(FILENAME, "wb") as file:
    pickle.dump(users, file)
 
with open(FILENAME, "rb") as file:
    users_from_file = pickle.load(file)
    for user in users_from_file:
        print("Имя:", user[0], "\tВозраст:", user[1], "\tЖенат(замужем):", user[2])


# In[ ]:




