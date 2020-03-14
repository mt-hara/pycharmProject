from pathlib import Path
from abc import ABCMeta
from abc import abstractmethod
from abc import ABC
import win32com.client


class AbstractFileDialog(metaclass=ABCMeta):
    def __init__(self, def_dir, fType, *args, **kw):
        self.fType = fType
        self.initdir = Path(self.get_initdir(def_dir))

    @abstractmethod
    def get_files(self):
        pass

    def get_initdir(self, def_dir):
        WHShell = win32com.client.Dispatch("WScript.Shell")
        retdir = WHShell.specialfolders(def_dir) + "\\"
        return retdir

    def hasItem(self, files):
        if files == "" or files is None:
            return False
