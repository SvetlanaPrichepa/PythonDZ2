# Напишите программу, которая принимает на вход вещественное число и
# показывает сумму его цифр.
# Пример:
#  - 6782 -> 23
#  - 0,56 -> 11

n = input('Введите число ')

def summa(x):
    if float(n) < 0:
        x = float(n) * (-1)
    number = 0

    for i in str(n):
        if i != '.':
            number += int(i)
    return number


print(f'Сумма равна {summa(n)}')
