"""Требуется вычислить, сколько раз встречается некоторое число X в массиве A[1..N]. 
Требуется найти в массиве A[1..N] самый близкий по величине элемент к заданному числу X."""

import random

size = int(input('Введите размер списка: '))
my_list = [random.randint(0, 100) for _ in range(size)]
num = int(input('Введите искомое число: '))
print(my_list)
count = 0

for i in range(size):
    if num == my_list[i]:
        count += 1

if count > 0:
    print(f'В данном списке число {num} встречается {count} раз')
else:
    difference = 0
    min_difference = abs(num - my_list[0])
    min_value = my_list[0]
    for i in range(size):
        difference = abs(num - my_list[i])
        if min_difference > difference:
            min_difference = difference
            min_value = my_list[i]
    print(f'В данном списке число {num} не встречается, самым близким к нему является число {min_value}')