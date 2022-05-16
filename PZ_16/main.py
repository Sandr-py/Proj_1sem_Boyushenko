import tkinter as tk
from tkinter import ttk
import sqlite3 as sq

from tkcalendar import DateEntry


class Main(tk.Frame):
    """Класс для главного окна"""

    def __init__(self, root):
        super().__init__(root)
        self.init_main()
        self.db = db
        self.view_records()

    def init_main(self):
        toolbar = tk.Frame(bg='#a0dea0', bd=4)
        toolbar.pack(side=tk.TOP, fill=tk.X)

        self.add_img = tk.PhotoImage(file="img/add.gif")
        self.btn_open_dialog = tk.Button(toolbar, text='Добавить игрока', command=self.open_dialog, bg='#5da130', bd=0,
                                         compound=tk.TOP, image=self.add_img)
        self.btn_open_dialog.pack(side=tk.LEFT)

        self.edit_img = tk.PhotoImage(file="img/edit.gif")
        btn_edit_dialog = tk.Button(toolbar, text="Редактировать", command=self.open_update_dialog, bg='#5da130',
                                    bd=0, compound=tk.TOP, image=self.edit_img)
        btn_edit_dialog.pack(side=tk.LEFT)

        self.delete_img = tk.PhotoImage(file="img/delete.gif")
        btn_delete = tk.Button(toolbar, text="Удалить запись", command=self.delete_records, bg='#5da130',
                               bd=0, compound=tk.TOP, image=self.delete_img)
        btn_delete.pack(side=tk.LEFT)

        self.search_img = tk.PhotoImage(file="img/search.gif")
        btn_search = tk.Button(toolbar, text="Поиск записи", command=self.open_search_dialog, bg='#5da130',
                               bd=0, compound=tk.TOP, image=self.search_img)
        btn_search.pack(side=tk.LEFT)

        self.refresh_img = tk.PhotoImage(file="img/update.gif")
        btn_refresh = tk.Button(toolbar, text="Обновить экран", command=self.view_records, bg='#5da130',
                                bd=0, compound=tk.TOP, image=self.refresh_img)
        btn_refresh.pack(side=tk.LEFT)

        self.tree = ttk.Treeview(self, columns=(
            'user_id', 'name', 'date_of_birth', 'post', 'science_degree', 'burden', 'wages'), height=15,
                                 show='headings')

        self.tree.column('user_id', width=50, anchor=tk.CENTER)
        self.tree.column('name', width=180, anchor=tk.CENTER)
        self.tree.column('date_of_birth', width=140, anchor=tk.CENTER)
        self.tree.column('post', width=140, anchor=tk.CENTER)
        self.tree.column('science_degree', width=140, anchor=tk.CENTER)
        self.tree.column('burden', width=140, anchor=tk.CENTER)
        self.tree.column('wages', width=140, anchor=tk.CENTER)

        self.tree.heading('user_id', text='ID')
        self.tree.heading('name', text='ФИО')
        self.tree.heading('date_of_birth', text='Дата рождения')
        self.tree.heading('post', text='Должность')
        self.tree.heading('science_degree', text='Ученая степень')
        self.tree.heading('burden', text='Нагрузка (ч/нед)')
        self.tree.heading('wages', text='Зарплата (руб.)')

        self.tree.pack()

    def records(self, user_id, name, dob, post, sd, burden, sall):
        self.db.insert_data(user_id, name, dob, post, sd, burden, sall)
        self.view_records()

    def update_record(self, user_id, name, dob, post, sd, burden, sall):
        self.db.cur.execute(
            """UPDATE users SET user_id=?, name=?, date_of_birth=?, post=?, science_degree=?, burden=?, wages=? WHERE user_id=?""",
            (user_id, name, dob, post, sd, burden, sall, self.tree.set(self.tree.selection()[0], '#1')))
        self.db.con.commit()
        self.view_records()

    def view_records(self):
        self.db.cur.execute("""SELECT * FROM users""")
        [self.tree.delete(i) for i in self.tree.get_children()]
        [self.tree.insert('', 'end', values=row) for row in self.db.cur.fetchall()]

    def delete_records(self):
        for selection_item in self.tree.selection():
            self.db.cur.execute("""DELETE FROM users WHERE user_id=?""", (self.tree.set(selection_item, '#1'),))
        self.db.con.commit()
        self.view_records()

    def search_records(self, post):
        post = (post,)
        self.db.cur.execute("""SELECT * FROM users WHERE post=?""", post)
        [self.tree.delete(i) for i in self.tree.get_children()]
        [self.tree.insert('', 'end', values=row) for row in self.db.cur.fetchall()]

    def open_dialog(self):
        Child(root, app)

    def open_update_dialog(self):
        Update()

    def open_search_dialog(self):
        Search()


