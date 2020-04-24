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
        self.pick_file()
        self.get_file_itr()

    def pick_file(self):
        picker = FilePicker()
        picked_list = picker.get_file_list()
        if picked_list is False:
            quit()
        else:
            self.file_list = picked_list
            return self.file_list

    def get_file_itr(self):
        if len(self.file_list) == 0:
            quit()
        for files in self.file_list:
            self.file_shelf.append(files)

        return self.file_shelf


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


def write_log_data(logfile_path, log_data):
    with open(logfile_path, "a", encoding="utf-8") as f:
        f.write("\n{}".format(log_data))


class ExcelDataToSQL():
    def __init__(self):
        self.files_inst = FilePathList()
        self.__get_fileitr()
        self.full_filepath = ""
        self.base_name = ""
        self.excelapp = ExcelFile()
        self.wb = self.excelapp.wb
        self.ws = None

    def __get_fileitr(self):
        self.file_itr = self.files_inst.file_shelf

    def open_wb(self):
        __log_data = ""
        _log_file = pathlib.Path(_log_dir) / "execute_log.log"
        item = self.file_itr.iterator()
        while item.hasnext():
            files = item.next()
            self.full_filepath = files
            self.base_name = pathlib.Path(files).name
            try:
                self.ws = self.excelapp.open_workbook(files)
            except Exception as e:
                __log_data = "Error OpenFile:{}".format(self.base_name)
            else:
                __log_data = "Success OpenFile:{}".format(self.base_name)
                self.get_dto()
            finally:
                write_log_data(_log_file, __log_data)

    def get_dto(self):
        pass


@stop_watch
def main():
    filedata = ExcelDataToSQL()
    filedata.open_wb()
    # files = FilePathList()
    # it = files.file_shelf.iterator()
    # while it.hasnext():
    #     item = it.next()
    #     print(item)

    # ex = ExcelDataToSQL(listmaker.file_list)
    # lists = ex.file_list
    # for i in lists:
    #     print(i)


if __name__ == "__main__":
    main()
