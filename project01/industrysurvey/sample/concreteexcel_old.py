from typing import Dict, Any, List
import tkinter
import tkinter.messagebox as msgbox
from sample.abstractexcel_old import AbstractWorkBook

root = tkinter.Tk()
root.withdraw()


class ConcreateExcelWorkBook(AbstractWorkBook):
    def __init__(self):
        super().__init__()

    def open_wb(self, filepath: str):
        try:
            self.xlwb = self.xlapp.books.open(filepath)
            # return self.xlwb
        except AttributeError:
            msgbox.showinfo("エラー", "ファイル読み込みエラー")
            exit(0)

    def close_wb(self):
        self.xlwb.close()

    def select_sheet(self):
        try:
            self.xlws = self.xlwb.sheets[0]
            # return self.xlws
        except AttributeError:
            msgbox.showinfo("エラー", "シート読み込みエラー")
            exit(0)

    def open_file(self,filepath):
        self.open_wb(filepath)
        self.select_sheet()


class ExcelData():
    def __init__(self,worksheet):
        self.shape_pos: List[Any] = []
        self.sheet: object = None
        self.get_worksheet(worksheet)

    def get_worksheet(self,xlws) -> object:
        self.sheet = xlws
        return  self.sheet

    def close_wb(self,xlwb):
        xlwb.close()

    def get_shape_pos(self):
        shapes = self.sheet.shapes
        for sh in shapes:
            var: Dict[str, Any] = {"top": sh.top, "left": sh.left}
            self.shape_pos.append(var)
            

class GetShapeData():
    def __init__(self):
        self.vender_biz_type=None
        self.capital_form = None
        self.corporate_type = None
        self.stock_status = None
        self.stock_marcket = ""
        self.iso9000_certif = ""
        self.iso14000_certif = ""
        self.pos_data: List[Any] = []




if __name__ == "__main__":
    xlapp = ConcreateExcelWorkBook()
    filename = "C:\\Users\\m-hara\\Desktop\\取引先コード取得済\\業態調査票（㈱八木熊）.xlsx"
    xlapp.open_file(filename)
    cl = ExcelData(xlapp.xlws)
    cl.get_shape_pos()
    print(cl.shape_pos)

    print(cl.sheet.range("H5").value)
    cl.close_wb(xlapp.xlwb)
    xlapp.close_app()
    # xlapp.select_sh
    # for i in cli.sh_pos:
    #     # print(i)
    #     print("top = " + str(i["top"]))
    #     print("left= " + str(i["left"]))
    #
    # cli.wb_close()
    # xlapp.close_app()
