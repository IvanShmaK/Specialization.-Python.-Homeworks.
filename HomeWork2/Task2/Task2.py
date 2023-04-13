"""Задача 12: Петя и Катя – брат и сестра. Петя – студент, а Катя – школьница. Петя помогает Кате по математике. Он задумывает два натуральных числа X и Y (X,Y≤1000), 
а Катя должна их отгадать. Для этого Петя делает две подсказки. Он называет сумму этих чисел S и их произведение P. Помогите Кате отгадать задуманные Петей числа."""

summa_of_numbers = int(input('Введите сумму задуманных чисел (от 2 до 2000): '))
product_of_numbers = int(input('Введите произведение задуманных чисел (от 1 до 10000): '))

discriminant = int(summa_of_numbers ** 2 - 4 * product_of_numbers)
first_number = int((summa_of_numbers + discriminant ** 0.5) / 2)
second_number = int((summa_of_numbers - discriminant ** 0.5) / 2)
print(f'Первое число - {first_number}, второе число - {second_number}')
