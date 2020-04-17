import sys
import traceback
from selectfiledir.filepicker import GetFile
from excelapp.ExcelApp import ExcelApp, ExcelWorkBook
from iterators.ItemIterator import *
from dto.ExcelSheetDTO import ExcelSheetDTO
from dao.TableDAO.QueryContext import ExecuteQuery


class ExcelDataToDTO():
    def __init__(self):
        self.baseapp = ExcelApp()
        self.app = self.baseapp.app
        self.wb = ExcelWorkBook()
        self.dto = None

    def get_dto(self,filename):
        self.wb.open_wb(self.app, filename)
        try:
            self.dto = ExcelSheetDTO(self.wb.xlws)
        except AttributeError as e:
            type_, value, traceback_ = sys.exc_info()
            print(traceback.format_exception(type_, value, traceback_))
            self.close()
            quit()
        else:
            return self.dto

    def close_app_wb(self):
        self.wb.close_workbook()

    def close_app(self):
        self.app.quit()

    def close_baseapp(self):
        self.baseapp.close_App()

    def close(self):
        self.close_app_wb()
        self.close_baseapp()

class FilePicker():
    def __init__(self):
        self.__def_dir = "DeskTop"
        self.__ftype =  [("Excel2003ファイル", "*.xlsx")]
        self.picker = GetFile(self.__def_dir, self.__ftype)
        self.file_list = self.picker.get_files()

    def get_file_list(self):
        if self.file_list is False:
            quit()
        else :
            return self.file_list




if __name__ == "__main__":
    picker = FilePicker()
    # ls =picker.get_file_list()
    # for x in ls:
    #     print(x)
    # Pickercls = FilePicker()
    filelist = picker.get_file_list()
    print(len(filelist))
    item_self = ItemShelf()
    excelcls = ExcelDataToDTO()
    cnt = 0
    for x in filelist:
        cnt = cnt +1
        dto = excelcls.get_dto(x)
        item_self.append(dto)
        excelcls.close_app_wb()
        print(cnt)

    excelcls.close_app()
    print("Close")
    it = item_self.iterator()
    i = 0
    while it.hasnext():
        i = i + 1
        item = it.next()
        print("{}:{}:{}".format(i,item.xlCustomerCd,item.xlCustomerName))

    print("Finish")