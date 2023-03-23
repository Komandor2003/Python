#!/usr/bin/env python
# coding: utf-8

# In[29]:


n = input().split()
numbers = {"один": 1, "два": 2, "три": 3, "четыре": 4 , "пять": 5, "шесть": 6, "семь": 7, "восемь": 8, "девять": 9 , "десять": 10, "одиннадцать": 11, "двенадцать": 12, "тринадцать": 13, "четырнадцать": 14, "пятнадцать": 15, "шестнадцать": 16, "семьнадцать": 17, "восемьнадцать": 18, "девятнадцать": 19, "двадцать": 20 ,  "тридцать": 30,  "сорок": 40, "пятьдесят": 50,  "шестьдесят": 60,  "семьдесят": 70, "восемьдесят": 80, "девяносто": 90, "сто": 100, "двести": 200, "триста": 300, "четыреста": 400, "пятьсот": 500, "шестьсот" : 600, "семьсот": 700, "восемьсот": 800, "девятьсот": 900, "тысяча": 1000}
answer = {1: "один", 2: "два", 3: "три", 4: "четыре", 5: "пять", 6: "шесть", 7: "семь", 8: "восемь", 9: "девять", 10: "десять", 11: "одиннадцать", 12: "двенадцать", 13: "тринадцать", 14: "четырнадцать", 15:"пятнадцать", 16: "шестнадцать", 17: "семнадцать", 18: "восемнадцать", 19: "девятнадцать", 20: "двадцать", 30: "тридцать", 40: "сорок", 50: "пятьдесят", 60: "шестьдесят", 70: "семьдесят", 80: "восемьдесят", 90: "девяносто", 100: "сто", 200: "двести", 300: "триста", 400: "четыреста", 500: "пятьсот", 600: "шестьсот", 700: "семьсот", 800: "восемьсот", 900: "девятьсот", 1000: "тысяча", 2000: "две тысячи", 3000: "три тысячи", 4000: "четыре тысячи", 5000: "пять тысяч", 6000: "шесть тысяч", 7000: "семь тысяч", 8000: "восемь тысяч", 9000: "девять тысяч", 10000: "десять тысяч"}
thous = {"две тысячи": 2000, "три тысячи": 3000, "четыре тысячи": 4000, "пять тысяч":5000, "шесть тысяч": 6000, "семь тысяч": 7000, "восемь тысяч": 8000, "девять тысяч": 9000, "десять тысяч": 10000}
moves = {"минус" : "-", "плюс" : "+"}

k = 0
flag = True
nnum = []
move = []
n.append("")

for i in range(len(n) - 1):

    if (n[i] + " " + n[i+1]) in thous:
        if flag == True:
            nnum.append(thous[n[i] + " " + n[i+1]])
            i += 1
            flag = False

    elif n[i] in numbers:
        if flag == True:
            nnum.append(numbers[n[i]])
            flag = False
        else:
            nnum[k] += numbers[n[i]]

    elif n[i] == 'плюс' or n[i] == 'минус' or (n[i] + ' ' + n[i+1]) == 'умножить на':
        if (n[i] + ' ' + n[i+1]) == 'умножить на':
            move.append('*')
            i += 1
        else :
            move.append(moves[n[i]])
        flag = True
        k += 1


otvet = nnum[0]

for i in range(len(move)):

    if move[i] == "+":
             otvet = otvet + nnum[i + 1]
    elif move[i] == "-":
             otvet = otvet - nnum[i + 1]
    elif move[i] == "*":
             otvet = otvet * nnum[i + 1]


for i in range(len(str(otvet)) - 1, -1, -1):
    if otvet not in answer:
        print(answer[otvet - (otvet % (10**i))], end = " ")
        otvet = otvet - ( otvet - (otvet % (10**i)))
    else :
        print(answer[otvet])
        break
    


# In[ ]:



