#!/usr/bin/env python
# coding: utf-8

# In[23]:


import csv
with open('man.csv', mode='w') as fm:
    fm = csv.writer(fm, delimiter=';', quotechar='"', quoting=csv.QUOTE_MINIMAL)
    fm.writerow(['имя', 'возраст','пол'])

with open('woman.csv', mode='w') as fw:
    fw = csv.writer(fw, delimiter=';', quotechar='"', quoting=csv.QUOTE_MINIMAL)
    fw.writerow(['имя', 'возраст','пол'])
    
def _writerm_(x):
    with open('man.csv', mode='a') as wm:
        wm = csv.writer(wm, delimiter=';', quotechar='"', quoting=csv.QUOTE_MINIMAL)
        wm.writerow(x)
    
def _writerw_(x):
    with open('woman.csv', mode='a') as ww:
        ww = csv.writer(ww, delimiter=';', quotechar='"', quoting=csv.QUOTE_MINIMAL)
        ww.writerow(x)
    
s = [('Ирина','27','ж'), ('Семен','33','м'), ('Евгений','45','м'), ('Светлана','21','ж')]
for i in s:
    if i[2] == "ж":
        _writerw_(i)
    elif i[2] == "м":
        _writerm_(i)


# In[18]:


import csv
with open('employee_fie.csv', mode='w') as employee_file:
    employee_writer = csv.writer(employee_file, delimiter=',', quotechar=',', quoting=csv.QUOTE_MINIMAL)
    employee_writer.writerow(['John Smith', 'Accounting', 'November'])
    employee_writer.writerow(['Erica Meyers', 'IT', 'March'])


# In[19]:


with open('employee_file2.csv', mode='w') as csv_file:
    fieldnames = ['emp_name', 'dept', 'birth_month']
    writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
    writer.writeheader()
    writer.writerow({'emp_name': 'John Smith', 'dept': 'Accounting', 'birth_month': 'November'})
    writer.writerow({'emp_name': 'Erica Meyers', 'dept': 'IT', 'birth_month': 'March'})


# In[ ]:




