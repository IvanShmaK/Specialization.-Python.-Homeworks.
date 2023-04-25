"""Задача 26:  Напишите программу, которая на вход принимает два числа A и B, и возводит число А в целую степень B с помощью рекурсии.
*Пример:*
A = 3; B = 5 -> 243 (3⁵)
A = 2; B = 3 -> 8"""

number = int(input('Введите число, которое будем возводить в степень: '))
power_of_number = int(input('Введите степень, в которую будем возводить число: '))

def power(num: int, pow:int) -> int:
    if pow == 1:
        return num
    return num * power(num, pow - 1)

print(power(number, power_of_number))