# Задайте последовательность чисел. Напишите программу, которая выведет список неповторяющихся элементов исходной последовательности.

number = int(input('Введите размерность: '))
inputList = []

for i in range(number):
    inputList.append(float(input(f'{i + 1}: ')))

output = {0}
output.clear()
for i in range(number):
    output.add(inputList[i])
print(output)