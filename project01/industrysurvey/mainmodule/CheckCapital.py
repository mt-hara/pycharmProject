import pathlib
import shutil
import tkinter as tk
from tkinter import messagebox as msgbox
from iterators.ItemIterator import *
from selectfiledir.ConcFilePicker import FilePicker
from excelapp.ConcExcelFile import ExcelFiles
from dto.CapitalUnitDTO import CaputalUnit
from functions.StopWatch import stop_watch


class CheckUnit():
    def __init__(self):
        self.file_shelf = ItemShelf()
        self.filepath = ""
        self.excelapp = ExcelFiles()
        self.wb = None
        self.ws = None
        self.ex_dto = None
        self.dto_itr= ItemShelf()

    # def open_excel(self):
    #     self.excelapp = ExcelFiles()
    #     self.wb= self.excelapp.wb

    def open_ws(self, filepath):
        self.ws = self.excelapp.open_workbook(filepath)

    def get_dto(self):
        self.ex_dto = CaputalUnit(self.ws)
        self.dto_itr.append(self.ex_dto)
        self.close_app_wb()

    def close_app_wb(self):
        self.excelapp.close_app_wb()

    def close_baseApp(self):
        self.excelapp.close_baseapp()

    def get_filepath_itr(self):
        picker = FilePicker()
        file_list = picker.get_file_list()
        for item in file_list:
            self.file_shelf.append(item)



@stop_watch
def main():
    root = tk.Tk()
    root.withdraw()

    checker = CheckUnit()
    checker.get_filepath_itr()
    itr = checker.file_shelf.iterator()
    i = 0
    max = itr.get_length()
    while itr.hasnext():
        i = i + 1
        item = itr.next()
        file = checker.open_ws(item)
        checker.get_dto()
        print("{}/{} {:.1%}".format(i,max,i/max))

    checker.close_baseApp()

    j=0
    dto_itr= checker.dto_itr.iterator()
    max2 = dto_itr.get_length()
    while dto_itr.hasnext():
        j=j + 1
        dto = dto_itr.next()
        cd = dto.xlCustomerCd
        cname = dto.xlCustomerName
        capital =dto.xlCustomerCapital
        capitalnuit = dto.xlCapitalUnit

        print("{},{},{}  {},{},({:.1%})".format(cd,cname,capitalnuit,j,max2,j/max2))

if __name__ == "__main__":
    main()
