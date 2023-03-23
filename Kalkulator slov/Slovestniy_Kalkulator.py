#!/usr/bin/env python
# coding: utf-8

# In[1]:


cif = {"ноль" : 0,"один" : 1, "два" : 2, "три" : 3, "четыре" : 4, "пять" : 5, "шесть" : 6, "семь" : 7, "восемь" : 8, "девять" : 9, "десять" : 10, "одиннадцать" : 11, "двенадцать" : 12, "тринадцать" : 13, "четырнадцать" : 14, "пятнадцать" : 15, "шестнадцать" : 16, "семнадцать" : 17, "восемнадцать" : 18, "девятнадцать" : 19, "двадцать" : 20, "тридцать" : 30, "сорок" : 40, "пятьдесят" : 50, "шестьдесят" : 60, "семьдесят" : 70, "восемьдесят" : 80, "девяносто" : 90, "сто" : 100, "двести" : 200, "тристо" : 300, "четыресто" : 400, "пятьсот" : 500, "шестьсот" : 600, "семьсот" : 700, "восемьсот" : 800, "девятьсот" : 900, "тысяча" : 1000, "две тысячи" : 2000, "три тысячи" : 3000, "четыре тысячи" : 4000, "пять тысяч" : 5000, "шесть тысяч" : 6000, "семь тысяч" : 7000, "восемь тысяч" : 8000,"девять тысяч" : 9000, "десять тысяч" : 10000}


# In[2]:


def calc() :   
    if c == 0 :
        t = []
        f = ""
        h = 1
        q = 0
        v = 0
        h1 = 1
        for i in range(l + 1):
            t.append(0)
        i = 0
        while i < l:
            if n[i] == "минус" or n[i] == "плюс" or n[i] == "умножить" or n[i] == 'разделить' :
                if q == 0:
                    h1 = - 1
                    v = 1
                if (f == "минус" or f == "плюс" or f == "умножить" or f == "разделить") and n[i] == "минус":
                    h = -1
                tmp = i
                t[i] = 0
                if h == 1:
                    f = n[i]  
                if n[i] == 'умножить' or n[i] == 'разделить':
                    i = i + 1
                i = i + 1 

            elif l <= 3 :
                q = 1
                t[i] = float(cif.get(n[i]))
                i = i + 1
            elif l > 3 :
                q = 1
                tmp1 = i
                j = 0
                while j != 1:
                    t[tmp1] = t[tmp1] + int(cif.get(n[i]))
                    i = i + 1
                    if i >= l :
                        j = 1
                    elif n[i] =='минус'  or n[i] =='плюс' or n[i] == "умножить" or n[i] == 'разделить':
                        j = 1



        if f == "минус":
            if  int(t[0 + v]) * h1 - int(t[tmp+1]) * h < 0:
                print("ответ : минус ", end = "")
            otv = int(t[0 + v]) * h1 - int(t[tmp+1]) * h
        elif f == "плюс":
            if  int(t[0 + v]) * h1 + int(t[tmp+1]) * h < 0:
                print("ответ : минус ", end = "")
            otv = int(t[0 + v]) * h1 + int(t[tmp+1]) * h
        elif f == "умножить":
            if h == - 1:
                tmp = tmp - 1
            if  int(t[0 + v])* h1 * int(t[tmp+2]) * h < 0:
                print("ответ : минус ", end = "")
            otv = int(t[0 + v])* h1 * int(t[tmp+2]) * h
        elif f == "разделить":
            if h == - 1:
                tmp = tmp - 1
            if int(t[0 + v])* h1 // int(t[tmp+2]) * h < 0:
                print("ответ : минус ", end = "")
            otv = int(t[0 + v])* h1 // int(t[tmp+2]) * h
        if otv < 0 :
            otv = otv * -1
        else :
            print("ответ : ", end = "")
        i = 10
        ost = 1
        cel = 1
        otv1 = ""
        if (otv > 10 and otv < 20) :
            otv1 = (list(cif.keys())[list(cif.values()).index(otv)] )
        else:
            while cel != 0:
                if (int((otv % i) // (i / 10) * (i / 10))) != 0 :
                    cel = int(otv // i)
                    ost = int((otv % i) // (i / 10) * (i / 10))
                    otv1 = (list(cif.keys())[list(cif.values()).index(ost)] ) + " " + otv1  
                i = i * 10    
        
    
        return(otv1)
    
    elif c == 2 :
        q = False
        t1 = 0
        t2 = 0
        for i in range(l):
            if n[i] == "в" :
                q = True
            elif n[i] != "в" and n[i] != "степени" :
                if q == False:
                    t1 = t1 + int(cif.get(n[i]))

                else :
                    t2 = t2 + int(cif.get(n[i]))

        otv = t1**t2

        print("ответ : ", end = "")



        i = 10
        ost = 1
        cel = 1
        otv1 = ""
        if (otv > 10 and otv < 20) :
            otv1 = (list(cif.keys())[list(cif.values()).index(otv)] )
        else:
            while cel != 0:
                if (int((otv % i) // (i / 10) * (i / 10))) != 0 :
                    cel = int(otv // i)
                    ost = int((otv % i) // (i / 10) * (i / 10))
                    otv1 = (list(cif.keys())[list(cif.values()).index(ost)] ) + " " + otv1  
                i = i * 10

        return(otv1)
    
    elif c == 1:
        t1 = 0
        t2 = 0
        f1 = 1
        f2 = 1
        f3 = 1
        q = False
        otv = 0
        if n[0] == "перестановок":
            for i in range(l):
                if n[i] != "перестановок" and n[i] != "из" :
                    t1 = t1 + int(cif.get(n[i]))
            for i in range(1, t1 + 1):
                f1 = f1 * i
        else :
            for i in range(l):
                if n [i] == "по":
                    q = True
                elif n[i] != "из" and n[i] != "по" and n[i] != "сочетаний" and n[i] != "размещений" :
                    if q == False:
                        t1 = t1 + int(cif.get(n[i]))
                    else :
                        t2 = t2 + int(cif.get(n[i]))
            for i in range(1, t1 + 1):
                f2 = f2 * i
            for i in range(1, t2 + 1):
                f1 = f1 * i
            for i in range(1, (t2 - t1) + 1):
                f3 = f3 * i

        if n[0] == "размещений" :
            otv = f2 // f3
        elif n[0] == "сочетаний" :
            otv = f2 // (f3 * f1)
        elif n[0] == "перестановок" :
            otv = f1
        i = 10
        ost = 1
        cel = 1
        otv1 = ""
        if (otv > 10 and otv < 20) :
            otv1 = (list(cif.keys())[list(cif.values()).index(otv)] )
        else:
            while cel != 0:
                if (int((otv % i) // (i / 10) * (i / 10))) != 0 :
                    cel = int(otv // i)
                    ost = int((otv % i) // (i / 10) * (i / 10))
                    otv1 = (list(cif.keys())[list(cif.values()).index(ost)] ) + " " + otv1  
                i = i * 10
        return(otv1)


# In[3]:


print("!!! ВАЖНО !!!")
print("калькулятор поддерживает только целочисленное деление, при не целом делении округление будет происходить в большую сторону")
print("на ввод калькулятор поддерживает числа не выше 1999 и не больше 10999 на вывод, а так же все числа должы стоять в именительном падеже")
n = input().split()
l = len(n)
c = 0
for i in n:
    if i == "размещений" or i == "сочетаний" or i == "перестановок":
        c = 1
    if i == "степени" :
        c = 2
print(calc())


# In[ ]:




