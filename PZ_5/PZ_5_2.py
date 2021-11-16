# Описать функцию TrianglePS(параметры), вычисляющую по стороне a равностороннего
# треугольника его периметр P = 3*a и площадь S = a2 √3/4. С помощью этой функции найти
# периметры и площади трех равносторонних треугольников с данными сторонами.
import math


def exception():  # Функция обработки исключения.
    a = input(f"Введите сторону треугольника: ")
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
    p = 3 * side
    s = side ** 2 * (math.sqrt(3) / 4)

    return p, s


perim1, plosh1 = trianglePS(exception())
perim2, plosh2 = trianglePS(exception())
perim3, plosh3 = trianglePS(exception())

print(f"периметр первого треугольника = {perim1};  Площадь первого треугольника = {round(plosh1, 1)}")
print(f"периметр второго треугольника = {perim2};  Площадь второго треугольника = {round(plosh2, 1)}")
print(f"периметр третьего треугольника = {perim3};  Площадь третьего треугольника = {round(plosh3, 1)}")

