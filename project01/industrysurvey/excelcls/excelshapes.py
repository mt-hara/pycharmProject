from typing import List
from dataclasses import dataclass, asdict
from abc import ABCMeta
from abc import abstractmethod


# @dataclass
# class ShapesDataClass:
#     biz_type: int = 0
#     capital_form: int = 0
#     corp_type: int = 0
#     stock_status: bool = False
#     stock_market: str = ""
#     iso9000: str = ""
#     iso14000: str =""


class ShapeDataDTO():
    def __init__(self,shapedata):
        self.shapesdto = shapedata
        self.shapes_list = None

    def get_shape_data(self, lists):
        self.shapes_list = lists
        for dict in self.shapes_list:
            t_pos = dict["top"]
            l_pos = dict["left"]
            if 210 < t_pos < 225:  # 業種分類
                if 80 < l_pos < 125:
                    self.shapesdto.biz_type = 1  # メーカー
                elif 145 < l_pos < 190:
                    self.shapesdto.biz_type = 2  # 商社
                elif 200 < l_pos < 285:
                    self.shapesdto.biz_type = 3  # メーカー＆商社
                elif 298 < l_pos < 350:
                    self.shapesdto.biz_type = 4  # 代理店
                elif 360 < l_pos < 400:
                    self.shapesdto.biz_type = 5  # 卸売
                elif 422 < l_pos < 445:
                    self.shapesdto.biz_type = 6  # その他
                else:
                    pass
            elif 222 < t_pos < 238:  # 資本形態
                if 80 < l_pos < 125:
                    self.shapesdto.capital_form = 1  # 個人
                else:
                    self.shapesdto.capital_form = 2  # 法人
                    # 法人の場合は会社形態を取得する
                    if 180 < l_pos < 235:
                        self.shapesdto.corp_type = 1  # 株式会社
                    elif 240 < l_pos < 290:
                        self.shapesdto.corp_type = 2  # 有限会社
                    elif 295 < l_pos < 400:
                        self.shapesdto.corp_type = 9  # その他
            elif 246 < t_pos < 256:  # 上場区分
                if 340 < l_pos < 410:
                    self.shapesdto.stock_status = 0  # 非上場
                else:
                    self.shapesdto.stock_status = 1  # 上場
                    # 上場の場合は上場市場を取得
                    if 80 < l_pos < 125:
                        self.shapesdto.stock_market = "東証1部"
                    elif 150 < l_pos < 190:
                        self.shapesdto.stock_market = "東証2部"
                    elif 210 < l_pos < 300:
                        self.shapesdto.stock_market = "その他"
            # ISO認認証取得区分
            elif 690 < t_pos < 717:  # ISO認証取得区分
                if 25.5 < l_pos < 100:
                    self.shapesdto.iso9000 = "取得済"
                elif 305 < l_pos < 390:
                    self.shapesdto.iso14000 = "取得済"
            elif 720 < t_pos < 731:
                if 25.5 < t_pos < 100:
                    self.shapesdto.iso9000 = "取得予定"
                elif 305 < l_pos < 390:
                    self.shapesdto.iso14000 = "取得予定"
            elif 733 < t_pos < 747:
                if 25.5 < l_pos < 100:
                    self.shapesdto.iso9000 = "取得予定なし"
                elif 305 < l_pos < 390:
                    self.shapesdto.iso14000 = "取得予定なし"
            elif t_pos > 800:
                pass

    def get_dict(self):
        return asdict(self.shapesdto)

# class ExcelShapesDTO():
#     def __init__(self):
#         self.__biz_type = None
#         self.__capital_form = None
#         self.__corp_type = None
#         self.__stock_status = None
#         self.__stock_market = ""
#         self.__i9000_certif = ""
#         self.__i14000_certif = ""
#
#     @property
#     def biz_type(self):
#         return self.biz_type
#
#     @biz_type.setter
#     def biz_type(self,param):
#         self.__biz_type = param
#
#     @property
#     def capital_form(self):
#         return self.__capital_form
#
#     @capital_form.setter
#     def capital_form(self, param):
#         self.__capital_form = param
#
#     @property
#     def corp_type(self):
#         return self.__corp_type
#
#     @corp_type.setter
#     def corp_type(self, param):
#         self.__corp_type = param
#
#     @property
#     def stock_status(self):
#         return self.__stock_status
#
#     @stock_status.setter
#     def stock_status(self, param):
#         self.__stock_status = param
#
#     @property
#     def stock_market(self):
#         return self.__stock_market
#
#     @stock_market.setter
#     def stock_market(self, param):
#         self.__stock_market = param
#
#     @property
#     def i9000_certif(self):
#         return self.__i9000_certif
#
#     @i9000_certif.setter
#     def i9000_certif(self, param):
#         self.__i9000_certif = param
#
#     @property
#     def i14000_certif(self):
#         return self.__i14000_certif
#
#     @i14000_certif.setter
#     def i14000_certif(self,param):
#         self.__i14000_certif = param