class Child(tk.Toplevel):
    """Класс для дочернего окна"""

    def __init__(self, root, app):
        super().__init__(root)
        self.init_child()
        self.view = app

    def init_child(self):
        self.title('Добавить игрока')
        self.geometry('400x250+400+300')
        self.resizable(False, False)

        label_description = tk.Label(self, text='Табельный номер')
        label_description.place(x=50, y=25)
        self.entry_description = ttk.Entry(self)
        self.entry_description.place(x=170, y=25)

        label_name = tk.Label(self, text='Фамилия И.О.')
        label_name.place(x=50, y=50)
        self.entry_name = ttk.Entry(self)
        self.entry_name.place(x=170, y=50)

        label_dob = tk.Label(self, text='Дата рождения')
        label_dob.place(x=50, y=75)
        self.dob = DateEntry(self, width=12, background='darkblue',
                             foreground='white', borderwidth=2, date_pattern='MM/dd/yyyy')
        self.dob.place(x=170, y=75)

        label_post = tk.Label(self, text='Должность')
        label_post.place(x=50, y=100)
        self.post = ttk.Combobox(self, values=[u'Преподаватель', u'Старший преподаватель', u'Доцент', u'Профессор',
                                               u'Зав кафедрой', u'Декан', u'Проректор', u'Ректор'])
        self.post.place(x=170, y=100)

        label_sd = tk.Label(self, text='Учёная степень')
        label_sd.place(x=50, y=125)
        self.sd = ttk.Combobox(self, values=[u'Бакалавр', u'Магистр', u'Кандидат наук', u'Доктор наук'])
        self.sd.place(x=170, y=125)

        label_burden = tk.Label(self, text='Нагрузка (ч./нед.)')
        label_burden.place(x=50, y=150)
        self.entry_burden = ttk.Entry(self)
        self.entry_burden.place(x=170, y=150)

        label_sall = tk.Label(self, text='Зарплата (руб.)')
        label_sall.place(x=50, y=175)
        self.entry_sall = ttk.Entry(self)
        self.entry_sall.place(x=170, y=175)

        btn_cancel = ttk.Button(self, text='Закрыть', command=self.destroy)
        btn_cancel.place(x=300, y=200)

        self.btn_ok = ttk.Button(self, text='Добавить')
        self.btn_ok.place(x=220, y=200)
        self.btn_ok.bind('<Button-1>', lambda event: self.view.records(self.entry_description.get(),
                                                                       self.entry_name.get(),
                                                                       self.dob.get(),
                                                                       self.post.get(),
                                                                       self.sd.get(),
                                                                       self.entry_burden.get(),
                                                                       self.entry_sall.get()))

        self.grab_set()
        self.focus_set()


class Update(Child):
    def __init__(self):
        super().__init__(root, app)
        self.init_edit()
        self.view = app

    def init_edit(self):
        self.title("Редактировать запись")
        btn_edit = ttk.Button(self, text="Редактировать")
        btn_edit.place(x=205, y=200)
        btn_edit.bind('<Button-1>', lambda event: self.view.update_record(self.entry_description.get(),
                                                                          self.entry_name.get(),
                                                                          self.dob.get(),
                                                                          self.post.get(),
                                                                          self.sd.get(),
                                                                          self.entry_burden.get(),
                                                                          self.entry_sall.get()))
        self.btn_ok.destroy()


class Search(tk.Toplevel):
    def __init__(self):
        super().__init__()
        self.init_search()
        self.view = app

    def init_search(self):
        self.title("Поиск")
        self.geometry("300x100+400+300")
        self.resizable(False, False)

        self.post_search = ttk.Combobox(self,
                                        values=[u'Преподаватель', u'Старший преподаватель', u'Доцент', u'Профессор',
                                                u'Зав кафедрой', u'Декан', u'Проректор', u'Ректор'])
        self.post_search.place(x=150, y=20, width=150)

        btn_cancel = ttk.Button(self, text="Закрыть", command=self.destroy)
        btn_cancel.place(x=185, y=50)

        btn_search = ttk.Button(self, text="Поиск")
        btn_search.place(x=105, y=50)
        btn_search.bind('<Button-1>', lambda event: self.view.search_records(self.post_search.get()))
        btn_search.bind('<Button-1>', lambda event: self.destroy(), add='+')


class DB:
    def __init__(self):
        with sq.connect('Kafedra.db') as self.con:
            self.cur = self.con.cursor()
            self.cur.execute("""CREATE TABLE IF NOT EXISTS users (
                user_id INTEGER PRIMARY KEY AUTOINCREMENT,
                name TEXT NOT NULL,
                date_of_birth TEXT,
                post TEXT NOT NULL,
                science_degree TEXT,
                burden INTEGER,
                wages INTEGER
                )""")

    def insert_data(self, user_id, name, date_of_birth, post, science_degree, burden, wages):
        self.cur.execute(
            """INSERT INTO users(user_id, name, date_of_birth, post, science_degree, burden, wages) VALUES (?, ?, ?, ?, ?, ?, ?)""",
            (user_id, name, date_of_birth, post, science_degree, burden, wages))
        self.con.commit()


if __name__ == "__main__":
    root = tk.Tk()
    db = DB()
    app = Main(root)
    app.pack()
    root.title("Отдел кадров")
    root.geometry("1000x450+300+200")
    root.resizable(False, False)
    root.mainloop()
