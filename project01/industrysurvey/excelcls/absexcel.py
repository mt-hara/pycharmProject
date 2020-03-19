# from typing import *
import xlwings as xlw
from abc import ABCMeta
from abc import abstractmethod


class AbstractApp(metaclass=ABCMeta):
    def __init__(self):
        self.app = xlw.App(visible=True)
        self.xlwb: object = None
        self.xlws: object = None

    def close_app(self) -> None:
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


class AbstractExcelApp():
    def __init__(self):
        self.app  = None
        self.xlwb = None
        self.xlws = None

    def open_app(self):
        self.app = xlw.App(visible=True)
        return self.app

    def close_app(self):
        self.app.quit()

    def open_wb(self, filepath):
        self.xlwb = AbstractWorkBook().open_wb(self.app, filepath)

    def close_wb(self):
        self.xlwb.close()

    def open_ws(self):
        self.xlws = AbstractWorkSheet().open_worksheet(self.xlwb)


class AbstractWorkBook():
    def __init__(self):
        self.wb = None

    def open_wb(self,app,filepath):
        self.wb = app.books.open(filepath)
        return self.wb


class AbstractWorkSheet():
    def __init__(self):
        self.sheet = None

    def open_worksheet(self, wb):
        self.sheet = wb.sheets[0]
        return  self.sheet


if __name__ == "__main__":
    cli = AbstractExcelApp()
    cli.open_app()
    filename = "C:\\Users\\m-hara\\Desktop\\取引先コード取得済\\業態調査票（㈱八木熊）.xlsx"

    cli.open_wb(filename)
    cli.open_ws()
    print(cli.xlws.range("H3").value)
    cli.close_wb()
    cli.close_app()

