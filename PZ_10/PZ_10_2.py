# Из предложенного текстового файла (text18-3.txt) вывести на экран его содержимое,
# количество знаков пунктуации в первых четырёх строках. Сформировать новый файл, в
# который поместить текст в стихотворной форме предварительно заменив символы третей
# строки их числовыми кодами.

from string import punctuation

p = 0


with open("text18-3.txt", "r", encoding="utf-8") as my_file:
    text = my_file.readlines()
    print("".join(text))

for i in text[0:4]:
    k = list(i)
    for j in k:
        if j in punctuation:
            p += 1

print(f"Колличество знаков пунктуации: {p}")
with open("text18-3.txt", "r", encoding="utf-8") as my_file:
    with open("new_file.txt", "w", encoding="utf-8") as new_file:

        text2 = [str(ord(str(i))) for i in text[2]]
        print(*text2)
        for line in range(len(text)):
            if line == 2:
                new_file.writelines(' '.join(str(j) for j in text2))
                print(file=new_file)
            else:
                new_file.write(text[line])

