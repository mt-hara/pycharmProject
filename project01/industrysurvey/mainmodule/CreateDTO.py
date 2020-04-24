import sys
import traceback
import pathlib
import shutil
from iterators.ItemIterator import *
from selectfiledir.filepicker import GetFile
from excelapp.ExcelApp import ExcelApp, ExcelWorkBook
from dto.ExcelSheetDTO import ExcelSheetDTO
from dao.TableDAO.QueryContext import ExecuteQuery
from functions.StopWatch import stop_watch

_log_base_dir = "/LogModule"


class FilePicker():
    def __init__(self):
        self.__def_dir = "DeskTop"
        self.__ftype = [("Excel2003ファイル", "*.xlsx")]
        self.picker = GetFile(self.__def_dir, self.__ftype)
        self.file_list = self.picker.get_files()

    def get_file_list(self):
        if self.file_list is False:
            quit()
        else:
            return self.file_list


class ExcelFile():
    def __init__(self):
        # self.baseapp = None
        self.baseapp = ExcelApp()
        self.app = self.baseapp.app
        self.wb = ExcelWorkBook()
        self.ws = None

    def open_excelapp(self):
        self.baseapp = ExcelApp()

    # @stop_watch
    def open_workbook(self, filepath):
        self.wb.open_wb(self.app, filepath)
        self.ws = self.wb.xlws
        return self.ws

    def close_app_wb(self):
        self.wb.close_workbook()

    def close_app(self):
        self.app.quit()

    def close_baseapp(self):
        self.baseapp.close_App()

    def close(self):
        self.close_app_wb()
        self.close_baseapp()


class ExcelDataToDTO():
    def __init__(self):
        self.file_list = []
        self.get_filepath_list()
        self.excelapp = ExcelFile()
        self.item_shelf = ItemShelf()
        self.dto = None

    def get_filepath_list(self):
        picker = FilePicker()
        self.file_list = picker.get_file_list()

    def get_excel_dto(self):
        for i in self.file_list:
            ws = self.excelapp.open_workbook(i)
            try:
                self.dto = ExcelSheetDTO(ws)
            except AttributeError as e:
                type_, value, traceback_ = sys.exc_info()
                print(traceback.format_exception(type_, value, traceback_))
                self.excelapp.close()
                quit()
            else:
                self.item_shelf.append(self.dto)
            self.excelapp.close_app_wb()
        self.excelapp.close_app()
        return self.item_shelf

    def close_app(self):
        self.excelapp.close_app()



class DTO():
    def __init__(self):
        self.file_shelf = ItemShelf()
        self.exapp = ExcelFile()
        self.dto = None

    def get_filepath_itr(self):
        picker = FilePicker()
        filelist = picker.get_file_list()
        for item in filelist:
            self.file_shelf.append(item)

    def change_dir(self,filename):
        currentdir=pathlib.Path(filename).parent
        new_dir=currentdir / "import済"
        shutil.move(filename,new_dir)

    def get_dto(self,filepath):
        ws = self.exapp.open_workbook(filepath)
        try:
            self.dto = ExcelSheetDTO(ws)
        except Exception as e:
            print(e)

    # def ws_open(self,filepath):
    #     # tmp = pathlib.Path(self.logbase)
    #     # log_file = tmp / "execute_log.txt"
    #     # basename = pathlib.Path(filepath).name
    #     try:
    #         self.ws = self.excelapp.open_workbook(filepath)
    #     except Exception as e:
    #         type_, value, traceback_ = sys.exc_info()
    #         print(traceback.format_exception(type_, value, traceback_))
    #         # self.intext = str(basename) + ": read NG : " + str(traceback.format_exception(type_, value, traceback_)) + \
    #         #               "\n"
    #         raise
    #     else:
    #         # self.intext = str(basename) + ": read OK\n"
    #         self.close_app_wb()
    #     # finally:
    #         # with open(log_file,"a",encoding="utf-8") as f:
    #         #     f.write(self.intext)



if __name__ == "__main__":
    dto = DTO()
    dto.get_filepath_itr()
    it = dto.file_shelf.iterator()
    while it.hasnext():
        item = it.next()
        print(item)
