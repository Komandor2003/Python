#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import re
from copy import deepcopy
import os.path


class Field(object):
    position = [['            '  for _ in range(8)] for _ in range(8)]
    colour = 'BLACK'
    whiteCheck = False
    blackCheck = False
    record = {}
    gameRecord = {}
    counter = 0
    gameCounter = 0
    newGameRecord = {}

    def __init__(self, x, y):

        self.x = x
        self.y = y

    def field(self):
        return f'╔====╦=====╦=====╦=====╦=====╦=====╦=====╦=====╦=====╦=====╗\n'                f'|{"WH":^4}|{"A":^4} |{"B":^4} |{"C":^4} |{"D":^4} |{"E":^4} |{"F":^4} |{"G":^4} |{"H":^4} |{"WH":^4} |\n'                f'╠====╬=====╬=====╬=====╬=====╬=====╬=====╬=====╬=====╬=====╣\n'                f'|{"1":^4}|{str(Field.position[0][0]):^4}|{str(Field.position[0][1]):^4}|{str(Field.position[0][2]):^4}|{str(Field.position[0][3]):^4}|{str(Field.position[0][4]):^4} |{str(Field.position[0][5]):^4}|{str(Field.position[0][6]):^4} |{str(Field.position[0][7]):^4}|{"1":^4}|\n'                f'╠====╬=====╬=====╬=====╬=====╬=====╬=====╬=====╬=====╬=====╣\n'                f'|{"2":^4}|{str(Field.position[1][0]):^4}|{str(Field.position[1][1]):^4}|{str(Field.position[1][2]):^4}|{str(Field.position[1][3]):^4}|{str(Field.position[1][4]):^4} |{str(Field.position[1][5]):^4}|{str(Field.position[1][6]):^4} |{str(Field.position[1][7]):^4}|{"2":^4}|\n'                f'╠====╬=====╬=====╬=====╬=====╬=====╬=====╬=====╬=====╬=====╣\n'                f'|{"3":^4}|{str(Field.position[2][0]):^4} |{str(Field.position[2][1]):^4} |{str(Field.position[2][2]):^4} |{str(Field.position[2][3]):^4} |{str(Field.position[2][4]):^4} |{str(Field.position[2][5]):^4} |{str(Field.position[2][6]):^4} |{str(Field.position[2][7]):^4} |{"3":^4} |\n'                f'╠====╬=====╬=====╬=====╬=====╬=====╬=====╬=====╬=====╬=====╣\n'                f'|{"4":^4}|{str(Field.position[3][0]):^4} |{str(Field.position[3][1]):^4} |{str(Field.position[3][2]):^4} |{str(Field.position[3][3]):^4} |{str(Field.position[3][4]):^4} |{str(Field.position[3][5]):^4} |{str(Field.position[3][6]):^4} |{str(Field.position[3][7]):^4} |{"4":^4} |\n'                f'╠====╬=====╬=====╬=====╬=====╬=====╬=====╬=====╬=====╬=====╣\n'                f'|{"5":^4}|{str(Field.position[4][0]):^4} |{str(Field.position[4][1]):^4} |{str(Field.position[4][2]):^4} |{str(Field.position[4][3]):^4} |{str(Field.position[4][4]):^4} |{str(Field.position[4][5]):^4} |{str(Field.position[4][6]):^4} |{str(Field.position[4][7]):^4} |{"5":^4} |\n'                f'╠====╬=====╬=====╬=====╬=====╬=====╬=====╬=====╬=====╬=====╣\n'                f'|{"6":^4}|{str(Field.position[5][0]):^4} |{str(Field.position[5][1]):^4} |{str(Field.position[5][2]):^4} |{str(Field.position[5][3]):^4} |{str(Field.position[5][4]):^4} |{str(Field.position[5][5]):^4} |{str(Field.position[5][6]):^4} |{str(Field.position[5][7]):^4} |{"6":^4} |\n'                f'╠====╬=====╬=====╬=====╬=====╬=====╬=====╬=====╬=====╬=====╣\n'                f'|{"7":^4}|{str(Field.position[6][0]):^4}|{str(Field.position[6][1]):^4}|{str(Field.position[6][2]):^4}|{str(Field.position[6][3]):^4}|{str(Field.position[6][4]):^4} |{str(Field.position[6][5]):^4}|{str(Field.position[6][6]):^4} |{str(Field.position[6][7]):^4}|{"7":^4}|\n'                f'╠====╬=====╬=====╬=====╬=====╬=====╬=====╬=====╬=====╬=====╣\n'                f'|{"8":^4}|{str(Field.position[7][0]):^4}|{str(Field.position[7][1]):^4}|{str(Field.position[7][2]):^4}|{str(Field.position[7][3]):^4}|{str(Field.position[7][4]):^4} |{str(Field.position[7][5]):^4}|{str(Field.position[7][6]):^4} |{str(Field.position[7][7]):^4}|{"8":^4}|\n'                f'╠====╬=====╬=====╬=====╬=====╬=====╬=====╬=====╬=====╬=====╣\n'                f'|{"BL":^4}|{"A":^4} |{"B":^4} |{"C":^4} |{"D":^4} |{"E":^4} |{"F":^4} |{"G":^4} |{"H":^4} |{"BL":^4} |\n'                f'╚====╩=====╩=====╩=====╩=====╩=====╩=====╩=====╩=====╩=====╝'

    def colourSwap(self):
        if Field.colour == 'WHITE':
            Field.colour = 'BLACK'
            return 'BLACK'
        else:
            Field.colour = 'WHITE'
            return 'WHITE'


class Pawn(Field):  # класс пешки, функция проверки хода
    moves = 0

    def __init__(self, colour):
        self.colour = colour

    def __repr__(self):
        if self.colour == 'WHITE':
            return '♙'
        else:
            return '♟'

    def itself(self):
        return f'Pawn {self.colour}'

    def move(self, fl1, fl2):
        if self.colour == 'WHITE':
            delt = 1
        else:
            delt = -1
        if (fl1.x == fl2.x) and (fl2.y - fl1.y == delt) and (Field.position[fl2.y][fl2.x] == ''):
            Field.position[fl1.y][fl1.x].moves += 1
            return True
        elif (fl1.x == fl2.x) and (fl2.y - fl1.y == 2 * delt) and (Field.position[fl2.y][fl2.x] == ''):
            if (fl1.y == 1 and self.colour == 'WHITE') or (fl1.y == 6 and self.colour == 'BLACK'):
                Field.position[fl1.y][fl1.x].moves += 1
                return True
        elif abs(fl1.x - fl2.x) == 1 and (fl2.y - fl1.y == delt) and (Field.position[fl2.y][fl2.x] != '')                 and (Field.position[fl2.y][fl2.x].colour != Field.position[fl1.y][fl1.x].colour):
            Field.position[fl1.y][fl1.x].moves += 1
            return True
        elif abs(fl1.x - fl2.x) == 1 and (fl2.y - fl1.y == delt) and (Field.position[fl2.y][fl2.x] == '')                 and (Field.position[fl1.y][fl2.x] != ''):
            if Field.position[fl1.y][fl2.x].moves == 1:
                if Field.newGameRecord[len(Field.newGameRecord)].split()[2] == f'{chr(fl2.x + 65)}{fl1.y + 1}':
                    Field.position[fl1.y][fl1.x].moves += 1
                    Field.position[fl1.y][fl2.x] = ' '
                    return True
        else:
            return False

    def transform(self, x1, y1, x2, y2, pawnTransformation,
                  colr):  # превращение пешки в фигуру при достижении конца доски
        if Field.position[y1][x1].move(Field(x1, y1), Field(x2, y2)):
            if pawnTransformation == 'Kn':
                Field.position[y2][x2] = Knight(colr)
            elif pawnTransformation == 'R':
                Field.position[y2][x2] = Rook(colr)
            elif pawnTransformation == 'B':
                Field.position[y2][x2] = Bishop(colr)
            elif pawnTransformation == 'Q':
                Field.position[y2][x2] = Queen(colr)
            elif pawnTransformation == 'P':
                Field.position[y2][x2] = Pawn(colr)
            Field.position[y1][x1] = ' '


class Rook(Field):  # класс ладьи, функция проверки хода
    moves = 0

    def __init__(self, colour):
        self.colour = colour

    def __repr__(self):
        if self.colour == 'WHITE':
            return '♖'
        else:
            return '♜'

    def itself(self):
        return f'Rook {self.colour}'

    def move(self, fl1, fl2):
        if self.colour == 'WHITE':
            delt = 1
        else:
            delt = -1

        if Field.position[fl2.y][fl2.x] != '':
            if Field.position[fl2.y][fl2.x].colour == Field.position[fl1.y][fl1.x].colour:
                return False

        if fl1.x == fl2.x:
            for iner in range(min(fl1.y, fl2.y) + 1, max(fl2.y, fl1.y)):
                if Field.position[iner][fl1.x] != '':
                    return False

        elif fl1.y == fl2.y:
            for iner in range(min(fl1.x, fl2.x) + 1, max(fl2.x, fl1.x)):
                if Field.position[fl1.y][iner] != '':
                    return False

        else:
            return False

        Field.position[fl1.y][fl1.x].moves += 1
        return True


class Knight(Field):  # класс коня, функция проверки хода
    def __init__(self, colour):
        self.colour = colour

    def __repr__(self):
        if self.colour == 'WHITE':
            return '♘'
        else:
            return '♞'

    def itself(self):
        return f'Knight {self.colour}'

    def move(self, fl1, fl2):
        if self.colour == 'WHITE':
            delt = 1
        else:
            delt = -1

        if Field.position[fl2.y][fl2.x] != '':
            if Field.position[fl2.y][fl2.x].colour == Field.position[fl1.y][fl1.x].colour:
                return False

        if (abs(fl1.x - fl2.x) == 1 and abs(fl1.y - fl2.y) == 2) or (
                abs(fl1.x - fl2.x) == 2 and abs(fl1.y - fl2.y) == 1):
            return True

        return False


class Bishop(Field):  # класс слона, функция проверки хода
    def __init__(self, colour):
        self.colour = colour

    def __repr__(self):
        if self.colour == 'WHITE':
            return '♗'
        else:
            return '♝'

    def itself(self):
        return f'Bishop {self.colour}'

    def move(self, fl1, fl2):
        if self.colour == 'WHITE':
            delt = 1
        else:
            delt = -1

        if Field.position[fl2.y][fl2.x] != '':
            if Field.position[fl2.y][fl2.x].colour == Field.position[fl1.y][fl1.x].colour:
                return False

        if fl2.x - fl1.x == -(fl2.y - fl1.y):
            for i in range(min(fl1.x, fl2.x) + 1, max(fl1.x, fl2.x)):
                if Field.position[max(fl1.y, fl2.y) - i + min(fl1.x, fl2.x)][i] != '':
                    return False

        elif fl2.x - fl1.x == fl2.y - fl1.y:
            for i in range(min(fl1.x, fl2.x) + 1, max(fl1.x, fl2.x)):
                if Field.position[min(fl1.y, fl2.y) - min(fl1.x, fl2.x) + i][i] != '':
                    return False

        else:
            return False

        return True


class Queen(Field):  # класс ферзя, функция проверки хода
    def __init__(self, colour):
        self.colour = colour

    def __repr__(self):
        if self.colour == 'WHITE':
            return '♕'
        else:
            return '♛'

    def itself(self):
        return f'Queen {self.colour}'

    def move(self, fl1, fl2):
        if self.colour == 'WHITE':
            delt = 1
        else:
            delt = -1

        if Field.position[fl2.y][fl2.x] != '':
            if Field.position[fl2.y][fl2.x].colour == Field.position[fl1.y][fl1.x].colour:
                return False

        if fl2.x - fl1.x == -(fl2.y - fl1.y):
            for i in range(min(fl1.x, fl2.x) + 1, max(fl1.x, fl2.x)):
                if Field.position[max(fl1.y, fl2.y) - i + min(fl1.x, fl2.x)][i] != '':
                    return False

        elif fl2.x - fl1.x == fl2.y - fl1.y:
            for i in range(min(fl1.x, fl2.x) + 1, max(fl1.x, fl2.x)):
                if Field.position[min(fl1.y, fl2.y) - min(fl1.x, fl2.x) + i][i] != '':
                    return False

        elif fl1.x == fl2.x:
            for iner in range(min(fl1.y, fl2.y) + 1, max(fl2.y, fl1.y)):
                if Field.position[iner][fl1.x] != '':
                    return False

        elif fl1.y == fl2.y:
            for iner in range(min(fl1.x, fl2.x) + 1, max(fl2.x, fl1.x)):
                if Field.position[fl1.y][iner] != '':
                    return False

        else:
            return False

        return True


class King(Field):  # класс коня, функция проверки хода, функция рокировки
    moves = 0

    def __init__(self, colour):
        self.colour = colour

    def __repr__(self):
        if self.colour == 'WHITE':
            return '♔'
        else:
            return '♚'

    def itself(self):
        return f'King {self.colour}'

    def castling(self, turn, place, colr, saves):
        if Field.position[place][4].moves == 0:
            if turn == '0-0':
                if Field.position[place][7]:
                    if Field.position[place][7].itself()[:4] == 'Rook':
                        if Field.position[place][7].moves == 0:
                            if Field.position[place][5] == '' and Field.position[place][6] == '':
                                if not chekmate(colr=colr, sec=True):
                                    Field.position[place][5] = Field.position[place][4]
                                    Field.position[place][4] = ''
                                    if not chekmate(colr=colr, sec=True):
                                        Field.position[place][6] = Field.position[place][5]
                                        Field.position[place][5] = ''
                                        if not chekmate(colr=colr, sec=True):
                                            Field.position[place][5] = Field.position[place][7]
                                            Field.position[place][7] = ''
                                            Field.position[place][6].moves += 1
                                            return True

            elif turn == '0-0-0':
                if Field.position[place][0]:
                    if Field.position[place][0].itself()[:4] == 'Rook':
                        if Field.position[place][0].moves == 0:
                            if Field.position[place][1] == '' and Field.position[place][2] == '' and                                     Field.position[place][3] == '':
                                if not chekmate(colr=colr, sec=True):
                                    Field.position[place][3] = Field.position[place][4]
                                    Field.position[place][4] = ''
                                    if not chekmate(colr=colr, sec=True):
                                        Field.position[place][2] = Field.position[place][3]
                                        Field.position[place][3] = ''
                                        if not chekmate(colr=colr, sec=True):
                                            Field.position[place][3] = Field.position[place][0]
                                            Field.position[place][0] = ''
                                            Field.position[place][2].moves += 1
                                            return True
        Field.position = saves
        return False

    def move(self, fl1, fl2):
        if self.colour == 'WHITE':
            delt = 1
        else:
            delt = -1

        if Field.position[fl2.y][fl2.x] != '':
            if Field.position[fl2.y][fl2.x].colour == Field.position[fl1.y][fl1.x].colour:
                return False

        if (abs(fl1.x - fl2.x) == 1 and abs(fl1.y - fl2.y) == 1) or (
                abs(fl1.x - fl2.x) == 0 and abs(fl1.y - fl2.y) == 1) \
                or (abs(fl1.x - fl2.x) == 1 and abs(fl1.y - fl2.y) == 0):
            Field.position[fl1.y][fl1.x].moves += 1
            return True

        return False


def anticol(colr):
    if colr == 'WHITE':
        return 'BLACK'
    else:
        return 'WHITE'


def chekmate(colr, xK=-1, yK=-1, sec=False):  # функция проверки шаха
    xA, yA = -1, -1
    if xK == -1 and yK == -1:
        for y in range(8):
            for x in range(8):
                if Field.position[y][x]:
                    if Field.position[y][x].itself() == 'King ' + anticol(colr):
                        xK, yK = x, y

    for y in range(8):
        for x in range(8):
            if Field.position[y][x]:
                if Field.position[y][x].colour == colr:
                    if Field.position[y][x].move(Field(x, y), Field(xK, yK)):
                        xA, yA = x, y

    if xA == -1 and yA == -1:
        if not sec:
            if colr == 'WHITE':
                Field.blackCheck = False
            else:
                Field.whiteCheck = False
        return False
    move1, move2, move3 = -1, -1, 0
    if sec:
        return True

    for dx in range(-1, 2):  # может ли король уйти от шаха
        for dy in range(-1, 2):
            if dx or dy:
                if 0 <= xK + dx <= 7 and 0 <= dy + yK <= 7:
                    if Field.position[yK][xK].move(Field(xK, yK), Field(xK + dx, yK + dy)):
                        Field.position[yK + dy][xK + dx] = Field.position[yK][xK]
                        Field.position[yK][xK] = ''
                        if not chekmate(colr=colr, xK=xK + dx, yK=yK + dy, sec=True):
                            move1 = 1
                        Field.position[yK][xK] = Field.position[yK + dy][xK + dx]
                        Field.position[yK + dy][xK + dx] = ''

    if abs(xA - xK) <= 1 and abs(yK - yA) <= 1:
        move2 = -1
    else:
        possibleMove = []
        checkField = []
        for y in range(min(yK, yA), max(yK, yA) + 1):  # может ли фигура перекрыть атакующую фигуру
            row = []
            for x in range(min(xK, xA), max(xK, xA) + 1):
                row.append(Field.position[y][x])
            checkField.append(row)

        if Field.position[yA][xA].itself()[:6] == 'Knight':
            move2 = -1
        else:
            if xA != xK and yA != yK:
                if xK < xA:
                    for i in range(1, len(checkField) - 1):
                        possibleMove.append(Field(min(xK, xA) + i, min(yK, yA) + i))
                else:
                    for i in range(1, len(checkField) - 1):
                        possibleMove.append(Field(min(xK, xA) + i, max(yK, yA) - i))

            elif xA != xK and yA == yK:
                for i in range(1, len(checkField) - 1):
                    possibleMove.append(Field(min(xK, xA) + i, yK))

            elif xA == xK and yA != yK:
                for i in range(1, len(checkField) - 1):
                    possibleMove.append(Field(xK, min(yK, yA) + i))

        for y in range(8):
            for x in range(8):
                if Field.position[y][x]:
                    if Field.position[y][x].colour == anticol(colr):
                        for fl in possibleMove:
                            if Field.position[y][x].move(Field(x, y), fl):
                                move2 = 1

    for y in range(8):  # может ли фигура съесть атакующую фигуру
        for x in range(8):
            if Field.position[y][x]:
                if Field.position[y][x].colour == anticol(colr):
                    if Field.position[y][x].move(Field(x, y), Field(xA, yA)):
                        if Field.position[y][x].itself() != 'King ' + anticol(colr):
                            if colr == 'BLACK':
                                Field.whiteCheck = True
                            else:
                                Field.blackCheck = True
                            print(f'Шах для {anticol(colr)}')
                            return False
                        else:
                            store = Field.position[yA][xA]
                            Field.position[yA][xA] = Field.position[yK][xK]
                            Field.position[yK][xK] = ''
                            if not chekmate(colr=colr, xK=xA, yK=yA, sec=True):
                                Field.position[yK][xK] = Field.position[yA][xA]
                                Field.position[yA][xA] = store
                                if colr == 'BLACK':
                                    Field.whiteCheck = True
                                else:
                                    Field.blackCheck = True
                                print(f'Шах для {anticol(colr)}')
                                return False
                            else:
                                move3 = -1
                                Field.position[yK][xK] = Field.position[yA][xA]
                                Field.position[yA][xA] = store

    if move1 == -1 and move2 == -1 and move3 == -1:
        return True  # шах и мат
    else:
        if colr == 'BLACK':
            Field.whiteCheck = True
        else:
            Field.blackCheck = True
        print(f'Шах для {anticol(colr)}')
        return False


def rec(file):  # запись игры в файл
    with open(file, 'w+') as f:
        count = 0
        for k, v in Field.newGameRecord.items():
            if k % 2 == 1:
                count += 1
                f.write(str(count) + ' ' + v.split()[1] + '-' + v.split()[2] + ' ')
            else:
                f.write(v.split()[1] + '-' + v.split()[2] + '\n')


def listMatch(file):  # чтение игры из файла
    r = re.compile(r"[a-hA-H][1-8]")
    with open(file, 'r') as f:
        counter = 1
        for line in f:
            t11, t12, t21, t22 = '', '', '', ''
            turn1, turn2 = '', ''
            try:
                turn1 = line.split()[1]
                turn2 = line.split()[2]
            except BaseException:
                pass
            if ':' in turn1:
                t11 = (r.search(turn1.split(':')[0])).group(0)
                t12 = (r.search(turn1.split(':')[1])).group(0)
            elif '-' in turn1:
                t11 = (r.search(turn1.split('-')[0])).group(0)
                t12 = r.search(turn1.split('-')[1]).group(0)
            if ':' in turn2:
                t21 = r.search(turn2.split(':')[0]).group(0)
                t22 = r.search(turn2.split(':')[1]).group(0)
            elif '-' in turn2:
                t21 = r.search(turn2.split('-')[0]).group(0)
                t22 = r.search(turn2.split('-')[1]).group(0)

            Field.record[counter] = f'{t11.upper()} {t12.upper()}'
            Field.record[counter + 1] = f'{t21.upper()} {t22.upper()}'
            counter += 2


