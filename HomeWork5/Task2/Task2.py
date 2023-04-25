"""Задача 28: Напишите рекурсивную функцию sum(a, b), возвращающую сумму двух целых неотрицательных чисел. Из всех арифметических операций допускаются только +1 и -1. 
Также нельзя использовать циклы.
*Пример:*
2 2       4"""

number_1 = int(input('Введите первое целое число: '))
number_2 = int(input('Введите второе целое число: '))

def summa(num_1: int, num_2:int) -> int:
    if num_2 == 0:
        return num_1
    num_1 += 1
    return summa(num_1, num_2 - 1)

if number_2 >= 0:
    print(summa(number_1, number_2))
elif number_1 >= 0:
    print(summa(number_2, number_1))
else:
    print('Хотя бы одно число должно быть неотрицательным!')