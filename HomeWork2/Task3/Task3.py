"""Задача 14: Требуется вывести все целые степени двойки (т.е. числа вида 2k), не превосходящие числа N."""

number = int(input('Введите число-предел: '))
final_number = 2
while final_number < number:
    print(final_number, end=' ')
    final_number = final_number * 2
    
