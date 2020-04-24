from selectfiledir.filepicker import GetFile
from excelapp.ExcelApp import ExcelApp
from excelapp.ExcelApp import ExcelWorkBook


class FilePicker():
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

    def close_workbook(self):
        self.wb.close_workbook()

    def close_baseapp(self):
        self.base_app.close_App()

    def close(self):
        self.close_workbook()
        self.close_baseapp()