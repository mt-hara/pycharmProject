import sys
import os
import traceback
from concurrent.futures.process import ProcessPoolExecutor
from multiprocessing import Pool
import multiprocessing as multi
# from mainmodule.CreateDTO import FilePicker, ExcelFile
from excelapp.ExcelApp import ExcelApp, ExcelWorkBook
from dto.ExcelSheetDTO import ExcelSheetDTO
from iterators.ItemIterator import *
from functions.StopWatch import stop_watch
from selectfiledir.filepicker import GetFile

class Excels():
    def __init__(self):
        self.__def_dir = "DeskTop"
        self.__ftype = [("Excel2007ファイル", "*.xlsx")]
        self.picker = GetFile(self.__def_dir, self.__ftype)
        self.file_list = self.get_file_list()
        self.baseapp = ExcelApp()
        self.app = self.baseapp.app
        self.wb = ExcelWorkBook()
        self.item_shelf = ItemShelf()
        self.ws = None
        self.dto = None

    def get_file_list(self):
        result = self.picker.get_files()
        if result is False:
            quit()
        else:
            self.file_list = list(result)

    def open_wb(self, filepath):
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


    def get_multi_dto(self, lists):
        n_cores = multi.cpu_count()
        with ProcessPoolExecutor(max_workers=n_cores) as executor:
            result = executor.map(self.get_excel_dto, lists)
            self.item_shelf.append(result)


    def test_code(self, lists):
        with Pool(4) as p:
            ret = p.map(self.get_excel_dto, lists)
            self.item_shelf.append(ret)

        # n_coores = multi.cpu_count()
        # p= Pool(n_coores)
        # res = p.map(self.get_excel_dto, lists)
        # return res

# class Calc:
#     def square(self, n):
#         return n * n
#
#     @stop_watch
#     def nomal_calc(self,args):
#         ls = []
#         for i in args:
#             ls.append(self.square(i))
#         return ls
#
#     @stop_watch
#     def calc_square_usemulti(self, args):
#         n_cores = multi.cpu_count()
#         p = Pool(n_cores)
#         res = p.map(self.square, args)
#         return res
#
#     @stop_watch
#     def calc_usemulti(self,args):
#         n_cores = multi.cpu_count()
#         with ProcessPoolExecutor(max_workers=n_cores) as executor:
#             params =executor.map(self.square, args)
#         return params


def main():
    pickerlist =["C://Users//m-hara//Desktop//取引先コード取得済//業態調査票（（株）清和光学製作所）.xlsx",
        "C://Users//m-hara//Desktop//取引先コード取得済//業態調査票（ＮＣＤ NakajimaControlDesign）.xlsx",
"C://Users//m-hara//Desktop//取引先コード取得済//業態調査票（イヌイ株式会社）.xlsx",
# "C://Users//m-hara//Desktop//取引先コード取得済//業態調査票（スペクトラ・フィジックス株式会社）.xlsx",
# "C://Users//m-hara//Desktop//取引先コード取得済//業態調査票（トルク精密工業株式会社）.xlsx",
# "C://Users//m-hara//Desktop//取引先コード取得済//業態調査票（株式会社SCREENクリエイティブコミュニケーションズ）.xlsx",
# "C://Users//m-hara//Desktop//取引先コード取得済//業態調査票（株式会社テクノフォームジャパン）.xlsx",
"C://Users//m-hara//Desktop//取引先コード取得済//業態調査票（株式会社ヤハタ）.xlsx"
]

    Excels()
    # picker = FilePicker()
    # pickerlist = list(picker.file_list)
    # dto = DataToDTO()
    # ls = dto.test_code(pickerlist)
    # print(ls)
    # print("end")
    # for i in pickerlist:
    #     print(i)



    # calc = Calc()
    # args = list(range(1000))
    # print(calc.calc_square_usemulti(args))
    #
    # print(calc.calc_usemulti(args))


if __name__ == "__main__":
    main()