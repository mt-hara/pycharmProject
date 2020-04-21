import sys
import traceback
from dao.BaseEngine import BaseSession
from dao.TableModel.CustomerMaster import CustomerMaster
from dao.TableDAO.Insert import Instert
from dao.TableDAO.Update import Update


class ExecuteQuery(BaseSession):
    def __init__(self,xldto):
        super().__init__()
        self.xldto = xldto
        self.iqexecute = self.has_record()

    def execute(self):
        self.iqexecute.execute(self.xldto)

    def has_record(self):
        param = self.xldto.xlCustomerCd
        if param == None:
            raise ValueError("取引先コード取得エラー")
        try:
            result = self.session.query(CustomerMaster).filter(CustomerMaster.customerCd == param).all()
        except Exception as e:
            raise Exception
            # type_, value, traceback_ = sys.exc_info()
            # print(traceback.format_exception(type_, value,traceback_))
            # return
        else:
            if len(result) == 0:
                return Instert()
            else:
                return Update()


class DeleleAll(BaseSession):
    def __init__(self):
        super().__init__()
        try:
            with self.transaction() as session:
                del_list = self.session.quety(CustomerMaster).all()
                for item in del_list:
                    self.session.delete(item)
        except Exception as e:
            print(e)


# class main():
#     def __init__(self, filename):
#         self.baseapp = ExcelApp()
#         self.app = self.baseapp.app
#         self.wb = ExcelWorkBook()
#         self.wb.open_wb(self.app, filename)
#         self.ws = self.wb.xlws
#
#     def close(self):
#         self.wb.close_workbook()
#         self.baseapp.close_App()

# if __name__ == "__main__":
#     filename = "C:\\Users\\m-hara\\Desktop\\取引先コード取得済\\業態調査票（（株）清和光学製作所）.xlsx"
#     # filename = "C:\\Users\\m-hara\\Desktop\\取引先コード取得済\\業態調査票（スペクトラ・フィジックス株式会社）.xlsx"
#     excls = main(filename)
#     ws = excls.ws
#
#     try:
#         data = ExcelSheetDTO(ws)
#     except AttributeError as e:
#         type_, value, traceback_ = sys.exc_info()
#         print(traceback.format_exception(type_, value, traceback_))
#         excls.close()
#         quit()
#     else:
#         TableMigration()
#         context = ExecuteQuery(data)
#         context.execute()
#
#
#         print("code finish")
#         excls.close()