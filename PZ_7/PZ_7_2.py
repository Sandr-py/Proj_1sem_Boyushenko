# Дана строка, содержащая цифры и строчные латинские буквы. Если буквы в строке
# упорядочены по алфавиту, то вывести 0; в противном случае вывести номер первого
# символа строки, нарушающего алфавитный порядок.
p = list(input(f"Введите какую-либо строку: "))
str_list = []
print(p)

for i in p:
    if i.isalpha():
       str_list.append(i)

print(str_list)
k = 0

reserve = ' '

for i in str_list:
    if ord(i) < ord(reserve):
        print(f"{str_list.index(i)}-й элемент строки ({i}) нарушает алфавитную последовательность")
        k += 1
        break
    else:
        reserve = i
if k != 1:
    print("Строка отстортирована в правильном порядке")
