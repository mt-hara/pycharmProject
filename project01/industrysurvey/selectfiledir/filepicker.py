import pathlib
from selectfiledir.abstractfilepicker import AbstractFileDialog
import tkinter.filedialog as dialog
import tkinter


class GetFile(AbstractFileDialog):
    def __init__(self, def_dir, fType, *args, **kw):
        super().__init__(def_dir, fType, *args, **kw)
        self.file_list = []

    def get_files(self):
        root = tkinter.Tk()
        root.withdraw()
        result = dialog.askopenfilenames(filetypes=self.fType, initialdir=self.initdir)
        if not self.hasItem(result):
            return False
        self.file_list = list(result)

        return self.file_list


class GetDirs(AbstractFileDialog):
    def __init__(self, def_dir, ftype, *args, **kw):
        super().__init__(def_dir, ftype, *args, **kw)
        self.file_list = []
        self.exttype = ""

        def get_files(self):
            result = dialog.askdirectory(initialdir=self.initdir)
            if not self.hasItem(result):
                return False

            self.set_ext_type(self.ftype)
            self.file_list = self.get_files_by_ext(result)
            return self.file_list

        def get_files_by_ext(self, dirs, **kw):
            self.set_ext_type(self.ftype)
            templist = list(pathlib.Path(dirs).glob(self.set_ext_type))
            for x in templist:
                self.file_list.append(str(x))
            return self.file_list

        def set_ext_type(self, ftype):
            self.exttype = ftype[0][1]
