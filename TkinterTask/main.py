import tkinter as tk
from tkinter import ttk
import sqlite3 as sq
from Child import *
from Search import *


class Main(tk.Frame):
    """Класс для главного окна"""

    def __init__(self, root):
        super().__init__(root)
        self.init_main()
        self.view_records()
        self.db = db

    def init_main(self):
        toolbar = tk.Frame(bg='#a0dea0', bd=4)
        toolbar.pack(side=tk.TOP, fill=tk.X)
        # self.add_img = tk.PhotoImage(file="BD/11.gif")
        btn_open_dialog = tk.Button(toolbar, text='Добавить игрока', command=self.open_dialog, bg='#5da130', bd=0,
                                    compound=tk.TOP)
        btn_open_dialog.pack(side=tk.LEFT)
        btn_open_search = tk.Button(toolbar, text='Поиск', command=self.open_search, bg='#5da130', bd=0,
                                    compound=tk.TOP)
        btn_open_search.pack(side=tk.RIGHT)
        self.tree = ttk.Treeview(self, columns=('user_id', 'name', 'sex', 'old', 'score'), height=15, show='headings')
        self.tree.column('user_id', width=50, anchor=tk.CENTER)
        self.tree.column('name', width=180, anchor=tk.CENTER)
        self.tree.column('sex', width=140, anchor=tk.CENTER)
        self.tree.column('old', width=140, anchor=tk.CENTER)
        self.tree.column('score', width=140, anchor=tk.CENTER)
        self.tree.heading('user_id', text='ID')
        self.tree.heading('name', text='Имя игрока')
        self.tree.heading('sex', text='Пол игрока')
        self.tree.heading('old', text='Возраст игрока')
        self.tree.heading('score', text='Результат игрока')
        self.tree.pack()

    def view_records(self):
        self.db.cur.execute("""SELECT * FROM users""")
        [self.tree.delete(i) for i in self.tree.get_children()]
        [self.tree.insert('', 'end', values=row) for row in self.db.cur.fetchall()]

    def records(self, user_id, name, sex, old, score):
        self.db.insert_data(user_id, name, sex, old, score)
        self.view_records()

    def open_dialog(self):
        Child(self)

    def open_search(self):
        Search(self)


class DB:
    def __init__(self):
        with sq.connect('Saper.db') as self.con:
            self.cur = self.con.cursor()
            self.cur.execute("""CREATE TABLE IF NOT EXISTS users (
                   user_id INTEGER PRIMARY KEY AUTOINCREMENT,
                   name TEXT NOT NULL,
                   sex INTEGER NOT NULL DEFAULT 1,
                   old INTEGER,
                   score INTEGER
                   )""")


    def insert_data(self, user_id, name, sex, old, score):
        self.cur.execute("""INSERT INTO users(user_id, name, sex, old, score) VALUES (?, ?, ?, ?, ?)""",
                             (user_id, name, sex, old, score))
        self.con.commit()

if __name__ == "__main__":
    root = tk.Tk()
    db = DB()
    app = Main(root)
    app.pack()
    root.title("Работа с базой данных Сапер")
    root.geometry("650x450+300+200")
    root.mainloop()
