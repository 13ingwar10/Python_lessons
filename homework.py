print("Задача 1. Вычислить число c заданной точностью d")

import random

d = 1*10**(-1*random.randint(1, 11))

counter = 0

while (d < 1):
    d = d*10
    counter += 1

print(f"Будет сгенерировано число с точность {counter} знаков после запятой")

floor = float(input("Укажите нижню границу:  "))
top = float(input("Укажите верхнюю границу:  "))

while (top <= floor):
    top = float(input(f"Ошибка! Укажите верхнюю границу выше {floor}:  "))

number = random.uniform(floor, top)
print(round(number, counter))
print("\n")

print("Задача 2. Задайте натуральное число N. Напишите программу, которая составит список простых множителей числа N.")

number = int(input("Введите число: "))
simple_numbers = [2, 3, 5, 7]
factors = []

print(f"Список простых множителей для числа {number}:")

for i in range(len(simple_numbers)-1):
    while (number%int(simple_numbers[i]) == 0):
        factors.append(simple_numbers[i])
        number = number / simple_numbers[i]
if (number != 1):
    factors.append(int(number))

print(factors)
print("\n")

print("Задача 3. Задайте последовательность чисел. Напишите программу, которая выведет список неповторяющихся элементов исходной последовательности.")

size = int(input("Введите количество элементов последовательности: "))
order = []
result = []
import random

for i in range(size - 1):
    order.append(random.randint(1, 10))
    if (order[i] not in result):
        result.append(order[i])
print("Выводим исходный список")
print(order)

print("Вариант 1) Формируется список, очищенный от дублей")
print(result)

print("Вариант 2) Формируется список элементов, которые в исходном массиве ни разу не повторяются")

result = []
counter = 0

for i in range(size - 1):
    counter = 0
    for g in range(size - 1):
        if (order[i] == order[g]):
            counter +=1
    if (counter < 2):
        result.append(order[i])

print(result) 

print("Задача 4. Задана натуральная степень k. Сформировать случайным образом список коэффициентов (значения от 0 до 100) многочлена и записать в файл многочлен степени k.")

k = int(input("Введите степень k (не больше 10): "))

while (k < 0 or k > 10):
    k = int(input("Ошибка! Введите число от 0 до 10 (включительно): "))

coefficients = []

import random

for i in range(k+1):
    coefficients.append(random.randint(1, 100))

print("Сформирован список коэффициентов")
print(coefficients)

with open("file.txt", "w") as file:
    for i in range(k, 0, -1):
        file.write(str(coefficients[k - i]) + "x^" + str(k - (k - i)) + " + ")
    file.write(str(coefficients[k]))
