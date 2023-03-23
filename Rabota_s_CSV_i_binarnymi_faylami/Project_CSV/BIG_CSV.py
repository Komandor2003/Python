#!/usr/bin/env python
# coding: utf-8

# In[ ]:


from tabulate import tabulate #Вывод красивой таблицы
import pickle
import csv


def correct( object ):
    if object:
        titles = []
        for line in object:
            for key in line.keys():
                if key not in titles:
                    titles.append( key )

        for index in range( len(object) ):
            for title in titles:
                if title not in object[index]:
                    object[index][title] = ''

        for index in range( len(object) ):
            for title in titles:
                object[index][title] = 'None' if object[index][title] == '' else object[index][title]
        return object
    else:
        print('Нельзя')

def load_table( nazvaniya ):
    itog = []
    for nazvanie in nazvaniya:
        try:
            if nazvanie.endswith('.csv'):
                with open( nazvanie ) as file:
                    reader = list(csv.DictReader( file, delimiter=';' ))
                    itog += reader
            elif nazvanie.endswith('.txt'):
                with open( nazvanie, 'rb' ) as file:
                    reader = pickle.load( file )
                    itog += reader
        except Exception as error:
            print(f'Видимо, файла {nazvanie} не существует')
    if itog != []:
        return correct( itog )
    else:
        return False

def save_table_csv( object, nazvanie ):
    if object:
        if not(nazvanie.endswith('.csv')):
            nazvanie = nazvanie+'.csv'
        try:
            with open(nazvanie, 'w') as file:
                zagolovki = list(object[0].keys())
                writer = csv.DictWriter( file, delimiter=';', lineterminator='\n', fieldnames=zagolovki )
                writer.writeheader()
                for stroka in object:
                    writer.writerow( stroka )
        except Exception as error:
            print(error)
    else:
        print('Нельзя')

def save_table_pickle( object, file_name ):
    if object:
        file_name = file_name.replace('.txt', '')+'.txt'
        with open( file_name, 'wb' ) as file:
            pickle.dump( object, file )
    else:
        print('Нельзя')

def print_table( object ):
    if object:
        print(f'\n'+tabulate(object, headers='keys', tablefmt='grid') )
    else:
        print('Пустая таблица')

def get_rows_by_number( object, nachalo, konec ):
    if object:
        while True:
            try:
                assert nachalo.isdigit() and konec.isdigit(), 'нужно ввести число'
                nachalo, konec = int(nachalo), int(konec)
                assert nachalo >= 1 and konec <= len(object), 'такие значения не подходят'
                assert nachalo <= konec, 'начало больше конца'
                return object[ nachalo-1: konec ]

            except Exception as error:
                print(error)
                nachalo = input('Начало: '); konec = input('Конец: ')
    else:
        print('Нельзя')

def get_rows_by_index( object, *znacheniya ):
    if object:
        znacheniya = znacheniya[0]
        itog = []
        for line in object:
            if all(list(line.values())[value].lower().startswith( znacheniya[value].lower() ) for value in range( len(znacheniya) )):
                itog.append(line)
        return itog
    else:
        print('Нельзя')

def find_stolbec( object, by_number ):
    if object:
        while True:
            try:
                zagolovki = [i.lower() for i in list(object[0].keys())]
                if by_number.lower() in zagolovki:
                    stolbec = by_number.capitalize()
                    break
                else:
                    assert by_number.isdigit(), 'Столбец нужно ввести либо названием, либо номером!'
                    assert 1 <= int(by_number) <= len( object[0].keys() ), 'Столбца с таким номером нет!'
                    stolbec = list(object[0].keys())[int(by_number)-1]
                    break
            except Exception as error:
                print(error)
                by_number = input('Название или номер столбца: ')
        return stolbec
    else:
        print('Нельзя')

def type_determine(string):
    if string in ('True', 'False'): 
        return 'Bool'
    elif string.isdigit(): 
        return 'Integer'
    elif string.replace('.', '', 1).isdigit() or string.replace(',', '', 1).isdigit(): 
        return 'Float'
    elif string == 'None': 
        return 'None'
    else: 
        return 'String'

def get_stolbec_types(object, by_number):
    if object:
        stolbec = find_stolbec( object, by_number )
        types = []
        for line in object:
            if type_determine(line[stolbec]) not in types:
                types.append( type_determine(line[stolbec]) )
        return {stolbec: ', '.join(types)}
    else:
        print('Нельзя')

