# В квадратной матрице элементы на главной диагонали увеличить в 2 раза.
from random import randint

my_list = []

# Генерация квадратной матрицы.

for i in range(5):
    my_list.append(list(randint(-10, 10) for j in range(5)))

for i in my_list:
    print(*i)

for i in range(5):  # Умножение элементов главной диагонали на 2.
    my_list[i][i] *= 2
print(end='\n\n\n')

for i in my_list:
    print(*i)
