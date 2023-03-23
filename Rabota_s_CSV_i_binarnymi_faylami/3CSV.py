#!/usr/bin/env python
# coding: utf-8

# In[1]:


import csv


# In[2]:


import csv
with open("classmates1.csv", encoding='1251') as r_file:
    # Создаем объект reader, указываем символ-разделитель ","
    file_reader = csv.reader(r_file, delimiter = ",")
    # Счетчик для подсчета количества строк и вывода заголовков столбцов
    count = 0
    # Считывание данных из CSV файла
    for row in file_reader:
        if count == 0:
            # Вывод строки, содержащей заголовки для столбцов
            print(f'Файл содержит столбцы: {", ".join(row)}')
        else:
            # Вывод строк
            print(f'    {row[0]} - {row[1]} и он родился в {row[2]} году.')
        count += 1
    print(f'Всего в файле {count} строк.')


# In[9]:


def izcsv(imya):
    import csv
    rez=[]
    with open(imya) as f:
        t = csv.reader(f, delimiter=';')
        for i in t:
            rez.append(i)
    return rez[0],rez[1:]
izcsv("classmates.csv")


# In[12]:


import csv
with open("classmates1.csv", encoding='1251') as r_file:
    # Создаем объект DictReader, указываем символ-разделитель ","
    file_reader = csv.DictReader(r_file, delimiter = ",")
    # Счетчик для подсчета количества строк и вывода заголовков столбцов
    count = 0
    # Считывание данных из CSV файла
    for row in file_reader:
        if count == 0:
            # Вывод строки, содержащей заголовки для столбцов
            print(f'Файл содержит столбцы: {",".join(row)}')
        # Вывод строк
        print(f' {row["Имя"]} - {row["Успеваемость"]}', end='')
        print(f' и он родился в {row["Год рождения"]} году.')
        count += 1
    print(f'Всего в файле {count + 1} строк.')


# In[ ]:


import csv
fieldnames = ['Имя', 'Класс', 'Возраст']
file_reader = csv.DictReader(r_file, fieldnames = fieldnames)


# In[13]:


import csv
with open("classmat.csv", mode="w", encoding='1251') as w_file:
    file_writer = csv.writer(w_file, delimiter = ",", lineterminator="\r")
    file_writer.writerow(["Имя", "Класс", "Возраст"])
    file_writer.writerow(["Женя", "3", "10"])
    file_writer.writerow(["Саша", "5", "12"])
    file_writer.writerow(["Маша", "11", "18"])


# In[17]:


import csv
with open("classmat.csv", mode="w", encoding='1251') as w_file:
    names = ["Имя", "Возраст"]
    file_writer = csv.DictWriter(w_file, delimiter = ",", 
                                 lineterminator="\r", fieldnames=names)
    file_writer.writeheader()
    file_writer.writerow({"Имя": "Саша", "Возраст": "6"})
    file_writer.writerow({"Имя": "Маша", "Возраст": "15"})
    file_writer.writerow({"Имя": "Вова", "Возраст": "14"})


# In[ ]:


file_writer.writerows([{"Имя": "Саша", "Возраст": "6"},
    {"Имя": "Маша", "Возраст": "15"},
    {"Имя": "Вова", "Возраст": "14"}])


# In[ ]:


Атрибут	                            Значение
    delimiter	      Устанавливает символ, с помощью которого разделяются элементы в файле. По умолчанию используется запятая.
    doublequote       Если True, то символ quotechar удваивается, если False, то к символу qutechar добавляется ecsapechar в качестве префикса.
    escapechar	      Строка из одного символа, которая используется для экранирования символа-разделителя.
    lineterminator	   Определяет разделитель для строк, по умолчанию используется “\r\n”
    quotechar	      Определяет символ, который используется для окружения символа-разделителя. По умолчанию используются двойные кавычки, то есть quotechar = ‘ ” ‘.
    quoting	            Определяет символ, который используется для экранирования символа разделителя (если не используются кавычки).
    skipinitialspace	Если установить значение этого параметра в True, то все пробелы после символа-разделителя будут игнорироваться.
    strict	             Если установить в True, то при неправильном вводе CSV будет возбуждаться исключение Error.


# In[9]:


#### Пример использования:

import csv
csv.register_dialect('my_dialect', delimiter=':', lineterminator="\r")
with open("classmat1.csv", mode="w", encoding='1251') as w_file:
    file_writer = csv.writer(w_file, 'my_dialect')
    file_writer.writerow(["Имя", "Клаcc", "Возраст"])
    file_writer.writerow(["Женя", "3", "10"])
    file_writer.writerow(["Саша", "5", "12"])
    file_writer.writerow(["Маша", "11", "18"])


# In[ ]:


#### В результате получим:

Имя:Класс:Возраст
Женя:3:10
Саша:5:12
Маша:11:18


# In[ ]:




