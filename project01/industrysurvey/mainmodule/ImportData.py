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


_log_dir= "C:\\workspace\\pycharmProject\\project01\\industrysurvey\\LogData"

# 一覧データ作成ベースプログラム

class FilePicker():
    def __init__(self):
        self.__def_dir = "DeskTop"
        self.__ftype = [("Excel2007ファイル", "*.xlsx"),("Excel2007ファイル", "*.xls")]
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

class ImportExcelData():
    def __init__(self):
        self.file_shelf = ItemShelf()
        self.filepath = ""
        self.excelapp = ExcelFile()
        self.basename = ""
        self.customercd = ""
        self.dto = None
        self.ws = None

    # def change_dir(self, filepath):
    #     currentdir = pathlib.Path(filepath).parent
    #     new_dir = currentdir / "import済"
    #     shutil.move(filepath, new_dir)

    def change_dir(self, filepath, new_dir_name):
        current_dir = pathlib.Path(filepath).parent
        new_dir_path = current_dir / new_dir_name
        pathlib.Path(new_dir_path).mkdir(exist_ok=True)
        shutil.move(filepath, new_dir_path)



    def ws_open(self,filepath):
        self.basename = pathlib.Path(filepath).name
        self.filepath = filepath
        _log_file = pathlib.Path(_log_dir) / "file_open.log"
        try:
            self.ws = self.excelapp.open_workbook(self.filepath)
        except Exception as e:
            self.__file_open_log = "Error...File_Open:" + str(self.basename)
            raise
        else:
            self.__file_open_log= "Success...File_Open:" + str(self.basename)
            # self.excelapp.close_app_wb()
            self.get_dto()

        finally:
            with open(_log_file, "a", encoding="utf-8") as f:
                f.write("\n" + self.__file_open_log)


    def get_dto(self):
        _log_file = pathlib.Path(_log_dir) / "dto_log.log"
        try:
            self.dto = ExcelSheetDTO(self.ws)
        except AttributeError as e:
            self.__dto_log = "Error...GetDTO:" + str(self.basename)
            raise
        else:
            self.customercd =self.dto.xlCustomerCd
            self.excelapp.close_app_wb()
            self.execute_query()
            self.__dto_log = "Success...GetDTO:" + str(self.basename)

        finally:
            # self.excelapp.close_app_wb()
            with open(_log_file, "a", encoding="utf-8") as f:
                f.write("\n" + self.__dto_log)

    def execute_query(self):
        _log_file = pathlib.Path(_log_dir) / "query_log.log"
        try:
            query = ExecuteQuery(self.dto)
            query.execute()
        except Exception as e:
            self.__query_log = "Error...Query:" +str(self.customercd) + "," + str(self.basename)

        else:
            self.__query_log = "Success...Query:" +str(self.customercd) + "," + str(self.basename)
            self.change_dir(self.filepath,"import済")
        finally:
            with open(_log_file, "a", encoding="utf-8") as f:
                f.write("\n" + self.__query_log)

    def close_app_wb(self):
        self.excelapp.close_app_wb()

    def close_baseAapp(self):
        self.excelapp.close_baseapp()

    def get_filepath_itr(self):
        picker = FilePicker()
        file_list = picker.get_file_list()
        for item in file_list:
            self.file_shelf.append(item)

@stop_watch
def main():
    ida = ImportExcelData()
    ida.get_filepath_itr()
    it = ida.file_shelf.iterator()
    i = 0
    max = it.get_length()
    while it.hasnext():
        i = i + 1
        item = it.next()
        files = ida.ws_open(item)
        print("{}/{} {:.1%}".format(i,max,i/max))
    ida.close_baseAapp()

if __name__ == "__main__":
    main()
