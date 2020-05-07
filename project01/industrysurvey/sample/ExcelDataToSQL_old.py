import sys
import traceback
import pathlib
import shutil

from mainmodule.FileFunction import FilePicker, ExcelFile
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


class FilePathList():
    def __init__(self):
        self.file_list = []
        self.file_shelf = ItemShelf()

    def get_filepath_list(self):
        picker = FilePicker()
        files = picker.get_file_list()
        if files is False:
            quit()
        else:
            self.file_list = files

    def set_file_itr(self):
        if len(self.file_list) == 0:
            quit()
        for files in self.file_list:
            self.file_shelf.append(files)


class ChangeDir():

    def __init__(self, filepath):
        self.__NEW_DIR_NAME = "import済"
        self.filepath = filepath
        self.__current_dir = pathlib.Path(self.filepath).parent
        self.__new_dir = self.__current_dir / self.__NEW_DIR_NAME

    def create_dir(self):
        pathlib.Path(self.__new_dir).mkdir(exist_ok=True)

    def move_file(self):
        shutil.move(self.filepath, self.__new_dir)


class ExcelDataToSQL():
    def __init__(self):
        pass


class ExcelDataToSQL_old():
    def __init__(self):
        self.__NEW_DIR_NAME = "import済"  # 処理終了後のファイル保存ディレクトリ名
        self.file_shelf =ItemShelf()
        self.file_list = []
        self.filepath = ""
        self.dto_shelf = ItemShelf()
        self.excelapp = ExcelFile()
        self.base_name = ""
        self.ws = None

    def change_dir(self, filepath):
        current_dir = pathlib.Path(filepath).parent
        new_dir_path = current_dir / self.__NEW_DIR_NAME
        pathlib.Path(new_dir_path).mkdir(exist_ok=True)
        shutil.move(filepath, new_dir_path)

    def write_log_data(self,logfile_path, log_data):
        with open(logfile_path, "a", encoding="utf-8") as f:
            f.write("\n{}".format(log_data))

    def get_filepath_list(self):
        picler = FilePicker()
        self.file_list = picler.get_file_list()
        if self.file_list is False:
            self.excelapp.close_baseapp()
            quit()
        else:
            return self.file_list

    def wb_open(self):
        __log_data = ""
        _log_file = pathlib.Path(_log_dir) / "fileopen_log.log"  # ログ出力先設定

        for i in self.file_list:
            self.base_name = pathlib.Path(i).name
            try:
                self.ws = self.excelapp.open_workbook(i)
            except Exception as e:
                __file_data = "Error:{}".format(self.base_name)
                continue
            else:
                __file_data = "Success:{}".format(self.base_name)
                self.set_dto_itr()
            finally:
                self.write_log_data(_log_file, __log_data)

    def set_dto_itr(self):
        __log_data = ""
        _log_file = pathlib.Path(_log_dir) / "dto_log.log"  # ログ出力先設定

        try:
            dto = ExcelSheetDTO(self.ws)
        except AttributeError as e:
            self.excelapp.close_workbook()
            __log_data = "Error:{}".format(self.base_name)
            raise
        else:
            self.dto_shelf.append(dto)
            __customercd = dto.xlCustomerCd
            self.excelapp.close_workbook()
            __log_data = "Success:{}:{}".format(__customercd ,self.base_name)
        finally:
            self.write_log_data(_log_file, __log_data)

    def execute_query(self,dto):
        __log_data = ""
        _log_file = pathlib.Path(_log_dir) / "query_log.log"  # ログ出力先設定

        __customercd = dto.xlCustomerCd
        __customername = dto.xlCustomerName

        try:
            query = ExecuteQueryAll(dto)
            query.execute()
        except Exception as e:
            __log_data = "Error:{}:{}".format(__customercd,__customername)
        else:
            __log_data = "Success:{}:{}".format(__customercd, __customername)
        finally:
            self.write_log_data(_log_file, __log_data)

    def close_wb(self):
        self.excelapp.close_workbook()

    def close_baseapp(self):
        self.excelapp.close_baseapp()


@stop_watch
def main():
    tosql = ExcelDataToSQL_old()
    tosql.get_filepath_list()
    tosql.wb_open()
    it = tosql.dto_shelf.iterator()
    while it.hasnext():
        item = it.next()
        print("{}:{}".format(item.xlCustomerCd,item.xlCustomerName))

    tosql.close_baseapp()



if __name__ == "__main__":
    main()

