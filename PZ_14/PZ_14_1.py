# Из исходного текстового файла (hotline.txt) перенести в первый файл строки с
# корректными номерами телефонов (т.е. в номере должно быть 11 цифр, например,
# 86532547891), а во второй с некорректными номерами телефонов. Посчитать
# полученные строки в каждом файле.

import re

nums = []
mask_nums = []
right_num = []
ntrt_num = []

with open("hotline.txt", "r+", encoding="utf-8") as file:  # Чтение файла.
    string = file.read()
    print(string)

p = re.compile(r"[8].*[0-9]")  # Компилция шаблона.

num = p.findall(string)  # Нахождение элементов по шаблону
print(num)

for i in range(len(num)):  # Обходом списка вычитаем все лишние элементы номеров
    for j in num[i]:
        if not j.isdigit():
            new_i = num[i].replace(j, '')
            num[i] = new_i

print(num)

for i in num:  # С помощью проверки сортируем номера.
    if len(i) == 11:
        right_num.append(i)
    elif len(i) != 11:
        ntrt_num.append(i)

print(f"\n\nСписок правильных номеров: {right_num} \nСписок неправильных номеров: {ntrt_num}")  # Вывод.
