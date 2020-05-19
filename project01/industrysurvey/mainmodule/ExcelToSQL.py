import pathlib
import shutil
from iterators.ItemIterator import *
from selectfiledir.filepicker import GetFile
from excelapp.ExcelApp import ExcelApp, ExcelWorkBook
from dto.ExcelSheetDTO import ExcelSheetDTO
from dao.TableDAO.QueryContext import ExecuteQuery
from functions.StopWatch import stop_watch

_log_file = "C:\\workspace\\pycharmProject\\project01\\industrysurvey\\LogData\\import_log.log"


# 一覧データ作成プログラムVer2

class FilePicker():
    def __init__(self):
        self.__def_dir = "DeskTop"
        self.__ftype = [("Excel2007ファイル", "*.xlsx"), ("Excel2007ファイル", "*.xls")]
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


class ExcelToDto():
    def __init__(self):
        self.file_shelf = ItemShelf()
        self.filepath = ""
        self.excelapp = ExcelFile()
        self.ws = None
        self.basename = ""
        self.dto_shelf = ItemShelf()

    def ws_open(self, filepath):
        self.basename = pathlib.Path(filepath).name
        self.filepath = filepath

        try:
            self.ws = self.excelapp.open_workbook(self.filepath)
        except Exception as e:
            self.__file_open_log = "File Open Error..." + str(self.basename)
            with open(_log_file, "a", encoding="utf-8") as f:
                f.write("\n" + self.__file_open_log)
            raise
        else:
            self.get_dto()

    def get_dto(self):
        try:
            dto = ExcelSheetDTO(self.ws)
        except Exception as e:
            self.__get_dto_log = "Get Dto Error..." + str(self.basename)
            with open(_log_file,"a", encoding="utf-8") as f:
                f.write("\n" + self.__get_dto_log)
            raise
        else:
            self.dto_shelf.append(dto)



    def execute_quety(self,dto):
        customerCd = dto.xlCustomerCd
        customername = dto.xlCustomerName
        try:
            query = ExecuteQuery(dto)
            query.execute()
        except Exception as e:
            self.__query_log = "Query Error..." + str(customerCd) + str(customername)
            with open(_log_file, "a", encoding="utf-8") as f:
                f.write("\n" + self.__query_log)
        else:
            pass


    def get_files_itr(self):
        picker = FilePicker()
        file_list = picker.get_file_list()
        for item in file_list:
            self.file_shelf.append(item)

    def close_app_wb(self):
        self.excelapp.close_app_wb()

    def close_baseApp(self):
        self.excelapp.close_baseapp()


@stop_watch
def main():
    etd = ExcelToDto()
    etd.get_files_itr()
    itr = etd.file_shelf.iterator()
    i = 0
    j = 0

    while itr.hasnext():
        item = itr.next()
        files = etd.ws_open(item)

    dtoitr = etd.dto_shelf.iterator()
    while dtoitr.hasnext():
        item = dtoitr.next()
        dto = etd.execute_quety(item)

    etd.close_baseApp()


if __name__ == "__main__":
    main()