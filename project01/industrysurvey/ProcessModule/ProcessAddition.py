import sys
import os
import traceback
from concurrent.futures.process import ProcessPoolExecutor
from multiprocessing import Pool
import multiprocessing as multi
from mainmodule.CreateDTO import FilePicker, ExcelFile
from dto.ExcelSheetDTO import ExcelSheetDTO
from iterators.ItemIterator import *
from functions.StopWatch import stop_watch

class DataToDTO():
    def __init__(self):
        # self.file_list = []
        self.exapp = ExcelFile()
        self.app = self.exapp.app
        self.item_shelf = ItemShelf()
        self.dto = None



    def get_excel_dto(self, filepath):
        ws = self.exapp.open_wb(filepath)
        dto = ExcelSheetDTO(ws)
        return dto
        # self.item_shelf.append(dto)
        # self.exapp.close_app_wb()



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
    # picker = FilePicker()
    # pickerlist = list(picker.file_list)
    dto = DataToDTO()
    ls = dto.test_code(pickerlist)
    print(ls)
    print("end")
    # for i in pickerlist:
    #     print(i)



    # calc = Calc()
    # args = list(range(1000))
    # print(calc.calc_square_usemulti(args))
    #
    # print(calc.calc_usemulti(args))


if __name__ == "__main__":
    main()