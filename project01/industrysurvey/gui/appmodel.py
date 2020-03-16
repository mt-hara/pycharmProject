import tkinter as tk
import tkinter.messagebox as msgbox
from selectfiledir.filepicker import GetFile
from selectfiledir.filepicker import GetDirs


class AppModel():
    def __init__(self,master) -> None:
        self.__observer = None

        self.master = master
        self.t_width = 600
        self.t_height = 100

    def register(self, controller):
        self.controller = controller




