# Средствами языка Python сформировать текстовый файл (.txt), содержащий
# последовательность из целых положительных и отрицательных чисел. Сформировать
# новый текстовый файл (.txt) следующего вида, предварительно выполнив требуемую
# обработку элементов:
# Исходные данные:
# Количество элементов:
# Минимальный элемент:
# Квадраты четных элементов:
# Сумма квадратов четных элементов:
# Среднее арифметическое суммы квадратов четных элементов:

from random import randint

my_list = []   # Заполняем сприсок рандомным количеством рандомных чисел.
for i in range(randint(10, 25)):
    my_list.append(str(randint(-100, 100)))

print(my_list)

with open("file.txt", "w+") as new_file:   # Создаём файл, в который поместим список.
    new_file.writelines(' '.join(my_list))
    new_file.close()

new_file = open("file.txt", "r+")   # Считываем сам список из этого файла.
list_1 = new_file.read().split(' ')
print(list_1)
new_file.close()

# создаём новый файл, в который заносим "Входные данные", "Количество элементов", "Минимальный элемент",
# "Квадраты чётных элементов" и их сумму.

with open("file.txt", "r+") as new_file:
    with open("main.txt", "w+") as main_file:
        main_file.writelines(f"Initial Data:  \n"
                             f"{' '.join(list_1)}\n\n"
                             f"Data's size: \n"
                             f"{str(len(new_file.read()))}\n\n"
                             f"Minimal element:  \n"
                             f"{str(min(int(i) for i in list_1))}\n\n"
                             f"Square of even elements:  \n"
                             f"{' '.join(str(int(i)**2) for i in list_1 if int(i) % 2 == 0)}\n\n"
                             f"Sum square of even elements: \n"
                             f"{str(sum(int(i) ** 2 for i in list_1 if int(i) % 2 == 0))}\n\n")



