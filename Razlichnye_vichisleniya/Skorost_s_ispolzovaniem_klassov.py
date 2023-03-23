#!/usr/bin/env python
# coding: utf-8

# In[13]:


class Speed11(object):
    def __init__(self, val, unit):
        self.val = val
        self.unit = unit
        self.val1 = float(0)
        self.unit1 = ""

    def __str__(self):
        if self.unit == "м/с":
            return f'''Скорость в {self.unit} равна {self.val}
Скорость в км/ч равна {self.val * 3.6}'''
        elif self.unit == "км/ч":
            return f'''Скорость в {self.unit} равна {self.val}
Скорость в м/с равна {self.val  * 1000 / 3600}'''
        else :
            return("ошибка, неверный ввод данных")
            
valun = input("введите скорость, а затем единицу измерения через пробел").split()
try :
    val = float(valun[0])
    unit = valun[1]
except :
    ("неверно введены данные")
print(Speed11(val, unit))


# In[ ]:




