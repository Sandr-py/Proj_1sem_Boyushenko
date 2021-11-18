# Составить функцию, которая выполнит суммирования числового ряда.
def exception(a):   # Функция обработки исключения.
    while type(a) != int:
        try:
            a = int(a)
        except ValueError:
            print(f"{a} не может быть числом, попробуйте снова...")
            a = input('Введите число: ')
    return a


def summari():   # Главная функция  с интеграцией обработки исключений и проведением рассчётов.
    stopWord = 'fill'
    summ = 0
    while stopWord != '1':
        num = input('Введите число: ')
        num = exception(num)
        summ += num
        stopWord = input("Если не хотите вводить больше, пропишите (1), иначе нажмите (Enter):   ")
    return summ   # Возврат суммы.
print(f"\n Сумма числового ряда равна {summari()}")
