from typing import *
import xlwings as xlw
from abc import ABCMeta
from abc import abstractmethod


class AbsExcelApp(metaclass=ABCMeta):
    def __init__(self):
        self.app = xlw.App(visible=True)
        self.xlwb: object = None
        self.xlws: object = None


    def close_app(self) -> object:
        self.app.quit()

    @abstractmethod
    def open_wb(self, *args):
        pass

    @abstractmethod
    def close_wb(self):
        pass

    @abstractmethod
    def selerct_sheet(self):
        pass

