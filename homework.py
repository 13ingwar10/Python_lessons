# print("Задача 1. Напишите программу, удаляющую из текста все слова, содержащие 'абв'")

# text_start = input("Введите строку: ")
# text_start = text_start.split()

# text_end = []

# for i in text_start:
#     if ('абв' not in i):
#         text_end.append(i)

# print(*text_end)
# print("\n")

print("Задача 2. Реализуйте RLE алгоритм: реализуйте модуль сжатия и восстановления данных.")

text = input("Введите строку для кодирования в формате RLE: ")

counter = 1
encoded_text = ''
prev_symbol = ''

for i in range(len(text)):
    counter = 0
    if text[i] != prev_symbol:
        for j in range(i, len(text)):
            if (text[i] == text[j]):
                counter += 1
            else: break 
        if counter > 0:
            encoded_text += (str(counter) + text[i])
            prev_symbol = text[i]

print(encoded_text)

text = input("Введите строку в формате RLE для декодирования в исходный формат: ")

counter = 0

for i in range(len(text) - 1):
    if (text[i].isdigit()):
        counter = int(text[i])
        for j in range(counter, 0, -1):
            print(text[i + 1], end='')

print("\n")
