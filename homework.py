print("Задача 1. Напишите программу, которая принимает на вход вещественное число и показывает сумму его цифр.")
number = str(input("Введите любое вещественное число: "))

number = number.replace('.', '')
sum = 0

for i in range(len(number)):
    sum += int(number[i])

print(sum)
print("\n")

print("Задача 2. Напишите программу, которая принимает на вход число N и выдает набор произведений чисел от 1 до N.")
number = int(input("Введите число N: "))
array = []
array.append(1)

for i in range(1, number):
    array.append((i+1)*array[i-1])
print(array)

print("\n")

print("Задача 3. Задайте список из n чисел последовательности (1 + 1/n)**n и выведите на экран их сумму.")

number = int(input("Введите число N: "))
array = []
sum = 0

print(f"Для n = {number} сформирована последовательность:", end=" ")
for i in range(number-1):
    array.append((1 + 1 / (i+1)) ** (i + 1))
    print(f"{i+1}: {round(array[i],2)}", end=", ")
    sum += array[i]
array.append((1 + 1/number)**number)
print(f"{number}: {round(array[number-1],2)}")
sum += array[number-1]
print(f"Сумма элементов равна {round(sum, 2)}")

print("\n")

print("Задача 4. Задайте список из N элементов, заполненных числами из промежутка [-N, N]. Найдите произведение элементов на указанных позициях. Позиции хранятся в файле file.txt в одной строке одно число.")

import random
number = int(input("Введите число N: "))
array = []

for i in range(number): # создаем список длинной N, заполненный числами из промежутка [-N, N]
    array.append(random.randint(-number, number))

print("Был сформирован массив: ", end='')
print(array)

array_for_write = [] # создаем список из двух случайных неодинаковых чисел, которые буду записаны в файл file.txt как позиции списка array для нахождения произведения
array_for_write.append(random.randint(0, number-1))
array_for_write.append(random.randint(0, number-1))
while (array_for_write[0] == array_for_write[1]):
    array_for_write[1] = random.randint(0, number-1)

print("Найдем произведение следующих позиций: ", end= '')
print(f"{array_for_write[0]+1} и {array_for_write[1]+1}")

with open("file.txt", "w+") as new_file: # записываем в отдельный файл позиции элементов списка array для перемножения
    for i in array_for_write:
        new_file.write(str(i) + '\n')

product = 0
with open("file.txt", 'r') as new_file: # достаем из файла file позиции элементов для перемножения, и записываем произведение в переменную product
    lines = new_file.readlines()
    product = array[int(lines[0])]*array[int(lines[1])]

print(f"Произведение данных элементов равно {product}")

print("\n")

print("Задача 5. Реализуйте алгоритм перемешивания списка")

number = int(input("Введите размер списка: "))

array = []
for i in range(number): # создаем список длинной number, заполненный случайными числами из промежутка [-10, 10]
    array.append(random.randint(-10, 10))

print("Был такой список: ", end='')
print(array)

temp = 0
position = 0

for i in range(number):
    temp = array[i]
    position = random.randint(0, number-1)
    array[i] = array[position]
    array[position] = temp

print("А получился такой: ", end='')
print(array)

print("\n")

print("Задача 6. Даны два массива, необходимо вернуть их пересечение")

# чтобы было веселее, сформируем массивы рандомно

size_first = int(input("Введите размер первого массива: "))
size_second = int(input("Введите размер второго массива: "))

array_first = []
array_second = []

for i in range(size_first): # заполним два массива случайными числами из промежутка [-10, 10]
     array_first.append(random.randint(-10, 10))
for i in range(size_second): 
     array_second.append(random.randint(-10, 10))

print("Первый массив: ", end='')
print(array_first)

print("Второй массив: ", end='')
print(array_second)

array_cross = []

for i in range(size_first): # заполним массив array_cross пересечениями из первых двух массивов
    for g in range(size_second):
        if (array_first[i] == array_second[g]):
            array_cross.append(array_first[i])

array_without_doubles = [] 

for i in range(len(array_cross)): # запишем итоговый массив array_without_doubles, очищенный от дублей
    if array_cross[i] not in array_without_doubles:
        array_without_doubles.append(array_cross[i])

print("Получились следующие пересечения: ", end='')
print(array_without_doubles)