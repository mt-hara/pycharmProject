from typing import *
import xlwings as xlw
import tkinter
import tkinter.messagebox as msgbox
from excelcls.absexcel import AbsExcelApp

root = tkinter.Tk()
root.withdraw()


class ConExcelApp(AbsExcelApp):

    def __init__(self) -> None:
        super().__init__()
        self.app.calculation = "manual"
        self.app.display_alerts = False

    # def close_app(self) -> None:
    #     self.app.quit()

    def open_wb(self, filepath) -> None:
        try:
            self.xlwb = self.app.books.open(filepath)
        except AttributeError:
            msgbox.showinfo("エラー", "ファイル読み込みエラー")
            exit(0)

    def close_wb(self) -> object:
        self.xlwb.close()

    def selerct_sheet(self) -> None:
        try:
            self.xlws = self.xlwb.sheets[0]
        except AttributeError:
            msgbox.showinfo("エラー", "シート読み込みエラー")
            exit(0)


class ConExcelWorkBook():
    def __init__(self):
        pass

    # def __init__(self, app :object, filepath: str):
    #     self.wb = AbsExcelWorkBook(app, filepath)
    #     self.ws = self.wb.xlws
    #     self.shape = self.ws.shapes
    #     self.sh_pos: List[Any] = []
    #
    # def open_book(self, app, filepath):
    #     try:
    #         self.exwb = app.books.open(filepath)
    #         self.exwb.app.calculate = "manual"
    #         self.exwb.app.display_alerts = False
    #
    #     except AttributeError:
    #         pass
    #
    # def wb_close(self):
    #     self.wb.close_book()
    #
    # def get_shape_pos(self):
    #     for sh in self.shape:
    #         var = {}
    #         var["top"] = sh.top
    #         var["left"] = sh.left
    #         self.sh_pos.append(var)


if __name__ == "__main__":
    xlapp = ConExcelApp()
    filename = "C:\\Users\\m-hara\\Desktop\\取引先コード取得済\\業態調査票（㈱八木熊）.xlsx"
    xlapp.open_wb(filename)

    xlapp.close_wb()
    xlapp.close_app()
    # cli = ConExcelWorkBook(xlapp.app, filename)
    # cli.get_shape_pos()
    #
    #
    # for i in cli.sh_pos:
    #     # print(i)
    #     print("top = " + str(i["top"]))
    #     print("left= " + str(i["left"]))
    #
    # cli.wb_close()
    # xlapp.close_app()
