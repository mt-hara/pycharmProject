import sys
import os
import pathlib

import tkinter as tk
import tkinter.filedialog as filedialog
import tkinter.messagebox as msgbox
from selectfiledir.filepicker import GetFile
from selectfiledir.filepicker import GetDirs


class AbsApplication(tk.Frame):
    def __init__(self, master=None, conf={}, **kw):
        super().__init__(master=master, conf={}, **kw)
        self.grid()

    def cancel_cmd(self):
        self.destroy()
        self.quit()


class Application():
    def __init__(self, master=None, conf={}, **kw) -> None:
        super().__init__(master=master, conf={}, **kw)
        self.master = master



