# Задайте натуральное число N. Напишите программу, которая составит список простых делителей числа N. (1 - составное число)

num = int(input('Задайте натуральное число: '))
simple_div = list()
for i in range(2, num + 1):
    if num % i == 0:
        simple_div.append(i)
    while num % i == 0:
        num = num / i
print('Список простых делителей числа: \n', simple_div)
