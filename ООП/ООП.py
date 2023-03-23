#!/usr/bin/env python
# coding: utf-8

# ## Семинар 15.07.2022

# ### 1. Создайте класс Circle и класс Rect, в каждом классе будет метод нахождения периметра perim. Создайте функцию вывода информации об экземплярах класса print_info не являющуюся методом класса. Создайте экземпляры классов и выведите информацию о каждом их них в виде словаря с помощью оператора print.

# In[13]:


from math import pi
class Circle:
    
    def __init__(self, r):
        self.r = r
        
    @property
    def perim(self):
        return f"Perimetr = {2*pi*self.r}"
    
    @property
    def info(self):
        return ({"radius" : self.r})

class Rect :
    
    def __init__(self, a, b):
        self.a = a
        self.b = b
        
    @property
    def perim(self):
        return f"Perimetr = {2*self.a*self.b}"
    
    @property
    def info(self):
        return({"a" : self.a, "b" : self.b})
    
def print_info(fig):
    return (fig.info, fig.perim)


# In[14]:


circ = Circle(2)
print(print_info(circ))
rect = Rect(2,3)
print(print_info(rect))


# ### 2. Создайте класс Money имеющий атрибуты rub и valuta для выполнения перевода рубли в укзанную валюту доллар или евро.

# In[18]:


class Money(object):
    def __init__(self, rub, valuta):
        self.rub = rub
        self.valuta = valuta
    def tranz(self):
        if self.valuta == "dol" :
            self.res = self.rub / 111
        elif self.valuta == "eur" :
            self.res = self.rub / 126
        return(self.res)
        


# In[19]:


m = Money(1000, 'dol')
print(m.tranz())
m = Money(3000, 'eur')
print(m.tranz())


# ### 3. Используя класс People с атрибутами имя и возраст, имеющего метод вывода информации со значениями атрибутов, в качестве базового, создайте класс Teacher, имеющий свойства:
#     - зарплата (salary)
#     методы:
#     - __init__ – конструктор;
#     - __str__.
# 
#      Используя класс People в качестве базового создайте класс Student с атрибутом оценки, имеющий:
#     - методы __init__ и __str__;
# 
# Создайте список, содержащий по 2 объекта каждого класса (People, Teacher,Student). Для этого списка:
# - выведите информацию о каждом человеке с помощью метода info;
# - выведите фамилии тех, кто моложе 30 лет;
# - найдите среднее значение оценкок студентов и среднюю зарплату учителей;
# - продемонстрируйте работу со свойствами должность и зарплата и методами.

# In[31]:


class People(object):
    def __init__(self,name,age):
        self.name = name
        self.age = age
    
    def __str__(self):
        return f"Имя {self.name}, Возраст {self.age}"
    
    
class Teacher(People):
    def __init__(self, name, age, salary):
        super().__init__(name, age)
        self.salary = salary
    def __str__(self):
        return f"Имя {self.name}, Возраст {self.age}, Зарплата {self.salary}$"
       

    
class Student(People):
    def __init__(self, name, age, marks):
        super().__init__(name,age)
        self.marks = marks
    def __str__(self):
        return f"Имя {self.name}, Возраст {self.age}, оценки {self.marks}"
        


# In[34]:





# In[35]:



Dasha = People("Даша", 18)
Dima = Teacher("Дима", 19, 1000)
Masha = Student("Маша", 18, [4,5,4,5,5])
l = [Dasha, Dima, Masha]
for i in l:
    print(i)


# ### 4. Для класса Teacher добавьте 
# #### • закрытый атрибут дисциплины (disciplines), в котором хранятся названия дисциплин, которые ведет преподаватель;
# #### • методы добавить_дисциплину (add_dis) и удалить_дисциплину (delete_dis), которые позволяют изменять список дисциплин.

# In[48]:


class People(object):
    def __init__(self,name,age):
        self.name = name
        self.age = age
    
    def __str__(self):
        return f"Имя {self.name}, Возраст {self.age}"
    
    
class Teacher(People):
    def __init__(self, name, age, salary, dis):
        super().__init__(name, age)
        self.salary = salary
        self.dis = dis
    def __str__(self):
        return f"Имя {self.name}, Возраст {self.age}, Зарплата {self.salary}$, Дисциплины {self.dis}"
    
    def __add_dis__(self, dis_):
        self.dis.append(dis_)
    def __del_dis__(self, dis_):
        j = self.dis.index(dis_)
        del self.dis[j]
        
       

    
class Student(People):
    def __init__(self, name, age, marks):
        super().__init__(name,age)
        self.marks = marks
    def __str__(self):
        return f"Имя {self.name}, Возраст {self.age}, оценки {self.marks}"


# In[50]:


Dasha = People("Даша", 21)
Dima = Teacher("Дима", 40, 1000, ["Математика","Информатика","Физкультура"])
Masha = Student("Маша", 18, [4,5,4,5,5])

l = [Dasha, Dima, Masha]
for i in l:
    print(i)
Dima.__del_dis__("Математика")
Dima.__add_dis__(str(input()))
for i in l:
    print(i)


# In[40]:


class Order(object):
    def __init__(self, code, price, count):
        self.code = code
        self.price = price
        self.count = count
    def __str__(self):
        return f"Код товара : {self.code}, цена за единицу : {self.price}, количество : {self.count}"
    
class Opt(Order):
    def __init__(self, count, price):
        super().__init__(self, count, price) 

    def __str__(self):
        if self.count >=500:
            return f"цена заказа сотавляет {self.price * self.count * 0.90}"
        else :
            return f"цена заказа сотавляет {self.price * self.count * 0.95}"
        
class Retail(Order):
    def __init__(self, count, price):
        super().__init__(self, count, price)  
        
    def __str__(self):
        return f"цена заказа сотавляет {self.price * self.count}"
    


# In[42]:



a = [18753782, 9618723, 1028375]
b = [20, 10, 100]
c = [2, 100, 600]
if (len(a)!=len(b)) or (len(b) != len(c)):
    print("ошибка, неверно введены данные")
else:    
    zak = len(a)
    for i in range(zak):
        print(Order(a[i], b[i], c[i]))
        if c[i] <= 20 :
            print(Retail(b[i], c[i]))
        else:
            print(Opt(b[i], c[i]))


# In[ ]:




