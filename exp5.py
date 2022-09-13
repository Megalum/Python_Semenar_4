# Даны два файла, в каждом из которых находится запись многочлена. Задача - сформировать файл, содержащий сумму многочленов.

# Подсчет повторяющихся элементов многочлена
def calc(string = '', numbers = 0):
    numberStr = ''
    const = 1
    if (string[0] == '+') & (string[1] != 'x'):
        while (string[const] != 'x'):
            numberStr += string[const]
            const += 1
            if (const == len(string)):
                break
        numbers += int(numberStr)
    elif (string[0] == '+') & (string[1] == 'x'):
        numbers += 1
    elif (string[0] == '-') & (string[1] != 'x'):
        while (string[const] != 'x'):
            numberStr += string[const]
            const += 1
            if (const == len(string)):
                break
        numbers -= int(numberStr)
    elif (string[0] == '-') & (string[1] == 'x'):
        numbers -= 1
    return numbers

# Перенос из файлов в строку
fileFirst = open('file1.txt', 'r')
fileSecond = open('file2.txt', 'r')
line = '+'
for l in fileFirst:
    line += l
line += ' '
for l in fileSecond:
    line += l
fileFirst.close()
fileSecond.close()

# Данные для сложения
listElements = line.split()
elements = ['xВі', 'xВІ', 'x', ' ']
output = ''
start = True

# Формирование ответа
for i in range(4):
    j = 0
    number = 0    
    while (j < len(listElements)):
        if i != 3:
            if set(elements[i]).issubset(listElements[j]):
                number = calc(listElements[j], number)   
                listElements.remove(listElements[j])
            else:
                j += 1        
        else:
            number = calc(listElements[j], number)    
            listElements.remove(listElements[j]) 
    if (number > 0):
        if (start):
            output += str(number) + elements[i]
            start = False
        else:
            output += ' +' + str(number) + elements[i]
    else: 
        if (start):
            output += str(number) + elements[i]
            start = False  
        else:
            output += ' ' + str(number) + elements[i]
print(output)

# Вывод в файл
o = open('file3.txt', 'w')
o.writelines(output)
o.close()
