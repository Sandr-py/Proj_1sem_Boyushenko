# Дано целое число N (>0). С помощью операций деления нацело и взятия остатка от деления
# определить, имеется ли в записи числа N цифра «2». Если имеется, то вывести TRUE, если
# нет — вывести FALSE.


n = input('Введите целое число n: ')

while type(n) != int:   # Обработка исключений
    try:
        n = int(n)
        if n <= 0:
            print('Вы ввели отрицательное число или 0. Попробуйте снова. . .')
            n = input('Введите целое число n: ')
            continue
    except ValueError:
        print('Вы ввели неверное значение. Попробуйте снова. . .')
        n = input('Введите целое число n: ')

p = 0   # Обозначение счётчика и необходимых параметров для вычислений.
t = len(str(n))
a = 10
b = 1
i = 0
while i != t:   # Поочерёдное нахождение разрядов числа.
    k = n % a
    k = k // b
    if int(k) == 2:
        p += 1
        k = 0
    a *= 10
    b *= 10
    i += 1
if int(p) >= 1:
    print(f'Число {n} содержит {p} раз цифру 2')
else:
    print(f'Число {n} не содержит {p} раз цифру 2')