def set_stolbec_types( object, by_number, types ):
    if object:
        stolbec = find_stolbec( object, by_number )
        while all( type.capitalize() not in ['String', 'Integer', 'Float', 'Bool', 'None'] for type in types):
            types = input('Что то пошло не так, ещё раз: ').split()
        types = [i.capitalize() for i in types]
        for line in object:
            line[stolbec] = 'None' if type_determine(line[stolbec]) not in types else line[stolbec]
        return object
    else:
        print('Нельзя')

def set_values( object, stolbec, *values ):
    if object:
        stolbec = find_stolbec(object, stolbec)
        for index in range( len(values) ):
            try:
                object[index][stolbec] = values[index]
            except Exception as error:
                break
        return object
    else:
        print('Нельзя')

def get_values( object, by_number, types ):
    if object:
        stolbec = find_stolbec( object, by_number )
        result = []
        types = [i.capitalize() for i in types]
        for line in object:
            if type_determine(line[stolbec]) in types:
                result.append( line[stolbec] )
        print(f'У столбца {stolbec} {len(result)} значений типа {types}: {result}')
    else:
        print('Нельзя')

def concat( object1, object2 ):
    while not(object1):
        object1 = load_table( input('название файла для первой таблицы: ').split() )
    while not(object2):
        object2 = load_table( input('название файла для второй таблицы: ').split() )
    if object:
        try:
            result = object1+object2
            if result == []:
                return False
            print(f'Новая таблица создана объединением')
            return correct(result)
        except Exception as error:
            print(error)
    else:
        print('Нельзя')

def split( object, row_number ):
    if object:
        while True:
            try:
                assert row_number.isdigit(), 'нужно ввести число'
                assert 1 <= int(row_number) <= len(object), 'такой строки нет'
                row_number = int(row_number)
                return [object[ :row_number ], object[row_number:]]
            except Exception as error:
                print(error)
                row_number = input('Введите номер строки: ')
    else:
        print('Нельзя')

def eq( object, stolbec1, stolbec2 ):
    if object:
        stolbec1 = find_stolbec( object, stolbec1 )
        stolbec2 = find_stolbec( object, stolbec2 )
        rezultat = []
        try:
            for line in object:
                if line[stolbec1] != 'None' and line[stolbec2] != 'None':
                    if (type_determine( line[stolbec1] ) == 'Integer' or type_determine( line[stolbec1] ) == 'Float') and (type_determine( line[stolbec2] ) == 'Integer' or type_determine( line[stolbec2] ) == 'Float'):
                        if float( line[stolbec1] ) == float( line[stolbec2] ):
                            rezultat.append(line)
                    else:
                        if line[stolbec1] == line[stolbec2]:
                            rezultat.append(line)
        except Exception as oshibka:
            print(oshibka)
        print(rezultat)
        return rezultat
    else:
        print('Нельзя')

def gr( object, stolbec1, stolbec2 ):
    if object:
        stolbec1 = find_stolbec( object, stolbec1 )
        stolbec2 = find_stolbec( object, stolbec2 )
        rezultat = []
        try:
            for line in object:
                if line[stolbec1] != 'None' and line[stolbec2] != 'None':
                    if (type_determine( line[stolbec1] ) == 'Integer' or type_determine( line[stolbec1] ) == 'Float') and (type_determine( line[stolbec2] ) == 'Integer' or type_determine( line[stolbec2] ) == 'Float'):
                        if float( line[stolbec1] ) > float( line[stolbec2] ):
                            rezultat.append(line)
                    else:
                        if line[stolbec1] > line[stolbec2]:
                            rezultat.append(line)
        except Exception as oshibka:
            print(oshibka)
        return rezultat
    else:
        print('Нельзя')

def ls( object, stolbec1, stolbec2 ):
    if object:
        stolbec1 = find_stolbec( object, stolbec1 )
        stolbec2 = find_stolbec( object, stolbec2 )
        rezultat = []
        try:
            for line in object:
                if line[stolbec1] != 'None' and line[stolbec2] != 'None':
                    if (type_determine( line[stolbec1] ) == 'Integer' or type_determine( line[stolbec1] ) == 'Float') and (type_determine( line[stolbec2] ) == 'Integer' or type_determine( line[stolbec2] ) == 'Float'):
                        if float( line[stolbec1] ) < float( line[stolbec2] ):
                            rezultat.append(line)
                    else:
                        if line[stolbec1] < line[stolbec2]:
                            rezultat.append(line)
        except Exception as oshibka:
            print(oshibka)
        return rezultat
    else:
        print('Нельзя')

