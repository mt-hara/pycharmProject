from typing import List, Any

from excelcls.absexcel import AbsExcelApp
from excelcls.absexcel import AbsExcelWorkBook


class ConcExcelApp(AbsExcelApp):

    def __init__(self):
        super().__init__()

    def close_app(self):
        self.app.quit()


class ConcExcelWorkBook():

    sh_pos: List[Any]

    def __init__(self, app, filepath):
        self.wb = AbsExcelWorkBook(app, filepath)
        self.ws = self.wb.xlws
        self.shape = self.ws.shapes
        self.sh_pos = []

    def wb_close(self):
        self.wb.close_book()

    def shapes_pos(self):
        for sh in self.shape:
            var = {}
            var["top"] = str(sh.top)
            var["left"] = str(sh.left)
            self.sh_pos.append(var)
            # print("top : " + str(sh.top))
            # print("left: " + str(sh.left))


if __name__ == "__main__":
    xlapp = ConcExcelApp()
    filename = "C:\\Users\\m-hara\\Desktop\\取引先コード取得済\\業態調査票（㈱八木熊）.xlsx"

    cli = ConcExcelWorkBook(xlapp.app, filename)
    cli.shapes_pos()


    for i in cli.sh_pos:
        print(i)

    cli.wb_close()
    xlapp.close_app()
