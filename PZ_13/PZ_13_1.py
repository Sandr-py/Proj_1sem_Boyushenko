# Организовать и вывести последовательность из N случайных целых чисел. Из
# исходной последовательности организовать первую последовательность, содержащую
# числа кратные трем, и вторую – для всех остальных. Найти количество элементов в
# полученных последовательностях.


from random import randint

my_list = [randint(-999, 999) for i in range(int(input(f"Введите предел последовательности: ")))]
print('Изначальная последовательность: ', *my_list)   # Генерация списка из случайных чисел.

# Генерация новых списков на основе главного с проверкой на кратность.

eq_list = list(filter(lambda n: n % 2 == 0, my_list))
nteq_list = list(filter(lambda m: m % 3 == 0, my_list))

print(f"Числа, кратные двум:", *eq_list)   # Вывод результата.

print(f"Числа, кратные трём:", *nteq_list)
