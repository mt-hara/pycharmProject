from typing import Dict, Any
import tkinter.messagebox as msgbox
from excelapp.AbstractExcelApp import AbstractExcelApp
from excelapp.AbstractExcelApp import AbstractExcelWorkBook
from selectfiledir.filepicker import *

root = tkinter.Tk()
root.withdraw()


class ExcelApp(AbstractExcelApp):
    def __init__(self):
        super().__init__()

    def set_app(self):
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

    def close_workbook(self):
        self.xlwb.close()


# class ExcelShapesPosOld():
#     def __init__(self, xlsheet):
#         self.shapes_pos = []
#         self.xlsheet = xlsheet
#
#     def get_shape_pos(self):
#         shapes = self.xlsheet.shapes
#         for sh in shapes:
#             var: Dict[str, Any] = {"top": sh.top, "left": sh.left}
#             self.shapes_pos.append(var)


    # def_dir = "DeskTop"
    # ftype = [("Excel2003ファイル", "*.xlsx")]
    # dialog = GetFile(def_dir,ftype)
    # files = dialog.get_files()


    # filename = "C:\\Users\\m-hara\\Desktop\\取引先コード取得済\\業態調査票（ＮＣＤ NakajimaControlDesign）.xlsx"
    #
    # baseapp = ExcelApp()
    # app = baseapp.app
    #
    # wb = ExcelWorkBook()
    # wb.open_wb(app, filename)
    # ws = wb.xlws
    #
    # exshapes = ExcelShapesPosOld(ws)
    # exsheetdto = ExcelSheetDTO(ws)
    # for k, v in exsheetdto.__dict__.items():
    #     print("{} : {}: type-{}".format(k,v,type(v)))
    # exshapes.get_shape_pos()
    # dto = CustomerMaster()
    # dto = ExcelSheetDTO(ws)
    # shapes_dto = ShapePosToValue(dto)
    #
    #
    # shapes_dto.set_shapes_data(exshapes.shapes_pos)
    # dto.set_cell_data(ws)
    # d = dataclasses.asdict(dto)
    # for x,y in d.items():
    #     print(x,y)

    # wb.close_workbook()
    # baseapp.close_App()
