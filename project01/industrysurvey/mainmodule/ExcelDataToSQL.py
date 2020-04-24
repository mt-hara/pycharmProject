import sys
import traceback
import pathlib
import shutil
from selectfiledir.filepicker import GetFile
from excelapp.ExcelApp import ExcelApp, ExcelWorkBook
from iterators.ItemIterator import *
from dto.ExcelSheetDTO import ExcelSheetDTO
from mainmodule.CreateDTO import ExcelDataToDTO
from dao.TableDAO.QueryContext import ExecuteQueryAll
from functions.StopWatch import stop_watch

# import LogModule.logging_config
# import logging

# log = logging.getLogger(__name__)

# ログデータ保存先ディレクトリパス

_log_dir = "C:\\workspace\\pycharmProject\\project01\\industrysurvey\\LogData"


def write_log_data(logfile_path, log_data):
    with open(logfile_path, "a", encoding="utf-8") as f:
        f.write("\n{}".format(log_data))


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


class ExcelDataToSQL():
    def __init__(self):
        self.file_shelf = ItemShelf()
        self.filepath = ""
        self.excelapp = ExcelFile()
        self.basename = ""
        self.customercd = ""
        self.customername = ""
        self.dto = None
        self.ws = None

    def close_wb(self):
        self.excelapp.close_workbook()

    def close_baseapp(self):
        self.excelapp.close_baseapp()

    def get_file_itr(self):
        picker = FilePicker()
        file_list = picker.get_file_list()
        if file_list is False:
            self.close_baseapp()
            quit()
        else:
            for item in file_list:
                self.file_shelf.append(item)
            return self.file_shelf

    def open_ws(self,filepath):
        self.basename = pathlib.Path(filepath).name
        self.filepath = filepath




@stop_watch
def main():
    todto = ExcelDataToSQL()
    todto.get_file_itr()

    # filedata = ExcelDataToSQL()
    # filedata.open_wb()



if __name__ == "__main__":
    main()