def ge( object, stolbec1, stolbec2 ):
    if object:
        stolbec1 = find_stolbec( object, stolbec1 )
        stolbec2 = find_stolbec( object, stolbec2 )
        rezultat = []
        try:
            for line in object:
                if line[stolbec1] != 'None' and line[stolbec2] != 'None':
                    if (type_determine( line[stolbec1] ) == 'Integer' or type_determine( line[stolbec1] ) == 'Float') and (type_determine( line[stolbec2] ) == 'Integer' or type_determine( line[stolbec2] ) == 'Float'):
                        if float( line[stolbec1] ) >= float( line[stolbec2] ):
                            rezultat.append(line)
                    else:
                        if line[stolbec1] >= line[stolbec2]:
                            rezultat.append(line)
        except Exception as oshibka:
            print(oshibka)
        return rezultat
    else:
        print('Нельзя')

def le( object, stolbec1, stolbec2 ):
    if object:
        stolbec1 = find_stolbec( object, stolbec1 )
        stolbec2 = find_stolbec( object, stolbec2 )
        rezultat = []
        try:
            for line in object:
                if line[stolbec1] != 'None' and line[stolbec2] != 'None':
                    if (type_determine( line[stolbec1] ) <= 'Integer' or type_determine( line[stolbec1] ) == 'Float') and (type_determine( line[stolbec2] ) == 'Integer' or type_determine( line[stolbec2] ) == 'Float'):
                        if float( line[stolbec1] ) <= float( line[stolbec2] ):
                            rezultat.append(line)
                    else:
                        if line[stolbec1] <= line[stolbec2]:
                            rezultat.append(line)
        except Exception as oshibka:
            print(oshibka)
        return rezultat
    else:
        print('Нельзя')

def ne( object, stolbec1, stolbec2 ):
    if object:
        stolbec1 = find_stolbec( object, stolbec1 )
        stolbec2 = find_stolbec( object, stolbec2 )
        rezultat = []
        try:
            for line in object:
                if line[stolbec1] != 'None' and line[stolbec2] != 'None':
                    if (type_determine( line[stolbec1] ) == 'Integer' or type_determine( line[stolbec1] ) == 'Float') and (type_determine( line[stolbec2] ) == 'Integer' or type_determine( line[stolbec2] ) == 'Float'):
                        if float( line[stolbec1] ) != float( line[stolbec2] ):
                            rezultat.append(line)
                    else:
                        if line[stolbec1] != line[stolbec2]:
                            rezultat.append(line)
        except Exception as oshibka:
            print(oshibka)
        return rezultat
    else:
        print('Нельзя')

def add( object, stolbec1, stolbec2 ):
    if object:
        stolbec1 = find_stolbec( object, stolbec1 )
        stolbec2 = find_stolbec( object, stolbec2 )
        result = []
        for line in object:
            if line[stolbec1] != 'None' and line[stolbec2] != 'None':
                if (type_determine( line[stolbec1] ) == 'Integer' or type_determine( line[stolbec1] ) == 'Float') and (type_determine( line[stolbec2] ) == 'Integer' or type_determine( line[stolbec2] ) == 'Float'):
                    result.append( {'Результат суммы':  str(float(line[stolbec1])+float(line[stolbec2]))} )
                else:
                    result.append( {'Результат суммы': line[stolbec1]+line[stolbec2]} )
            else:
                result.append( {'Результат суммы': 'None'} )
        print_table( result )
    else:
        print('Нельзя')

def sub( object, stolbec1, stolbec2 ):
    if object:
        stolbec1 = find_stolbec( object, stolbec1 )
        stolbec2 = find_stolbec( object, stolbec2 )
        result = []
        for line in object:
            if line[stolbec1] != 'None' and line[stolbec2] != 'None':
                if (type_determine( line[stolbec1] ) == 'Integer' or type_determine( line[stolbec1] ) == 'Float') and (type_determine( line[stolbec2] ) == 'Integer' or type_determine( line[stolbec2] ) == 'Float'):
                    result.append( {'Результат разности':  str(float(line[stolbec1])-float(line[stolbec2]))} )
                else:
                    result.append( {'Результат разности': 'None'} )
            else:
                result.append( {'Результат разности': 'None'} )
        print_table( result )
    else:
        print('Нельзя')

