#!/usr/bin/env python
# coding: utf-8

# In[1]:


import requests
import os
import time
from bs4 import BeautifulSoup
from tkinter import *

def clicked():
    try:
        m = 'погода-'
        n = txt.get()
        n = n.lower()
        m = m+n
        SITE = 'https://sinoptik.ua/'
        SITE = SITE + m

        os.system("cls")

        headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/97.0.4692.99 Safari/537.36 Edg/97.0.1072.69'}
        full_page = requests.get(SITE, headers=headers)
        soup = BeautifulSoup(full_page.content, 'html.parser')

        a = ''
        a = a + n + ' '

        date = soup.findAll("div", {'class':'main loaded'})

        for i in (date[0].text):
            a = a + i
        a = a.split()
        g = 0
        d = 0
        for i in range(len(a)):
            if a[i]=='мин.':
                g = i
            elif a[i]=='макс.':
                d = i
        for i in range(len(a)):
            if i>0 and i<2:
                lbl2.configure(text=a[1])
            elif i>=2 and i==3:
                lbl3.configure(text=a[2]+' '+a[3])
            elif i>=4 and i<=(g-2):
                lbl4.configure(text=a[4]+' '+a[5])
            elif i>g and i<d:
                lbl5.configure(text=a[i])
            elif i>d:
                lbl6.configure(text=a[i])
    except LookupError:
        m = 'погода-'
        n = txt.get()
        n = n.lower()
        m = m+n
        SITE = 'https://sinoptik.ua/'
        SITE = SITE + m

        os.system("cls")

        headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/97.0.4692.99 Safari/537.36 Edg/97.0.1072.69'}
        full_page = requests.get(SITE, headers=headers)
        soup = BeautifulSoup(full_page.content, 'html.parser')

        a = ''
        a = a + n + ' '

        date = soup.findAll("div", {'class':'main loaded'})

        for i in (date[0].text):
            a = a + i
        a = a.split()
        g = 0
        d = 0
        for i in range(len(a)):
            if a[i]=='мин.':
                g = i
            elif a[i]=='макс.':
                d = i
        for i in range(len(a)):
            if i>0 and i<2:
                lbl2.configure(text=a[1])
            elif i>=2 and i==3:
                lbl3.configure(text=a[2]+' '+a[3])
            elif i>=4 and i<=(g-2):
                lbl4.configure(text=a[4]+' '+a[5])
            elif i>g and i<d:
                lbl5.configure(text=a[i])
            elif i>d:
                lbl6.configure(text=a[i])

window = Tk()
window.title("GUI на Python")
window.geometry("330x230")
selected = StringVar()
lbl = Label(window, text="Город: ")
lbl.grid(column=0, row=0)
txt = Entry(window,width=10)
txt.grid(column=1, row=0)
btn = Button(window, text="Загрузить", command=clicked)
btn.grid(column=2, row=0)
lbl = Label(window, text="День недели: ")
lbl.grid(column=0, row=1)
lbl = Label(window, text="Дата: ")
lbl.grid(column=0, row=2)
lbl = Label(window, text="Описание: ")
lbl.grid(column=0, row=3)
lbl = Label(window, text="Температура мин.: ")
lbl.grid(column=0, row=4)
lbl = Label(window, text="Температура макс.: ")
lbl.grid(column=0, row=5)
lbl2 = Label(window, text="Данные")
lbl2.grid(column=1, row=1)
lbl3 = Label(window, text="Данные")
lbl3.grid(column=1, row=2)
lbl4 = Label(window, text="Данные")
lbl4.grid(column=1, row=3)
lbl5 = Label(window, text="Данные")
lbl5.grid(column=1, row=4)
lbl6 = Label(window, text="Данные")
lbl6.grid(column=1, row=5)
window.mainloop()


# In[ ]:




