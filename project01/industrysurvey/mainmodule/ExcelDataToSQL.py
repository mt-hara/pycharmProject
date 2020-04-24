import sys
import traceback
import pathlib
import shutil
from selectfiledir.filepicker import GetFile
from excelapp.ExcelApp import ExcelApp, ExcelWorkBook
from iterators.ItemIterator import *
from dto.ExcelSheetDTO import ExcelSheetDTO
from mainmodule.CreateDTO import ExcelDataToDTO
from dao.TableDAO.QueryContext import ExecuteQuery
from functions.StopWatch import stop_watch
# import LogModule.logging_config
# import logging

# log = logging.getLogger(__name__)

class FilePicler():
    def __init__(self):
        self.__def_dir = "DeskTop"
        self.__ftype = [("Excel2003ファイル", "*.xlsx")]
        self.picker = GetFile(self.__def_dir, self.__ftype)
        self.file_list = self.picker.get_files()

    def get_file_list(self):
        if self.file_list is False:
            return False
        else:
            return self.file_list


class ExcelFile():
    def __init__(self):
        self.base_app = ExcelApp()
        self.app = self.base_app.app
        self.wb = ExcelWorkBook()
        self.ws = None

    def open_workbook(self, filepath):
        self.wb.open_wb(self.app, filepath)
        self.ws = self.wb.xlws
        return self.ws

    def close_wb(self):
        self.wb.close_workbook()

    def close_baseapp(self):
        self.base_app.close_App()

    def close(self):
        self.close_wb()
        self.close_baseapp()


class ExcelToSQL():
    def __init__(self):
        self.file_shelf = ItemShelf()
        self.dto_shelf = ItemShelf()
        self.filepath = ""
        self.excelapp = ExcelFile()
        self.base_name = ""
        self.customercd = ""
        self.dto = None
        self.ws = None

    def get_filepath_itr(self):
        picker = FilePicler()
        file_list = picker.get_file_list()
        if file_list is False:
            self.excelapp.close_baseapp()
            quit()
        else:
            for item in file_list:
                self.file_shelf.append(item)


    def change_dir(self, filepath, new_dir_name):
        current_dir = pathlib.Path(filepath).parent
        new_dir_path = current_dir / new_dir_name
        pathlib.Path(new_dir_path).mkdir(exist_ok=True)
        shutil.move(filepath, new_dir_path)


    def ws_open(self):
        file_itr = self.file_shelf.iterator()
        i = 0
        max=file_itr.get_length()
        while file_itr.hasnext():
            i = i + 1
            filepath = file_itr.next()
            try:
                self.ws = self.excelapp.open_workbook(filepath)
            except Exception as e:
                print(e)
            else:
                self.get_dto()


    def get_dto(self):
        try:
            self.dto = ExcelSheetDTO(self.ws)
        except AttributeError as e:
            self.excelapp.close_wb()
            raise
        else:
            self.customercd = self.dto.xlCustomerCd
            self.dto_shelf.append(self.dto)
            self.excelapp.close_wb()



    def close_wb(self):
        self.excelapp.close_wb()

    def close_baseapp(self):
        self.excelapp.close_baseapp()

@stop_watch
def main():
    tosql = ExcelToSQL()
    tosql.get_filepath_itr()
    tosql.ws_open()
    it = tosql.dto_shelf.iterator()
    while it.hasnext():
        item = it.next()
        print(item)
    tosql.close_baseapp()

    # it = tosql.file_shelf.iterator()
    # i = 0
    # max = it.get_length()
    # while it.hasnext():
    #     i = i + 1
    #     item = it.next()
    #     # files = tosql.ws_open(item)
    #     # print("{}/{} {:.1%}".format(i, max, i/max))
    # tosql.close_baseapp()


    # data_dato = ExcelDataToDTO()
    # filelists = data_dato.file_list
    # for i in filelists:
    #     print(i)
    # data_dato.get_excel_dto()
    # it = data_dato.item_shelf.iterator()
    # i = 0
    # while it.hasnext():
    #     i +=1
    #     item=it.next()
    #     print("{}: {}: {}".format(i, item.xlCustomerCd,item.xlCustomerName))
    # print("end")

if __name__ == "__main__":
    main()

    # class FilePicker():
#     def __init__(self):
#         self.__def_dir = "DeskTop"
#         self.__ftype =  [("Excel2003ファイル", "*.xlsx")]
#         self.picker = GetFile(self.__def_dir, self.__ftype)
#         self.file_list = self.picker.get_files()
#
#     def get_file_list(self):
#         if self.file_list is False:
#             quit()
#         else :
#             return self.file_list
#
# class ExcelFile():
#     def __init__(self):
#         self.baseapp = ExcelApp()
#         self.app = self.baseapp.app
#         self.wb = ExcelWorkBook()
#         self.ws = None
#         self.dto = None
#
#     def close_app_wb(self):
#         self.wb.close_workbook()
#
#     def close_app(self):
#         self.app.quit()
#
#     def close_baseapp(self):
#         self.baseapp.close_App()
#
#     def close(self):
#         self.close_app_wb()
#         self.close_baseapp()
#
#     def open_wb(self, filepath):
#         self.wb.open_wb(self.app, filepath)
#         self.ws = self.wb.xlws
#         return self.ws
#
#     # def get_dto(self):
#     #     try:
#     #         self.dto = ExcelSheetDTO(self.ws)
#     #     except AttributeError as e:
#     #         type_, value, traceback_ = sys.exc_info()
#     #         print(traceback.format_exception(type_, value, traceback_))
#     #         self.close()
#     #         quit()
#     #     else:
#     #         return self.dto
#
#
# class Dto():
#     def __init__(self):
#         self.file_list = []
#         self.get_file_list()
#         self.excelapp=ExcelFile()
#         self.item_shelf = ItemShelf()
#         self.dto = None
#
#
#     def get_file_list(self):
#         picker = FilePicker()
#         self.file_list = picker.get_file_list()
#
#     def get_excel_dto(self):
#         for i in self.file_list:
#             ws = self.excelapp.open_wb(i)
#             try:
#                 self.dto = ExcelSheetDTO(ws)
#             except AttributeError as e:
#                 type_, value, traceback_ = sys.exc_info()
#                 print(traceback.format_exception(type_, value, traceback_))
#                 self.excelapp.close()
#                 quit()
#             else:
#                 self.item_shelf.append(self.dto)
#             self.excelapp.close_app_wb()
#         self.excelapp.close_app()
#         return self.item_shelf






    # data_dato.close_app()

    # dtoinst = Dto()
    # te = dtoinst.get_excel_dto()
    # it = dtoinst.item_shelf.iterator()
    # i = 0
    # while it.hasnext():
    #     i +=1
    #     item=it.next()
    #     print("{}: {}: {}".format(i, item.xlCustomerCd,item.xlCustomerName))
    # print("end")
