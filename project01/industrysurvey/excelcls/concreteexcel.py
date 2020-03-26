from typing import Dict, Any, List
import xlwings as xlw
import tkinter
import tkinter.messagebox as msgbox
from excelcls.abstractexcel import AbstractExcelApp
from excelcls.abstractexcel import AbstractExcelWorkBook

from excelcls.excelshapes import ShapeDataDTO

root = tkinter.Tk()
root.withdraw()


class ExcelApp(AbstractExcelApp):
    def __init__(self):
        super().__init__()

    def set_app(self):
        return self.app

    # def close_App(self):
    #     self.app.quit()


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

    def close_workbook(self):
        self.xlwb.close()


class ExcelShapesPos():
    def __init__(self, xlsheet):
        self.shapes_pos = []
        self.xlsheet = xlsheet

    def get_shape_pos(self):
        shapes = self.xlsheet.shapes
        for sh in shapes:
            var: Dict[str, Any] = {"top": sh.top, "left": sh.left}
            self.shapes_pos.append(var)


if __name__ == "__main__":
    filename = "C:\\Users\\m-hara\\Desktop\\取引先コード取得済\\業態調査票（㈱八木熊）.xlsx"

    baseapp = ExcelApp()
    app = baseapp.app

    wb = ExcelWorkBook()
    wb.open_wb(app, filename)
    ws = wb.xlws

    exshapes = ExcelShapesPos(ws)
    exshapes.get_shape_pos()

    dto = ShapeDataDTO()
    dto.get_shape_data(exshapes.shapes_pos)
    print(dto.shapesdto.biz_type)

    wb.close_workbook()
    baseapp.close_App()
