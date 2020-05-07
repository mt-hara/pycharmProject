import pathlib
import shutil
from selectfiledir.filepicker import GetFile
from excelapp.ExcelApp import ExcelApp, ExcelWorkBook
from iterators.ItemIterator import *
from dto.ExcelSheetDTO import ExcelSheetDTO
from mainmodule.CreateDTO import ExcelDataToDTO
from dao.TableDAO.QueryContext import ExecuteQuery, ExecuteQueryAll
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
        self.__ftype = [("Excel2007ファイル", "*.xlsx")]
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
        # self.file_list = ""
        self.filepath = ""
        self.excelapp = ExcelFile()
        self.basename = ""
        self.customercd = ""
        self.customername = ""
        self.dto = None
        self.ws = None

    def change_dir(self, filepath, new_dir_name):
        current_dir = pathlib.Path(filepath).parent
        new_dir_path = current_dir / new_dir_name
        pathlib.Path(new_dir_path).mkdir(exist_ok=True)
        shutil.move(filepath, new_dir_path)

    def close_wb(self):
        self.excelapp.close_workbook()

    def close_baseapp(self):
        self.excelapp.close_baseapp()

    def get_filepath_itr(self):
        picker = FilePicker()
        file_list = picker.get_file_list()
        if file_list is False:
            self.close_baseapp()
            quit()
        else:
            for item in file_list:
                self.file_shelf.append(item)
            return self.file_shelf

    def open_ws(self, filepath):
        self.basename = pathlib.Path(filepath).name
        self.filepath = filepath
        _log_file = pathlib.Path(_log_dir) / "fileopen_log.log"
        _log_data = ""
        try:
            self.ws = self.excelapp.open_workbook(self.filepath)
        except Exception as e:
            _log_data = "Error:{}".format(self.basename)
            # raise
        else:
            _log_data = "Success:{}".format(self.basename)
            self.get_dto()
        finally:
            write_log_data(_log_file, _log_data)

    def get_dto(self):
        _log_file = pathlib.Path(_log_dir) / "getdto_log.log"
        _log_data = ""
        try:
            self.dto = ExcelSheetDTO(self.ws)
        except AttributeError as e:
            _log_data = "Error:{}".format(self.basename)
            self.close_wb()
        else:
            self.customercd = self.dto.xlCustomerCd
            self.customername = self.dto.xlCustomerName
            _log_data = "Success:{}:{}".format(self.customercd, self.customername)
            self.close_wb()
            self.execute_query_all()
        finally:
            write_log_data(_log_file, _log_data)
            # self.close_wb()

    def execute_query(self):
        _log_file = pathlib.Path(_log_dir) / "query_log.log"
        _log_data = ""
        try:
            query = ExecuteQuery(self.dto)
            query.execute()
        except Exception as e:
            _log_data = "Error:{}:{}".format(self.customercd, self.customername)
        else:
            _log_data = "Success:{}:{}".format(self.customercd, self.customername)
            self.change_dir(self.filepath, "import済")
        finally:
            write_log_data(_log_file, _log_data)

    def execute_query_all(self):
        _log_file = pathlib.Path(_log_dir) / "query_log.log"
        _log_data = ""
        try:
            query = ExecuteQueryAll(self.dto)
            query.execute()
        except Exception as e:
            _log_data = "Error:{}:{}".format(self.customercd, self.customername)
        else:
            _log_data = "Success:{}:{}".format(self.customercd, self.customername)
            self.change_dir(self.filepath, "import済")
        finally:
            write_log_data(_log_file, _log_data)

@stop_watch
def main():
    todto = ExcelDataToSQL()
    todto.get_filepath_itr()
    itr = todto.file_shelf.iterator()
    cnt = 0
    max = itr.get_length()
    while itr.hasnext():
        cnt = cnt + 1
        item = itr.next()
        files = todto.open_ws(item)
        print("{}/{} {:.1%}".format(cnt, max, cnt / max))

    todto.close_baseapp()


if __name__ == "__main__":
    main()
