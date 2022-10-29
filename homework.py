print("Задача 1. Задайте список из нескольких чисел. Напишите программу, которая найдёт сумму элементов списка, стоящих на нечётной позиции.")

size = int(input("Задайте размер массива: ")) # Формируем рандомный список, размер задает пользователь
import random
array = []

for i in range(size):
    array.append(random.randint(0, 99))

print("Сформирован список:")
print(array)

sum = 0

for i in range(1, size, 2): # Пробегаемся по нечетным позиция начиная с 1, значения записываем в sum накопленной суммой
    sum += array[i]

print(f"Сумма элементов нечетных позиций равна {sum}")
print("\n")

print("Задача 2. Напишите программу, которая найдёт произведение пар чисел списка. Парой считаем первый и последний элемент, второй и предпоследний и т.д.")

size = int(input("Задайте размер массива: ")) # Формируем рандомный список, размер задает пользователь
import random
array = []

for i in range(size):
    array.append(random.randint(0, 10))

print("Сфоромирован список:")
print(array)

start = 0
end = size - 1
result = []

while (start <= end):                           # Перемножаем элементы на позициях start и end, двигая их навстречу друг другу при каждом проходе цикла. 
    result.append(array[start] * array[end])    # Из полученных произведений формируем список result
    start += 1
    end -= 1

print("Выводим произведения крайних элементов:")
print(result)
print("\n")

print("Задача 3. Задайте список из вещественных чисел. Напишите программу, которая найдёт разницу между максимальным и минимальным значением дробной части элементов.")

size = int(input("Задайте размер массива: ")) # Формируем рандомный список вещественных чисел. Размер задает пользователь
import random
array = []

for i in range(size):
    array.append(round(0.1 + random.random()*10, 2))

print(array)

max = 0
min = 0

for i in range(1, size):                 # Проходим по циклу и записываем в переменные max и min наибольшую и наименьшую дробные части элементов списка
    if (array[max] % 1 < array[i] % 1):
        max = i
    elif (array[min] % 1 > array[i] % 1):
        min = i
 
result = array[max]%1 - array[min]%1     # Записываем в переменную result разницу между дробными частями элементов под индексами max и min
print (round(result, 2))

print("Задача 4. Напишите программу, которая будет преобразовывать десятичное число в двоичное.")

number = int(input("Введите десятичное число: ")) # Пользователь вводит двоичное число, записываем в number
array = []

while (number > 0):                               # Фомируем массив из остатков от деления number на 2
    array.append(number % 2)
    number = int(number / 2)

start = 0
end = len(array) - 1
temp = 0

for i in range(int(len(array) / 2)):              # Поскольку двоичное число собирается "с хвоста", переворачиваем список
    temp = array[start]
    array[i] = array[end]
    array[end] = temp
    start += 1
    end -= 1

print(*array)                                     # Выводим ответ, печатая список result в распакованном виде
print("\n")

print("Задача 5. Задайте число. Составьте список чисел Фибоначчи, в том числе для отрицательных индексов.")

number = int(input("Введите количество элементов последовательности Фибоначчи: "))  # Пользователь задает число, до которого строится последовательность Фибоначчи
array_positiv = [0, 1]           # Создаем вспомогательные списки. array_positiv стремится вправо от нуля, array_negativ стремится влево от нуля, в array_resul запишем ответ
array_negativ = [0, 1]
array_result = []

for i in range (2, number + 1):  # Для n элементов длинна последовательности Фибоначчи всегда будет равна n + 1, элементы под номерами 0 и 1 заполнены по умолчанию, начинаем со второго
    array_positiv.append(array_positiv[i - 2] + array_positiv[i - 1])
    array_negativ.append(array_negativ[i - 2] - array_negativ[i - 1])

index = len(array_negativ) - 1                 # Собираем ответ в список array_result, с помощью index будем двигаться по спискам за два цикла
while (index > 0):
    array_result.append(array_negativ[index])
    index -= 1

index = 0

while (index < len(array_positiv)):
    array_result.append(array_positiv[index])
    index += 1

print(array_result)
print("\n")