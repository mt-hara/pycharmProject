from excelcls.absexcel import AbsExcelApp
from excelcls.absexcel import AbsExcelWorkBook


class ConcExcelApp(AbsExcelApp):

    def __init__(self):
        super().__init__()

    def close_app(self):
        self.app.quit()


class ConcExcelWorkBook():

    def __init__(self, app, filepath):
        self.wb = AbsExcelWorkBook(app, filepath)
        self.ws = self.wb.xlws
        self.datadict = {}

    def wb_close(self):
        self.wb.close_book()
