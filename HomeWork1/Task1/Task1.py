'''Задача 2: Найдите сумму цифр трехзначного числа.
*Пример:*
123 -> 6 (1 + 2 + 3)
100 -> 1 (1 + 0 + 0) '''

# Решение через арифметические действия:
number = int(input('Введите трехзначное число: '))
if int(number / 1000) == 0 and int(number / 100) > 0:
    num1 = number % 10
    number = int(number / 10)
    num2 = number % 10
    num3 = int(number / 10)
    print(num1 + num2 + num3)
else:
    print('Число должно быть трехзначным!')

# Решение через срезы строки:
# text = str(input('Введите трехзначное число: '))
# if len(text) == 3 and text.isdigit() == True:
#     print(int(text[0]) + int(text[1]) + int(text[2]))
# else:
#     print('Число должно быть трехзначным!')