# Вычислить число c заданной точностью d

d = float(input('Введите точность: '))
number = float(input('Введите число: '))
count = 0

while d < 1:
    count += 1
    d *= 10
print(f'%.{count}f' % number)