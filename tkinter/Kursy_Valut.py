#!/usr/bin/env python
# coding: utf-8

# In[1]:


import requests
import os
import time
from bs4 import BeautifulSoup
from tkinter import *
from tkinter.ttk import Combobox


def clicked():
    n = txt.get() + '-'
    n = n.replace(' ', '')
    m = combo.get() + '-' + combo1.get()

    n = n + m

    SITE = 'https://finance.rambler.ru/calculators/converter/'
    SITE = SITE + n

    os.system("cls")

    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/97.0.4692.99 Safari/537.36 Edg/97.0.1072.69'}

    full_page = requests.get(SITE, headers=headers)

    soup = BeautifulSoup(full_page.content, 'html.parser')

    date = soup.findAll('div', {'class': 'converter-display__value'})

    lbl1.configure(text=date[1].text + ' ' + combo1.get())


window = Tk()
window.title("Курс валют")
window.geometry('400x250')
selected = StringVar()
combo = Combobox(window)
combo1 = Combobox(window)

lbl = Label(window, text="Введите сумму: ")
lbl.grid(column=0, row=0)
txt = Entry(window, width=23)
txt.grid(column=1, row=0)

lbl = Label(window, text="Перевод из: ")
lbl.grid(column=0, row=2)
combo['values'] = ('Выберите', 'RUB', 'USD', 'EUR', 'CHF')
combo.current(0)  # установите вариант по умолчанию
combo.grid(column=1, row=2)

lbl = Label(window, text="Перевод в: ")
lbl.grid(column=0, row=4)
combo1['values'] = ('Выберите', 'RUB', 'USD', 'EUR', 'CHF')
combo1.current(0)  # установите вариант по умолчанию
btn = Button(window, text="Загрузить", command=clicked)
combo1.grid(column=1, row=4)
btn.grid(column=2, row=4)

lbl = Label(window, text="Курс: ")
lbl.grid(column=0, row=6)
lbl1 = Label(window, text="Данные")
lbl1.grid(column=1, row=6)

window.mainloop()


# In[ ]:




