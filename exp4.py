# Задана натуральная степень k. Сформировать случайным образом список коэффициентов (значения от 0 до 100) многочлена и записать в файл многочлен степени k.

import random

# проверка на первое входжение
def addstring(f, s):
    if f:
        return s
    else:
        return ' + ' + s

degree = {'0':'⁰', '1':'¹', '2':'²', '3':'³', '4':'⁴', '5':'⁵', '6':'⁶', '7':'⁷', '8':'⁸', '9':'⁹'}
k = int(input('Введите степень: '))
start = True
output = f'При k = {k}: '
number = 0

while k >= 0:
    number = random.randint(0, 100)
    if (number > 1) & (k != 0):
        output += addstring(start, f'{str(number)}x')
        start = False
        for a in str(k):
            output += degree.get(a)
    elif (number == 1) & (k != 0):
        output += addstring(start, 'x')
        start = False
        for a in str(k):
            output += degree.get(a)
    elif (number != 0) & (k == 0):
        output += addstring(start, f'{str(number)} = 0')
    elif (number == 0) & (k == 0):
        output += ' = 0'
    k -= 1
print(output)