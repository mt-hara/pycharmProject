import sys
import os
import traceback
import time
from pathlib import Path
from concurrent.futures.process import ProcessPoolExecutor
from multiprocessing import Pool
import multiprocessing as multi
from excelapp.ExcelApp import ExcelApp, ExcelWorkBook
from dto.ExcelSheetDTO import ExcelSheetDTO
from iterators.ItemIterator import *
from functions.StopWatch import stop_watch
from selectfiledir.filepicker import GetFile


class DTO():
    def __init__(self):
        self.__def_dir = "DeskTop"
        self.__ftype = [("Excel2003ファイル", "*.xlsx")]
        self.picker = GetFile(self.__def_dir, self.__ftype)
        self.file_list = self.get_file_list()
        self.item_shelf = ItemShelf()
        # self.baseapp = None
        # self.app = None
        # self.wb = None
        # self.ws =None

    def open_baseapp(self):
        self.baseapp = ExcelApp()
        self.app = self.baseapp.app
        self.wb = ExcelWorkBook()

    def open_workbook(self, filepath):
        self.wb.open_wb(self.app, filepath)
        self.ws = self.wb.xlws
        return self.ws

    def close_app_wb(self):
        self.wb.close_workbook()

    def close_app(self):
       self.app.quit()

    def close_baseapp(self):
        self.baseapp.close_App()

    def close(self):
        self.close_app_wb()
        self.close_baseapp()

    def get_file_list(self):
        lists = self.picker.get_files()
        if lists is False:
            quit()
        else:
            return lists

    def get_excel_dto(self, itemlist):
        self.open_baseapp()
        # for i in itemlist:
        self.ws = self.open_workbook(itemlist)
        self.dto = ExcelSheetDTO(self.ws)
        # self.dto = ExcelSheetDTO(self.ws)
        # self.close_app_wb()
        # self.close_app()
        # self.item_shelf.append(self.dto)
        return self.dto

    def multi_get(self, itemlist):
        # print(type(itemlist))
        # for i in itemlist:
        #     print(i)

        cores = multi.cpu_count()
        # with ProcessPoolExecutor(max_workers=cores) as pool:
        #     res = list(pool.map(self.get_excel_dto, itemlist))
        # return res
        P = Pool(cores)
        res = P.map(self.get_excel_dto, itemlist)
        for i in res:
            print(i)
        # print(res)
    # @stop_watch
    # def multi(self, args):
    #     print("multi")
    #     n_cores = multi.cpu_count()
    #     P = Pool(n_cores)
    #     res = P.map(self.multi_dto, args)
    #     return  res

class Calc:
    def square(self, n):
        return n * n

    @stop_watch
    def nomal_calc(self,args):
        ls = []
        for i in args:
            ls.append(self.square(i))
        return ls

    @stop_watch
    def calc_square_usemulti(self, args):
        n_cores = multi.cpu_count()
        p = Pool(n_cores)
        res = p.map(self.square, args)
        return res

    @stop_watch
    def calc_usemulti(self,args):
        n_cores = multi.cpu_count()
        with ProcessPoolExecutor(max_workers=n_cores) as executor:
            params =executor.map(self.square, args)
        return params


def main():
    pickerlist =["C://Users//m-hara//Desktop//取引先コード取得済//業態調査票（（株）清和光学製作所）.xlsx",
        "C://Users//m-hara//Desktop//取引先コード取得済//業態調査票（ＮＣＤ NakajimaControlDesign）.xlsx",
"C://Users//m-hara//Desktop//取引先コード取得済//業態調査票（イヌイ株式会社）.xlsx",
"C://Users//m-hara//Desktop//取引先コード取得済//業態調査票（スペクトラ・フィジックス株式会社）.xlsx",
"C://Users//m-hara//Desktop//取引先コード取得済//業態調査票（トルク精密工業株式会社）.xlsx",
"C://Users//m-hara//Desktop//取引先コード取得済//業態調査票（株式会社SCREENクリエイティブコミュニケーションズ）.xlsx",
"C://Users//m-hara//Desktop//取引先コード取得済//業態調査票（株式会社テクノフォームジャパン）.xlsx",
"C://Users//m-hara//Desktop//取引先コード取得済//業態調査票（株式会社ヤハタ）.xlsx"
]
    dto = DTO()
    itemlist = dto.file_list
    res = dto.multi_get(list(itemlist))
    print(type(res))
    # excls = ExcelDataToDTO()
    # excls.get_filepath_list()
    # args = excls.file_list
    # ls = excls.multi(args)
    # print(type(ls))
    # it = ls.item_shelf.iterator()
    # while it.hasnext():
    #     item=it.next()
    #     print(item.xlCustomerCd)



if __name__ == "__main__":
    main()