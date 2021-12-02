# Дан список размера N (N — четное число). Поменять местами его первый элемент со
# вторым, третий — с четвертым и т. д.

from random import randint

def change_obj(lim):   # Создание функции, меняющей соседние элементы списка.
    my_list = []
    for i in range(lim):
        num = randint(1, 100)
        my_list.append(num)
    print(f"Первоначальный список: {my_list}")
    for i in range(0, len(my_list), 2):
        my_list[i], my_list[i + 1] = my_list[i + 1], my_list[i]
    return my_list

# Проверка на ввод чётного и положительного предела

a = int(input(f"Введите чётный предел списка: "))
while a % 2 != 0 or a < 0:
    print(f"Вы ввели нечётное или отрицательное число")
    a = int(input(f"Введите чётный пердел списка: "))

print(f"Конечный список: {change_obj(a)}") # Вывод с вызовом функции.
