from dto.excelbase import AbsExcelApp
from dto.excelbase import AbsExcelWorkBook

class ExcelData():
    def __init__(self, app, filepath):
        self.xlwb = AbsExcelWorkBook(app, filepath)



