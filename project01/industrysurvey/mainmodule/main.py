import sys
import traceback
from selectfiledir.filepicker import GetFile
from excelapp.ExcelApp import ExcelApp, ExcelWorkBook
from iterators.ItemIterator import *
from dto.ExcelSheetDTO import ExcelSheetDTO
from dao.TableDAO.QueryContext import ExecuteQuery


class FilePicker(GetFile):
    __def_dir = "DeskTop"
    __ftype =  [("Excel2003ファイル", "*.xlsx")]

    def __init__(self):
        super().__init__(self.__def_dir, self.__ftype)

    def get_list(self):
        if self.get_files() is False:
            exit()
        else:
            return self.file_list


    # def get_filepath(self):
    #     getfilecls = GetFile(self.__def_dir, self.__ftype)
    #     result = getfilecls.get_files()
    #     if result == False:
    #         return False
    #     else:
    #         return result

class Excel():
    def __init__(self,filename):
        self.baseapp = ExcelApp()
        self.app = self.baseapp.app
        self.wb = ExcelWorkBook()
        self.wb.open_wb(self.app, filename)
        self.ws = self.wb.xlws

    def open_workbook(self, filename):
        pass

    def close_app_wb(self):
        self.wb.close_workbook()

    def close_app(self):
        self.baseapp.close_App()

    def close(self):
        self.close_app_wb()
        self.close_app()


class SheetDataToDTO():
    def __init__(self, worksheet):
        self.ws = worksheet
        self.dto = self.get_dto()

    def get_dto(self):
        try:
            self.dto = ExcelSheetDTO(self.ws)
        except AttributeError as e:
            type_, value, traceback_, = sys.exc_info()
            print(traceback.format_exception(type_, value, traceback_))
            # self.ws.close()
            quit()
        else:
            return self.dto


if __name__ == "__main__":
    Pickercls = FilePicker()
    filelist = Pickercls.get_list()
    for x in filelist:
        excelcls = Excel(x)
        ws = excelcls.ws
        s = SheetDataToDTO(ws)
        print(s)
