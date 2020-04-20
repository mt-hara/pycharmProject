import sys
import traceback

from iterators.ItemIterator import *
from selectfiledir.filepicker import GetFile
from excelapp.ExcelApp import ExcelApp, ExcelWorkBook
from dto.ExcelSheetDTO import ExcelSheetDTO
from dao.TableDAO.QueryContext import ExecuteQuery
from functions.StopWatch import stop_watch


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
        self.dto = None

    def open_excelapp(self):
        self.baseapp = ExcelFile()

    # @stop_watch
    def open_wb(self, filepath):
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
            ws = self.excelapp.open_wb(i)
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

