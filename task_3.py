# Задайте последовательность чисел. Напишите программу, которая выведет список неповторяющихся элементов 
# исходной последовательности.

str = input('Задайте последовательность чисел: ')
list1 = str.split()
list2 = list()
for item in list1:
    if item not in list2:
        list2.append(item)
print('Список неповторяющихся элементов исходной последовательности: \n', list2)
