# Дан первый член A и разность D арифметической прогрессии. Сформировать и вывести
# список размера 10, содержащий 10 первых членов данной прогрессии: A, A + D, A +
# 2*D, A + 3*D, ... .

def ArifProg(num, diff):  # Функция, высчитывающая арифметическую прогрессию.
    counter = 0
    ListArif = []
    while counter != 10:
        summ = num + diff * counter
        ListArif.append(summ)
        counter += 1
    return ListArif

# Вывод с вызовом функции.

print(ArifProg(float(input(f"Введите первый член арифметической прогрессии:  ")), float(input(f"Введите разность:  "))))