def gameStart(file=''):  # функция игры
    Field.position = [['' for _ in range(8)] for _ in range(8)]
    Field.colour = 'BLACK'
    Field.whiteCheck = False
    Field.blackCheck = False
    Field.record = {}
    Field.gameRecord = {}
    Field.counter = 0
    Field.gameCounter = 0
    Field.newGameRecord = {}

    if file:
        if not os.path.exists(file):
            print('Данный файл не существует, введите команду еще раз')
            return False
        else:
            listMatch(file)

    game = Field(1, 1)  # расстановка фигур
    Field.position[7] = [Rook('BLACK'), Knight('BLACK'), Bishop('BLACK'), Queen('BLACK'),
                         King('BLACK'), Bishop('BLACK'), Knight('BLACK'), Rook('BLACK')]
    Field.position[6] = [Pawn('BLACK'), Pawn('BLACK'), Pawn('BLACK'), Pawn('BLACK'),
                         Pawn('BLACK'), Pawn('BLACK'), Pawn('BLACK'), Pawn('BLACK')]
    Field.position[1] = [Pawn('WHITE'), Pawn('WHITE'), Pawn('WHITE'), Pawn('WHITE'),
                         Pawn('WHITE'), Pawn('WHITE'), Pawn('WHITE'), Pawn('WHITE')]
    Field.position[0] = [Rook('WHITE'), Knight('WHITE'), Bishop('WHITE'), Queen('WHITE'),
                         King('WHITE'), Bishop('WHITE'), Knight('WHITE'), Rook('WHITE')]

    print(Field.field(game))
    while True:
        pawnTransformation = ''
        colour = game.colourSwap()
        print(f'Ход {colour}')
        ok = False
        while not ok:
            try:
                turn = input('Введите клетку для выбора а затем через пробел клетку хода фигуры')  # запись ходаA2 A3
                if turn == '0-0' or turn == '0-0-0':
                    ok = True
                    continue
                elif turn == 'next':  # перемещение по записанной партии
                    Field.gameRecord[Field.counter] = deepcopy(Field.position)
                    Field.counter += 1
                    fl = Field.record[Field.counter]
                    print(f'Следующий ход - {fl}')
                    x1 = ord(fl.split()[0][:1]) - 65
                    y1 = int((fl.split()[0])[1:]) - 1
                    x2 = ord(fl.split()[1][:1]) - 65
                    y2 = int((fl.split()[1])[1:]) - 1
                    ok = True
                    continue

                elif turn == 'prev':
                    Field.gameRecord[Field.counter] = deepcopy(Field.position)
                    Field.counter -= 1
                    fl = Field.record[Field.counter]
                    print(f'Предыдущий ход - {fl}')
                    Field.position = Field.gameRecord[Field.counter]
                    game.colourSwap()
                    ok = True
                    continue

                elif turn[:9] == 'record to':
                    rec(turn[10:])
                    continue

                elif turn == 'exit':
                    ok = True
                    return False

                x1 = ord(turn.split()[0][0]) - 65
                y1 = int((turn.split()[0])[1]) - 1
                x2 = ord(turn.split()[1][0]) - 65
                y2 = int((turn.split()[1])[1]) - 1
                if '=' in turn.split()[1]:
                    pawnTransformation = turn.split()[1][3]
                if 0 <= x1 <= 7 and 0 <= x2 <= 7 and 0 <= y1 <= 7 and 0 <= y2 <= 7 and pawnTransformation in ['Kn', 'B',
                                                                                                              'Q', 'R',
                                                                                                              'P', '']:
                    ok = True

                else:
                    print('Неверный ход: неверный ввод команды или клетки')
            except BaseException:
                print('Неверный ход: неверный ввод команды или клетки')

        if turn == '0-0' or turn == '0-0-0':  # если ход - рокировка
            save = Field.position
            if colour == 'WHITE':
                if Field.position[0][4]:
                    if Field.position[0][4].itself() == 'King WHITE':
                        if not Field.position[0][4].castling(turn, 0, anticol(colour), save):
                            print('Неверный ход: рокировка не возможна')
                            colour = game.colourSwap()
                            print(Field.field(game))
                            continue
                        else:
                            Field.gameCounter += 1
                            Field.newGameRecord[
                                Field.gameCounter] = f'{Field.gameCounter}- {chr(x1 + 65)}{y1 + 1} {chr(x2 + 65)}{y2 + 1}'
                            print(Field.field(game))
                            continue
            else:
                if Field.position[7][4]:
                    if Field.position[7][4].itself() == 'King BLACK':
                        if not Field.position[7][4].castling(turn, 7, anticol(colour), save):
                            print('Неверный ход: рокировка невозможна')
                            colour = game.colourSwap()
                            print(Field.field(game))
                            continue
                        else:
                            Field.gameCounter += 1
                            Field.newGameRecord[
                                Field.gameCounter] = f'{Field.gameCounter}- {chr(x1 + 65)}{y1 + 1} {chr(x2 + 65)}{y2 + 1}'
                            print(Field.field(game))
                            continue

        if Field.position[y1][x1] == '':
            print('Неверный ход: пустая клетка')
            colour = game.colourSwap()
            print(Field.field(game))
            continue

        if Field.position[y1][x1].colour == colour:
            if not Field.position[y1][x1].move(Field(x1, y1), Field(x2, y2)):
                print('Неверный ход: фигура не может сходить на заданную клетку')
                colour = game.colourSwap()
                print(Field.field(game))
                continue

            elif Field.position[y2][x2] == King(anticol(colour)):
                print('Неверный ход: фигура не может съесть короля')
                colour = game.colourSwap()
                print(Field.field(game))
                continue
            else:
                if colour == 'WHITE':  # проверка на шах, проверка избавляется ли игрок от шаха
                    if Field.whiteCheck:
                        store = Field.position[y2][x2]
                        Field.position[y2][x2] = Field.position[y1][x1]
                        Field.position[y1][x1] = ''
                        print(Field.field(game))
                        chekmate(anticol(colour))
                        if Field.whiteCheck:
                            Field.position[y1][x1] = Field.position[y2][x2]
                            Field.position[y2][x2] = store
                            print('Неверный ход: вам все еще объявлен шах')
                            colour = game.colourSwap()
                            print(Field.field(game))
                            continue
                        Field.position[y1][x1] = Field.position[y2][x2]
                        Field.position[y2][x2] = store
                    else:
                        if Field.position[y1][x1].itself()[:4] == 'Pawn':
                            if y1 == 6 and y2 == 7:
                                if not pawnTransformation:
                                    print('Неверный ход: укажите, в какую фигуру должна превратиться пешкаБ например:\n'
                                          'P - пешка, R - ладья, Kn - конь, B - слон, Q - ферзь\n'
                                          'Пример хода: E7 E8=Q')
                                    colour = game.colourSwap()
                                    print(Field.field(game))
                                    continue
                                else:
                                    Field.position[y1][x1].transform(x1, y1, x2, y2, pawnTransformation, colour)
                                    print(Field.field(game))
                                    Field.gameCounter += 1
                                    Field.newGameRecord[
                                        Field.gameCounter] = f'{Field.gameCounter}- {chr(x1 + 65)}{y1 + 1} {chr(x2 + 65)}{y2 + 1}'
                                    continue
                    Field.gameCounter += 1
                    Field.newGameRecord[
                        Field.gameCounter] = f'{Field.gameCounter}- {chr(x1 + 65)}{y1 + 1} {chr(x2 + 65)}{y2 + 1}'
                    Field.position[y2][x2] = Field.position[y1][x1]
                    Field.position[y1][x1] = ''

                elif colour == 'BLACK':
                    if Field.blackCheck:
                        store = Field.position[y2][x2]
                        Field.position[y2][x2] = Field.position[y1][x1]
                        Field.position[y1][x1] = ''
                        chekmate(anticol(colour))
                        if Field.blackCheck:
                            Field.position[y1][x1] = Field.position[y2][x2]
                            Field.position[y2][x2] = store
                            print('Неверный ход: вам все еще объявлен шах')
                            colour = game.colourSwap()
                            print(Field.field(game))
                            continue
                        Field.position[y1][x1] = Field.position[y2][x2]
                        Field.position[y2][x2] = store
                    else:
                        if Field.position[y1][x1].itself()[:4] == 'Pawn':
                            if y1 == 1 and y2 == 0:
                                if not pawnTransformation:
                                    print('Неверный ход: укажите, в какую фигуру должна превратиться пешкаБ например:\n'
                                          'P - пешка, R - ладья, Kn - конь, B - слон, Q - ферзь\n'
                                          'Пример хода: E2 E1=Q')
                                    colour = game.colourSwap()
                                    print(Field.field(game))
                                    continue
                                else:
                                    Field.position[y1][x1].transform(x2, y2, pawnTransformation)
                                    print(Field.field(game))
                                    Field.gameCounter += 1
                                    Field.newGameRecord[
                                        Field.gameCounter] = f'{Field.gameCounter}- {chr(x1 + 65)}{y1 + 1} {chr(x2 + 65)}{y2 + 1}'
                                    continue
                    Field.gameCounter += 1
                    Field.newGameRecord[
                        Field.gameCounter] = f'{Field.gameCounter}- {chr(x1 + 65)}{y1 + 1} {chr(x2 + 65)}{y2 + 1}'
                    Field.position[y2][x2] = Field.position[y1][x1]
                    Field.position[y1][x1] = ''

                if chekmate(colour):
                    print(f'Шах и мат для {anticol(colour)}')
                    print(Field.field(game))
                    return True


        else:
            print('Неверный ход: вы не можете атаковать свои фигуры')
            colour = game.colourSwap()
        print(Field.field(game))


helpManual = 'записать игру - введите команду record to %filename%, эта команда запишет вашу игру в файл с заданным именем\n'              'начать игру - введите команду start game\n'              'посмотреть игру из файла  - введите start game with %filename%, и вы увидете игру из заданного файла\n'              'Для выхода введите exit'
while True:
    print('Введите одну из следующих комманд:')
    print('help')
    print('exit')
    print('start game')
    print('start game with %filename%')
    print('record to %filename%')
    s = input()
    if s == 'start game':
        gameStart()
    elif s[:15] == 'start game with':
        gameStart(s[16:])
    elif s == 'help':
        print(helpManual)
    elif s[:9] == 'record to':
        rec(s[10:])
    elif s == 'exit':
        exit()

# start game with chess_part.txt


# In[ ]:





# In[ ]:




