import tkinter as tk
import tkinter.messagebox as msgbox
from selectfiledir.filepicker import GetFile
from selectfiledir.filepicker import GetDirs


class AppModel():
    def __init__(self,master) -> None:
        self.__observer = None
        self.master = master
        #main Frame size
        self.t_width = 600
        self.t_height = 100
        self.def_dir="DeskTop"
        self.ftype=[("Excel2003ファイル","*.xlsx")]
        self.__filepath = []


    @property
    def filepath(self):
        return self.__filepath
    @filepath.setter
    def filepath(self,files):
        self.__filepath = files


    def register(self, controller):
        self.controller = controller






