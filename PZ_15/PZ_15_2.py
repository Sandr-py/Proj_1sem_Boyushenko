# Из матрицы сформировать массив из положительных четных элементов, найти их
# сумму и среднее арифметическое.


from random import randint

# Генерация матрицы.

a = randint(3, 7)
my_list = [[randint(-10, 10) for j in range(a)] for i in range(randint(3, 7))]

new_list = []

for i in my_list:  # Вывод матрицы.
    print(f"{i}")

for i in my_list:  # Обход элементов матрицы.
    for j in i:
        if j > 0 and j % 2 == 0:
            new_list.append(j)

# Вывод результата.

print(f"Массив: {new_list}\n\nСумма элементов: {sum(new_list)}\n\nСреднее арифметическое: "
      f"{round(sum(new_list) / len(new_list), 2)}")
