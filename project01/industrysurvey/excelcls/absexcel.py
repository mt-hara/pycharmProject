import xlwings as xlw
import tkinter
import tkinter.messagebox as msgbox
from abc import ABCMeta
from abc import abstractmethod
root = tkinter.Tk()
root.withdraw()


class AbsExcelApp(metaclass=ABCMeta):
    def __init__(self):
        self.app = xlw.App(visible=True)

    @abstractmethod
    def close_app(self):
        self.app.quit()


class AbsExcelWorkBook():
    def __init__(self, app, filename) -> None:
        self.app = app
        self.filepath = filename
        self.xlwb = None
        self.xlws = None
        self.open_book(self.app)

    def open_book(self, app):
        try:
            self.xlwb = app.books.open(self.filepath)
            self.xlwb.app.calculate = 'manual'
            self.xlwb.app.display_alerts = False
            self.xlws = self.xlwb.sheets[0]
        except AttributeError:
            msgbox.showinfo("エラー", "ファイル読み込みエラー")
            pass
        finally:
            pass

    def close_book(self):
        self.xlwb.close()
