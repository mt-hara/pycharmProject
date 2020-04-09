import sys
import traceback
from excelapp.ExcelApp import ExcelApp,ExcelWorkBook
from dto.ExcelSheetDTO import ExcelSheetDTO

from dao.BaseEngine import BaseSession
from dao.tablemodel.CustomerMaster import CustomerMaster
from dao.tablemodel.StockStatusMaster import StockStatusMaster
from dao.crud.CRUD_old import RegistData

class Main(BaseSession):
    def __init__(self,xldto):
        super().__init__()

        try:
            # MetaBase().metadata.create_all(self.engine)

            customer = CustomerMaster()
            customer.stockstatus = StockStatusMaster()
            customer.set_data(xldto)
            customer.stockstatus.set_data(xldto)
            # customer.customerCd = "789"
            # customer.customerName = "abcde"
            # customer.stockstatus = StockStatusMaster(stockListingStatus="上場",
            #                                          stockMarket="test market")

            with self.transaction() as session:
                self.session.add(customer)
        except Exception as e:
            print(e)



class OpenExcel():
    def __init__(self, filename):
        super().__init__()
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
    xlapp = OpenExcel(filename)
    ws = xlapp.ws
    try:
        data = ExcelSheetDTO(ws)
        RegistData(data)
    except AttributeError as e:
        type_, value, traceback_ = sys.exc_info()
        print(traceback.format_exception(type_, value, traceback_))
        xlapp.close()
        quit()
    else:
        pass



# try:
#     Base().metadata.create_all(self.engine)
#
#     customer = CustomerMaster()
#     customer.customerCd = "789"
#     customer.customerName = "abcde"
#     customer.stockstatus = StockStatusMaster(stockListingStatus="上場",
#                                              stockMarket="test market")
#
#     with self.transaction() as session:
#         self.session.add(customer)
# except Exception as e:
#     print(e)
