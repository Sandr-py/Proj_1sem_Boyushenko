# Размер скидки на продукты определен следующим образом: при покупке до 500 р. скидка
# составит 2%; при покупке от 500 р. до 1000 р. скидка составит 3%; при покупке от 1000 р.
# до 1500 р. скидка составит 4%; при покупке от 1500 р. до 2000 р. скидка составит 5%.
# Составить программу определяющую размер скидки в зависимости от потраченной суммы.
# Реализовать данную задачу приложением с применением библиотеки tkinter.


from tkinter import *
from tkinter import ttk


# Написание функции-обработчика: вывод полученных данных производится путём изменения скрытого текстового поля.

def disk_t():
    a = summa.get()
# Обработка исключений
# (возникла ошибка ввиду невозможности корректного прерывания функции в случае ввода неправильных данных)
# Решение данной проблемы будет представлено ниже.
    try:
        a = int(a)
    except ValueError:
        sale_label.configure(text='Некорректная форма записи', fg='red')
        accept_button.configure(command=disk_t)

    def sale(k, s):  # Составление функции для решения задачи.
        p = s / 100
        t = k * p
        sale_label.configure(text=f'Конечная стоимость: {k - t} рублей.', fg='black')
# Условием повторно проверяется правильность введённых данных, в противном случае в поле вывода выбивается ошибка.
    if type(a) != int:
        sale_label.configure(text=f'Некорректная форма записи', fg='red')

    elif a < 0:
        sale_label.configure(text=f'Число не должно быть отрицательным', fg='red')

    elif 0 <= a < 500:
        sale(a, 2)

    elif 500 <= a < 1000:
        sale(a, 3)

    elif 1000 <= a < 1500:
        sale(a, 4)

    elif 1500 <= a < 2000:
        sale(a, 5)

    else:
        sale(a, 10)


# Инициализация корневого окна приложения.

root = Tk()
root.title('Калькулятор скидки')
root.geometry('390x190')
root.configure(bg='#FFF8DC')

main_frame = LabelFrame(root, text='Калькулятор скидки', bd=5, bg='#FFF8DC')
main_frame.grid(pady=5, padx=5)

# Добавление подписи к полю ввода с указанием единиц измерения.

main_label = Label(master=main_frame, text='Введите стоимость покупки:', font=('Arial', 20), bg='#FFF8DC')
main_label.grid(row=0, columnspan=2, sticky=W + E, pady=5)

meas_system = Label(master=main_frame, text='Руб.', font=('Arial', 14), bg='#FFF8DC')
meas_system.grid(row=1, column=1, sticky=W)

# Добавление кнопки отправления данных в функцию-обработчик.

accept_button = Button(master=main_frame, text='Принять', font=('Arial', 10), command=disk_t, bg='#F4A460', bd=1,
                       relief=FLAT, activebackground="#8B4513")
accept_button.grid(row=2, columnspan=2, sticky=E + W, pady=7)

# Добавление поля ввода необходимых данных

summa = Entry(master=main_frame, width='20', font=('Arial', 14), bg='#FFDEAD')
summa.grid(row=1, column=0, sticky=E)

# Добавление изменяемого текстового поля-вывода.

sale_label = Label(main_frame, font=('Arial', 15), bg='#FFDEAD')
sale_label.grid(row=3, columnspan=2, sticky=E + W)

root.mainloop()
