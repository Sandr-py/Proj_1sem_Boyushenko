# Дан список размера N. Найти номер его первого локального минимума (локальный
# минимум — это элемент, который меньше любого из своих соседей).

from random import randint

# Функция со сравнением следующего и предыдущего элемента относительно
# текущего в списке.

def min_lists_obj(lim):
    my_list = []
    for i in range(lim):
        a = randint(1, 100)
        my_list.append(a)
    for i in range(len(my_list)):
        if my_list[i] < my_list[i + 1] and my_list[i] < my_list[i - 1]:
            return my_list[i], my_list

# Вывод локального минимума и его идентификатора.
        
LocMin, AllList = min_lists_obj(int(input(f"Введите предел списка   ")))
print(f"Превый локальный минимум списка {AllList}: {LocMin}")
