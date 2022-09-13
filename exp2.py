# Задайте натуральное число N. Напишите программу, которая составит список простых множителей числа N.

import sympy

number = int(input('Введите число: '))
output = {0}
count = 1

output.clear()
while number > 1:
    if number / sympy.prime(count) != number // sympy.prime(count):
        count += 1
    else:
        output.add(sympy.prime(count))
        number /= sympy.prime(count)
        count = 1       
print(output)