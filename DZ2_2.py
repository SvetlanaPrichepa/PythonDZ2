#Напишите программу, которая принимает на вход число N и выдает набор произведений
# чисел от 1 до N.
# Пример:
# - пусть N = 4, тогда [ 1, 2, 6, 24 ] (1, 1*2, 1*2*3, 1*2*3*4)

input_n = int(input('Введите число: '))
list = [1]

for i in range (1,input_n):
    list.append ((i+1) * list [i-1])

print(list)