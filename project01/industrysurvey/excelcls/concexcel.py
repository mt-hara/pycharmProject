from typing import *

from excelcls.absexcel import AbsExcelApp
from excelcls.absexcel import AbsExcelWorkBook


class ConExcelApp(AbsExcelApp):

    def __init__(self):
        super().__init__()

    def close_app(self):
        self.app.quit()


class ConExcelWorkBook():

    def __init__(self, app :object, filepath: str):

        self.wb = AbsExcelWorkBook(app, filepath)
        self.ws = self.wb.xlws
        self.shape = self.ws.shapes
        self.sh_pos: List[Any] = []

    def wb_close(self):
        self.wb.close_book()

    def get_shape_pos(self):
        for sh in self.shape:
            var = {}
            var["top"] = sh.top
            var["left"] = sh.left
            self.sh_pos.append(var)


if __name__ == "__main__":
    xlapp = ConExcelApp()
    filename = "C:\\Users\\m-hara\\Desktop\\取引先コード取得済\\業態調査票（㈱八木熊）.xlsx"

    cli = ConExcelWorkBook(xlapp.app, filename)
    cli.get_shape_pos()


    for i in cli.sh_pos:
        # print(i)
        print("top = " + str(i["top"]))
        print("left= " + str(i["left"]))

    cli.wb_close()
    xlapp.close_app()
