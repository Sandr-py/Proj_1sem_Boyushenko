# Описать функцию TrianglePS(параметры), вычисляющую по стороне a равностороннего
# треугольника его периметр P = 3*a и площадь S = a2 √3/4. С помощью этой функции найти
# периметры и площади трех равносторонних треугольников с данными сторонами.
import math


def exception():   # Функция обработки исключения.
    a = input(f"Введите сторону треугольника")
    while type(a) != int:
        try:
            a = int(a)
            if a < 0:
                print(f'{a} отрицательно число, введите положительное целое число. . . ')
                a = input('Введите число: ')
        except ValueError:
            print(f"{a} не может быть числом, попробуйте снова...")
            a = input('Введите число: ')
    return a



def trianglePS(side):
    p= 3*side
    s = side * 2 * math.sqrt(3) / 4

    return p, s


side1 = exception()
side2 = exception()
side3 = exception()

print(f"периметр первого треугольника = {exception(side1)};  Площадь первого треугольника = {}")
print(f"")
print(f"")