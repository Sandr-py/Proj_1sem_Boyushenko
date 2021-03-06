# Книжные магазины предлагают следующие коллекции книг.
# Магистр – Лермонтов, Достоевский, Пушкин, Тютчев
# ДомКниги – Толстой, Грибоедов, Чехов, Пушкин.
# БукМаркет – Пушкин, Достоевский, Маяковский.
# Галерея – Чехов, Тютчев, Пушкин. Определить:
# 1. Полный список всех книг магазинов.
# 2. Какие книги есть во всех магазинах.
# 3. Хотя бы одну книгу, которая есть не во всех магазинах.

new_list = []   # Разбиваем строку на отдельные элементы типа (название: содержание) методом вложенных списков.
my_list = list("Магистр – Лермонтов, Достоевский, Пушкин, Тютчев. ДомКниги – Толстой, Грибоедов, Чехов, Пушкин."
               " БукМаркет – Пушкин, Достоевский, Маяковский. Галерея – Чехов, Тютчев, Пушкин".split('. '))
print(f"\033[3m{my_list}\033[0m")

for i in my_list:   # Вывод данного списка.
    new_list.append(i.split(" – "))
print(f"\033[3m{new_list}\033[0m", end='\n_______________________________________\n\n')
magistr = set(new_list[0][1].split(', '))
DomKnig = set(new_list[1][1].split(', '))
BookMarket = set(new_list[2][1].split(', '))
Galereya = set(new_list[3][1].split(', '))
print(f"Ассортимент \033[33m'Магистра': \033[31m{magistr}\033[0m\n"   # Ассоритменты магазинов.
      f"{' '* len('Ассортимент')} \033[33m'ДомКниги': \033[31m{DomKnig}\033[0m\n"
      f"{' '* len('Ассортимент')} \033[33m'БукМаркета': \033[31m{BookMarket}\033[0m\n"
      f"{' '* len('Ассортимент')} \033[33m'Галереи': \033[31m{Galereya}\033[0m\n")

# Вывод общих и необщих элемнтов.

print(f"Во всех магазинах есть следующие книги: \033[36m{''.join(magistr.intersection(DomKnig, BookMarket, Galereya))}\033[0m\n "
      f"Не во всех маганзинах есть следующие книги: "
      f"\033[36m{' // '.join((magistr.union(DomKnig, BookMarket, Galereya)).difference(magistr.intersection(DomKnig, BookMarket, Galereya)))}\033[0m")