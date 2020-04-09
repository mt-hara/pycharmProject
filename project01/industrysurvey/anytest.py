import sys
import traceback
from excelapp.ExcelApp import ExcelApp, ExcelWorkBook
from dto.ExcelSheetDTO import ExcelSheetDTO
from dao.crud.DataPrcessing import ExecuteNonQuery

class main():
    def __init__(self, filename):
        self.baseapp = ExcelApp()
        self.app = self.baseapp.app
        self.wb = ExcelWorkBook()
        self.wb.open_wb(self.app, filename)
        self.ws = self.wb.xlws

    def close(self):
        self.wb.close_workbook()
        self.baseapp.close_App()


if __name__ == "__main__":
    filename = "C:\\Users\\m-hara\\Desktop\\取引先コード取得済\\業態調査票（（株）清和光学製作所）.xlsx"
    excls = main(filename)
    ws = excls.ws

    try:
        data = ExcelSheetDTO(ws)
    except AttributeError as e:
        type_, value, traceback_ = sys.exc_info()
        print(traceback.format_exception(type_, value, traceback_))
        excls.close()
        quit()
    else:
        te = ExecuteNonQuery(data)
        # customer_model = Update(data)
        # customer_model = Insert(data)


    print("Finish code")
    excls.close()