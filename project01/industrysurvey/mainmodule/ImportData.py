import sys
import traceback
import pathlib
import shutil
from iterators.ItemIterator import *
from selectfiledir.filepicker import GetFile
from excelapp.ExcelApp import ExcelApp, ExcelWorkBook
from dto.ExcelSheetDTO import ExcelSheetDTO
from dao.TableDAO.QueryContext import ExecuteQuery

class FilePicker():
    def __init__(self):
        self.__def_dir = "DeskTop"
        self.__ftype = [("Excel2007ファイル", "*.xlsx")]
        self.picker = GetFile(self.__def_dir, self.__ftype)
        self.file_list = self.picker.get_files()

    def get_file_list(self):
        if self.file_list is False:
            quit()
        else:
            return self.file_list


class ExcelFile():
    def __init__(self):
        self.baseapp = ExcelApp()
        self.app = self.baseapp.app
        self.wb = ExcelWorkBook()
        self.ws = None
        # self.dto = None

    # def get_excelapp(self):
    #     self.baseapp = ExcelApp()

    def open_workbook(self, filepath):
        self.wb.open_wb(self.app, filepath)
        self.ws = self.wb.xlws
        return self.ws

    def close_app_wb(self):
        self.wb.close_workbook()

    def close_baseapp(self):
        self.baseapp.close_App()

    def close(self):
        self.close_app_wb()
        self.close_baseapp()

class ImportExcelData():
    def __init__(self):
        self.file_shelf = ItemShelf()
        self.excelapp = ExcelFile()
        self.dto = None

    def get_filepath_itr(self):
        picker = FilePicker()
        file_list = picker.get_file_list()
        for item in file_list:
            self.file_shelf.append(item)

    def change_dir(self, filepath):
        currentdir = pathlib.Path(filepath).parent
        new_dir = currentdir / "import済"
        shutil.move(filepath, new_dir)

    def get_excel_dto(self, filepath):
        ws = self.excelapp.open_workbook(filepath)
        try:
            xldto = ExcelSheetDTO(ws)
        except AttributeError as e:
            type_, value, traceback_ = sys.exc_info()
            print(traceback.format_exception(type_, value, traceback_))
            self.excelapp.close()
            basename=pathlib.Path(filepath).name
            self.indata= str(basename) + " : GetDto False"
            return False
        else:
            basename=pathlib.Path(filepath).name
            indata= str(basename) + " : GetDto success"
            return xldto
        finally:
            with open("execute_log.txt", "a", encoding="utf-8") as f:
                f.write(self.indata)

    def import_data(self, xldto):
        exe_query= ExecuteQuery(xldto)
        try:
            exe_query.execute()
        except:
            pass

if __name__ == "__main__":
    ida = ImportExcelData()
    ida.get_filepath_itr()
    it = ida.file_shelf.iterator()
    while it.hasnext():
        item = it.next()
        dto = ida.get_excel_dto(item)
        if dto is False:
            print("error")
            continue
        else:
            print("ok")
