import tkinter as tk
import tkinter.filedialog as filedialog
import tkinter.messagebox as msgbox
from selectfiledir.filepicker import GetFile
from selectfiledir.filepicker import GetDirs


class AppController():
    def __init__(self, master, model, view):
        self.master = master
        self.model = model
        self.view = view
        self.view.register(self)

    def click_get_file(self):
        dialog = GetFile(self.model.def_dir,self.model.ftype)
        files = dialog.get_files()
        if files == False:
            return False
        self.model.filepath = files

        for x in self.model.filepath:
            print(x)

    def exit(self):
        self.master.destroy()
        self.master.quit()