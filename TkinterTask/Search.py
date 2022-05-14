import tkinter as tk
from tkinter import ttk

class Search(tk.Toplevel):
    """Класс для окна поиска"""

    def __init__(self, root):
        super().__init__(root)
        self.init_search()

    def init_search(self):
        self.title('Найти игрока')
        self.geometry('300x100+400+300')
        self.resizable(False, False)
        label_search = tk.Label(self, text='Поиск')
        label_search.place(x=50, y=20)
        self.entry_search_name = ttk.Entry(self)
        self.entry_search_name.place(x=110, y=20)
        btn_close = ttk.Button(self, text='Закрыть', command=self.destroy)
        btn_close.place(x=160, y=60)
        self.btn_accept = ttk.Button(self, text='Поиск')
        self.btn_accept.place(x=80, y=60)
        self.btn_accept.bind('<Button-1>')
        self.grab_set()
        self.focus_set()
