# Реализовать прототип в IDE PyCharm Community с применением пакета tk. Получить интерфейс максимально
# приближенный к оригиналу.

from tkinter import *
from tkinter import ttk

special_list = ['Front-End', 'Back-End', 'Full-Stack']

root = Tk()
root.title("Анкета Web-Разработчика")
root.geometry('690x527')

label = Label(text = 'Анкета Web-Разработчика', font = ('Times New Roman', 20))
label.grid(row = 0, column = 0, sticky = N, pady=7)
var = IntVar()

frame1 = LabelFrame(master=root, relief=RAISED, borderwidth=1, background='#B0E0E6')
frame1.grid(row=1, column=0, sticky=W+E+N+S)
frame2 = LabelFrame(master=root, relief=RAISED, borderwidth=1, background='#C0C0C0')
frame2.grid(row=1, column=1, sticky=W+E+N+S)
frame3 = LabelFrame(master=root, relief=RAISED, borderwidth=1, background='#B0E0E6')
frame3.grid(row=2, column=0, sticky=W+E+N+S)
frame4 = LabelFrame(master=root, relief=RAISED, borderwidth=1, background='#C0C0C0')
frame4.grid(row=2, column=1, sticky=N+S+W)
frame5 = LabelFrame(master=root, relief=RAISED, borderwidth=1, background='#B0E0E6')
frame5.grid(row=3, column=0, sticky=W+E+N+S)
frame6 = LabelFrame(master=root, relief=RAISED, borderwidth=1, background='#C0C0C0')
frame6.grid(row=3, column=1, sticky=W+E+N+S)
frame7 = LabelFrame(master=root, relief=RAISED, borderwidth=1, background='#B0E0E6')
frame7.grid(row=4, column=0, sticky=W+E+N+S)
frame8 = LabelFrame(master=root, relief=RAISED, borderwidth=1, background='#C0C0C0')
frame8.grid(row=4, column=1, sticky=W+E+N+S)
frame9 = LabelFrame(master=root, relief=RAISED, borderwidth=1, background='#B0E0E6')
frame9.grid(row=5, column=0, sticky=W+E+N+S)
frame10 = LabelFrame(master=root, relief=RAISED, borderwidth=1, background='#C0C0C0')
frame10.grid(row=5, column=1, sticky=W+E+N+S)
frame11 = LabelFrame(master=root, relief=RAISED, borderwidth=1, background='#B0E0E6')
frame11.grid(row=6, column=0, sticky=W+E+N+S)
frame12 = LabelFrame(master=root, relief=RAISED, borderwidth=1, background='#C0C0C0')
frame12.grid(row=6, column=1, sticky=W+E+N+S)



lable1 = Label(master=frame1, text='Регистрационное имя', font=('Times New Roman', 15), background='#B0E0E6')
lable1.grid(row=1, column=0, sticky=W+E)

name = Entry(master=frame2, width=40, relief=RAISED, borderwidth=1, background='#C0C0C0')
name.grid(row=1, column=1, sticky=W+E+N+S, pady=5, padx=5)

lable2 = Label(master= frame3,text = 'Пароль', font=('Times New Roman', 15), background='#B0E0E6')
lable2.grid(row=2, column=0, sticky=W+N+S+E)

password = Entry(master=frame4, width=40, relief=RAISED, borderwidth=1, background='#C0C0C0')
password.grid(row=3, column=1, sticky=W, padx=5)
double_password = Entry(master=frame4, width=40, background='#C0C0C0')
double_password.grid(rowspan=1, column=1, pady=5, padx=5, sticky=W)

lable_pass = Label(master=frame4, text=':Подтвердите пароль', font=('Times New Roman', 10), background='#C0C0C0')
lable_pass.grid(row=4, column=2, sticky=E)

spec_lable = Label(master= frame5,text = 'Ваша специализация', font=('Times New Roman', 15), background='#B0E0E6')
spec_lable.grid(row=3, column=0, sticky=W)

special = ttk.Combobox(values=special_list, background='#C0C0C0')
special.grid(row=3, column=1, sticky=W, padx=5)

gender_lab = Label(master= frame7,text = 'Пол', font=('Times New Roman', 15), background='#B0E0E6')
gender_lab.grid(row=4, column=0, sticky=W)

genderM = Radiobutton(frame8, text='М', variable=var, value='m', background='#C0C0C0')
genderF = Radiobutton(frame8, text='Ж', variable=var, value='f', background='#C0C0C0')

genderM.grid(row=4, column=1)
genderF.grid(row=4, column=2)

skills = Label(master= frame9,text = 'Ваши навыки', font=('Times New Roman', 15), background='#B0E0E6')
skills.grid(row=5, column=0, sticky=W)

skill_bar1 = Checkbutton(text='Знание HTML и CSS', background='#C0C0C0')
skill_bar1.grid(in_=frame10, row=5, column=1, sticky=W, pady=1)
skill_bar2 = Checkbutton(text='Знание Perl', background='#C0C0C0')
skill_bar2.grid(in_=frame10, row=6, column=1, sticky=W, pady=1)
skill_bar3 = Checkbutton(text='Знание ASP', background='#C0C0C0')
skill_bar3.grid(in_=frame10, row=7, column=1, sticky=W, pady=1)
skill_bar4 = Checkbutton(text='Знание Adobe Photoshop', background='#C0C0C0')
skill_bar4.grid(in_=frame10, row=8, column=1, sticky=W, pady=1)
skill_bar5 = Checkbutton(text='Знание JAVA', background='#C0C0C0')
skill_bar5.grid(in_=frame10, row=9, column=1, sticky=W, pady=1)
skill_bar6 = Checkbutton(text='Знание JavaScript', background='#C0C0C0')
skill_bar6.grid(in_=frame10, row=10, column=1, sticky=W, pady=1)
skill_bar7 = Checkbutton(text='Знание Flash', background='#C0C0C0')
skill_bar7.grid(in_=frame10, row=11, column=1, sticky=W, pady=1)


more_info = Label(master=frame11, text='Дополнительные сведения о себе', font=('Times New Roman', 15), background='#B0E0E6')
more_info.grid(row=6, column=0, sticky=W)

inf_txt = Text(height=5, width=43, font=('Times New Roman', 12), wrap=WORD, background='#C0C0C0')
inf_txt.grid(pady=5, padx=5, row=6, column=1, sticky=W)

scroll = Scrollbar(command=inf_txt.yview, background='#C0C0C0')
scroll.grid(row=6, column=1, sticky=E+N+S, pady=5, padx=5)

inf_txt.config(yscrollcommand=scroll.set)

log_button = Button(text='Зарегистрировать')
clear_button = Button(text='Очистить форму')

log_button.grid(pady=7, row=7, column=0, sticky=W)
clear_button.grid(pady=7, row=7, column=0, sticky=E)

root.mainloop()
