import sys
import pathlib

import tkinter as tk
import tkinter.filedialog as FileDialog
import tkinter.messagebox as msgbox
from tkinter import Tk

from gui.appmodel import AppModel
from gui.appview import AppView
from gui.appcontroller import AppController


class AbstractApp(tk.Frame):
    def __init__(self, master=None, cnf={}, **kw):
        super().__init__(master=master,cnf={}, **kw)
        self.grid()


class MyApp(AbstractApp):
    def __init__(self,master=None,cnf={}, **kw):
        super().__init__(master=master,cnf=cnf, **kw)
        self.master = master
        self.__filepath = []
        self.__dirpath = ""
        self.__savepath = ""

        self.model = AppModel(self.master)
        self.view = AppView(self.master, self.model)
        self.controller = AppController(self.master, self.model, self.view)

        self.view.top_view()


if __name__ == "__main__":
    root: Tk = tk.Tk()
    apps = MyApp(master=root)
    apps.master.title("My Application")
    apps.master.geometry("650x400")
    apps.mainloop()