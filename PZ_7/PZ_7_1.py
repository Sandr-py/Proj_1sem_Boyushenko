# Дан символ C. Вывести два символа, первый из которых предшествует символу C в
# кодовой таблице, а второй следует за символом C.
a = input("Введите любой символ с клавиатуры:   ")   # Проверка на то, чтобы был введён только 1 символ.
while int(len(a)) > 1:
    if int(len(a)) > 1:
        print(f"Вы должны ввести только один символ. . . ")
        a = input("Введите любой символ с клавиатуры:   ")

first_num = chr(ord(a)-1)   # Нахождение последующего и предыдущего символа.
second_num = chr(ord(a)+1)
print(f"Предыдущий от \033[1m'{a}'\033[0m символ: \033[1m'{first_num}'\033[0m,Последующий:"
      f" \033[1m'{second_num}'\033[0m")