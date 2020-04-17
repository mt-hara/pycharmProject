# from typing import Dict, Any
import tkinter.messagebox as msgbox
from excelapp.AbstractExcelApp import AbstractExcelApp
from excelapp.AbstractExcelApp import AbstractExcelWorkBook
from selectfiledir.filepicker import *

root = tkinter.Tk()
root.withdraw()


class ExcelApp(AbstractExcelApp):
    def __init__(self):
        super().__init__()

    def get_app(self):
        return self.app


class ExcelWorkBook(AbstractExcelWorkBook):
    def __init__(self):
        super().__init__()

    def open_wb(self, app, filepath):
        try:
            self.xlwb = app.books.open(filepath)
        except AttributeError:
            msgbox.showinfo("エラー", "ファイル読み込みエラー")
            exit(0)
        else:
            self.select_sheet()

    def select_sheet(self):
        try:
            self.xlws = self.xlwb.sheets[0]
        except AttributeError:
            msgbox.showinfo("エラー", "シート読み込みエラー")
            exit(0)
        # else:
        #     return self.xlws

    def close_workbook(self):
        self.xlwb.close()