def mul( object, stolbec1, stolbec2 ):
    if object:
        stolbec1 = find_stolbec( object, stolbec1 )
        stolbec2 = find_stolbec( object, stolbec2 )
        result = []
        for line in object:
            if line[stolbec1] != 'None' and line[stolbec2] != 'None':
                if (type_determine( line[stolbec1] ) == 'Integer' or type_determine( line[stolbec1] ) == 'Float') and (type_determine( line[stolbec2] ) == 'Integer' or type_determine( line[stolbec2] ) == 'Float'):
                    result.append( {'Результат произведения':  str(float(line[stolbec1])*float(line[stolbec2]))} )
                else:
                    result.append( {'Результат произведения': 'None'} )
            else:
                result.append( {'Результат произведения': 'None'} )
        print_table( result )
    else:
        print('Нельзя')

def div( object, stolbec1, stolbec2 ):
    if object:
        stolbec1 = find_stolbec( object, stolbec1 )
        stolbec2 = find_stolbec( object, stolbec2 )
        result = []
        for line in object:
            if line[stolbec1] != 'None' and line[stolbec2] != 'None':
                if (type_determine( line[stolbec1] ) == 'Integer' or type_determine( line[stolbec1] ) == 'Float') and (type_determine( line[stolbec2] ) == 'Integer' or type_determine( line[stolbec2] ) == 'Float'):
                    result.append( {'Результат частности':  str(float(line[stolbec1])/float(line[stolbec2]))} )
                else:
                    result.append( {'Результат частности': 'None'} )
            else:
                result.append( {'Результат частности': 'None'} )
        print_table( result )
    else:
        print('Нельзя')


    
#загрузка таблицы
a = load_table( input('с какого файла загружать - ').split() )
print_table( a )

#сохранение таблицы в csv
save_table_csv( a, input('название файла - ') )

#сохранение таблицы в csv
# save_table_pickle( a, input('название файла - ') )

#вырез таблицы по номерам
# b = get_rows_by_number(a, nachalo=input('начало - '), konec=input('конец - '))
# print_table(b)

#вырез таблицы по значениям столбцов
# b = get_rows_by_index(a, input('ключевые слова через пробел - ').split())
# print_table(b)

#показывает как типы данных есть в столбце
# b = get_stolbec_types(a, input('столбец - '))
# print(b)

#оставляет в столбце только введённые типы
# b = set_stolbec_types( a, input('столбец - '), input('типы (можно через пробел) - ').split() )
# print_table(b)

#присваивает столбцу введённые значения
# set_values( a, input('столбец - '), *input('какие значения присвоить - ').split() )
# print_table(a)

#показывает ячейки столбца, которые принадлежат одному из введённых типов данных
# get_values( a, input('столбец - '), input('типы (можно через пробел) - ').split() )

#объединяет две таблицу в одну функцией concat
# b = load_table( input('название файла - ').split() )
# print_table(b)
# c = concat(a,b)
# print_table(c)

#разделяет таблицу на две таблицы по разрывающей строке
# b,c = split(a, input('номер строки, через которую надо разорвать таблицу - '))
# print_table(b)
# print_table(c)

#оставляет строки исходя из операции
# stolbec1 = input('первый столбец - ')
# stolbec2 = input('второй столбец - ')
# b = eq(a, stolbec1, stolbec2) #только те строки, где первый столбец равен второму
# print_table(b)

# b = gr(a, stolbec1, stolbec2) #только те строки, где первый столбец больше второго
# print_table(b)

# b = ls(a, stolbec1, stolbec2) #только те строки, где первый столбец меньше второго
# print_table(b)

# b = ge(a, stolbec1, stolbec2) #только те строки, где первый столбец >= второго
# print_table(b)

# b = le(a, stolbec1, stolbec2) #только те строки, где первый столбец <= второму
# print_table(b)

# b = ne(a, stolbec1, stolbec2) #только те строки, где первый столбец != второму
# print_table(b)


#производит арифм.операции и выводит новую таблицу с результатом
#лучше загрузить таблицу с файла test4.csv
# stolbec1 = input('первый столбец - ')
# stolbec2 = input('второй столбец - ')
# add(a, stolbec1, stolbec2)
# sub(a, stolbec1, stolbec2)
# mul(a, stolbec1, stolbec2)
# div(a, stolbec1, stolbec2)


# In[ ]:




