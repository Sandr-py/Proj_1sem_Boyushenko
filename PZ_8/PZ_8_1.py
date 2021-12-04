# Дана строка 'апельсины 45 991 63 100 12 яблоки 13 47 26 0 16',
# отражающая продажи продукции по дням в кг. Преобразовать информацию из
# строки в словари, с использованием функции найти максимальные продажи по
# каждому виду продукции, результаты вывести на экран.

index_alpha = []
future_keys = []
dictionary = {}   # Создаём 2 списка id-значение для названий товаров и пустой словарь.
print(f"Введите название товара во мн.числе и колличество проданных килограм по дням через пробел:"
      f" <Пример> \n апельсины 5 16 25 40 яблоки 59 45 30 5")
my_list = list(input(':   ').split(' '))   # Разбиваем введённую строку на отдельные слова и значения.
print(my_list)
for i in my_list:
    if i.isalpha():
        index_alpha.append(my_list.index(i))
        future_keys.append(i)
for i in range(len(index_alpha)):
    print(f"\033[33m{index_alpha[i]} : {future_keys[i]}\033[0m")   # добавление в списки id и его значения

for i in range(len(index_alpha)):   # добавление в словарь ключа-названия товара и список проданных товаров срезом.
    if index_alpha[i] == index_alpha[-1]:
        dictionary[future_keys[i]] = [int(my_list[j]) for j in range(index_alpha[i]+1, len(my_list))]
    else:
        dictionary[future_keys[i]] = [int(my_list[p]) for p in range(index_alpha[i]+1, index_alpha[i+1])]

for key, value in dictionary.items():   # Вывод словаря для проверки
    print(f"{key} : {value} \n")

# Вывод максимального значения каждого списка и его id в списке + 1 (день продажи.)

for key, value in dictionary.items():
    print(f"{key} продались лучше всего в\033[1m\033[31m {value.index(max(value)) + 1}-й\033[0m день,"
          f" а именно \033[1m\033[31m{max(value)}\033[0m\n")
