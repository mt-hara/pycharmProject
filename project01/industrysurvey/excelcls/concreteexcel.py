from typing import Dict, Any
import tkinter.messagebox as msgbox
from excelcls.abstractexcel import AbstractExcelApp
from excelcls.abstractexcel import AbstractExcelWorkBook
from selectfiledir.filepicker import *
import  dataclasses
from abstractdto.abscustomermstrdto import AllCustomerMaster
from dto.exshapesdto import ShapesDataDTO

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


class ExcelShapesPos():
    def __init__(self, xlsheet):
        self.shapes_pos = []
        self.xlsheet = xlsheet

    def get_shape_pos(self):
        shapes = self.xlsheet.shapes
        for sh in shapes:
            var: Dict[str, Any] = {"top": sh.top, "left": sh.left}
            self.shapes_pos.append(var)


class ConcreteExcel():

    def get_ws(self):
        filename = "C:\\Users\\m-hara\\Desktop\\取引先コード取得済\\業態調査票（㈱八木熊）.xlsx"
        self.baseapp = ExcelApp()
        self.app = self.baseapp.app

        self.wb = ExcelWorkBook()
        self.wb.open_wb(self.app, filename)
        self.ws = self.wb.xlws
        return self.ws






if __name__ == "__main__":
    # def_dir = "DeskTop"
    # ftype = [("Excel2003ファイル", "*.xlsx")]
    # dialog = GetFile(def_dir,ftype)
    # files = dialog.get_files()


    filename = "C:\\Users\\m-hara\\Desktop\\取引先コード取得済\\業態調査票（（株）清和光学製作所）.xlsx"

    baseapp = ExcelApp()
    app = baseapp.app

    wb = ExcelWorkBook()
    wb.open_wb(app, filename)
    ws = wb.xlws

    exshapes = ExcelShapesPos(ws)
    exshapes.get_shape_pos()
    dto = AllCustomerMaster()
    dao = ShapesDataDTO(dto)


    dao.get_shapes_dt(exshapes.shapes_pos)
    dto.set_cell_data(ws)
    d = dataclasses.asdict(dto)
    for x,y in d.items():
        print(x,y)

    wb.close_workbook()
    baseapp.close_App()
