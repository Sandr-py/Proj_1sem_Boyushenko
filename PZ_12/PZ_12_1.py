# Реализовать прототип в IDE PyCharm Community с применением пакета tk. Получить интерфейс максимально
# приближенный к оригиналу.

from tkinter import *
from tkinter import ttk

special_list = ['Front-End', 'Back-End', 'Full-Stack']

root = Tk()
root.title("Анкета Web-Разработчика")
root.geometry('700x500')

label = Label(text = 'Анкета Web-Разработчика', font = ('Times New Roman', 20))
label.grid(row = 0, column = 0, sticky = N)
var = IntVar()





frame1 = LabelFrame(master=root, relief=RAISED, borderwidth=1)
frame1.grid(row=1, column=0, sticky=W+E+N+S)
frame2 = LabelFrame(master=root, relief=RAISED, borderwidth=1)
frame2.grid(row=1, column=1, sticky=W+E+N+S)
frame3 = LabelFrame(master=root, relief=RAISED, borderwidth=1)
frame3.grid(row=2, column=0, sticky=W+E+N+S)
frame4 = LabelFrame(master=root, relief=RAISED, borderwidth=1)
frame4.grid(row=2, column=1, sticky=N+S+W)
frame5 = LabelFrame(master=root, relief=RAISED, borderwidth=1)
frame5.grid(row=3, column=0, sticky=W+E+N+S)
frame6 = LabelFrame(master=root, relief=RAISED, borderwidth=1)
frame6.grid(row=3, column=1, sticky=W+E+N+S)
frame7 = LabelFrame(master=root, relief=RAISED, borderwidth=1)
frame7.grid(row=4, column=0, sticky=W+E+N+S)
frame8 = LabelFrame(master=root, relief=RAISED, borderwidth=1)
frame8.grid(row=4, column=1, sticky=W+E+N+S)
frame9 = LabelFrame(master=root, relief=RAISED, borderwidth=1)
frame9.grid(row=5, column=0, sticky=W+E+N+S)
frame10 = LabelFrame(master=root, relief=RAISED, borderwidth=1)
frame10.grid(row=5, column=1, sticky=W+E+N+S)
frame11 = LabelFrame(master=root, relief=RAISED, borderwidth=1)
frame11.grid(row=6, column=0, sticky=W+E+N+S)
frame12 = LabelFrame(master=root, relief=RAISED, borderwidth=1)
frame12.grid(row=6, column=1, sticky=W+E+N+S)



lable1 = Label(master=frame1, text='Регистрационное имя', font=('Times New Roman', 15))
lable1.grid(row=1, column=0, sticky=W+E)

name = Entry(master=frame2, width=40, relief=RAISED, borderwidth=1)
name.grid(row=1, column=1, sticky=W+E+N+S, pady=5, padx=5)

lable2 = Label(master= frame3,text = 'Пароль', font=('Times New Roman', 15))
lable2.grid(row=2, column=0, sticky=W+N+S+E)

password = Entry(master=frame4, width=40, relief=RAISED, borderwidth=1)
password.grid(row=3, column=1, sticky=W, padx=5)
double_password = Entry(master=frame4, width=40)
double_password.grid(rowspan=1, column=1, pady=5, padx=5, sticky=W)

lable_pass = Label(master=frame4, text=':Подтвердите пароль', font=('Times New Roman', 10))
lable_pass.grid(row=4, column=2, sticky=E)

spec_lable = Label(master= frame5,text = 'Ваша специализация', font=('Times New Roman', 15))
spec_lable.grid(row=3, column=0, sticky=W)

special = ttk.Combobox(values=special_list)
special.grid(row=3, column=1, sticky=W, padx=5)

gender_lab = Label(master= frame7,text = 'Пол', font=('Times New Roman', 15))
gender_lab.grid(row=4, column=0, sticky=W)

genderM = Radiobutton(frame8, text='М', variable=var, value='m')
genderF = Radiobutton(frame8, text='Ж', variable=var, value='f')

genderM.grid(row=4, column=1)
genderF.grid(row=4, column=2)

skills = Label(master= frame9,text = 'Ваши навыки', font=('Times New Roman', 15))
skills.grid(row=5, column=0, sticky=W)

skill_bar1 = Checkbutton(text='Знание HTML и CSS')
skill_bar1.grid(in_=frame10,  row=5, column=1, sticky=W, pady=1)
skill_bar2 = Checkbutton(text='Знание Perl')
skill_bar2.grid(in_=frame10, row=6, column=1, sticky=W, pady=1)
skill_bar3 = Checkbutton(text='Знание ASP')
skill_bar3.grid(in_=frame10, row=7, column=1, sticky=W, pady=1)
skill_bar4 = Checkbutton(text='Знание Adobe Photoshop')
skill_bar4.grid(in_=frame10, row=8, column=1, sticky=W, pady=1)
skill_bar5 = Checkbutton(text='Знание HTML и CSS')
skill_bar5.grid(in_=frame10, row=9, column=1, sticky=W, pady=1)
skill_bar6 = Checkbutton(text='Знание HTML и CSS')
skill_bar6.grid(in_=frame10, row=10, column=1, sticky=W, pady=1)
skill_bar7 = Checkbutton(text='Знание HTML и CSS')
skill_bar7.grid(in_=frame10, row=11, column=1, sticky=W, pady=1)
# Label(master=frame11, text = 'Дополнительные свдения о себе', font=('Times New Roman', 15)).grid(row=6, column=0, sticky=W)

root.mainloop()
