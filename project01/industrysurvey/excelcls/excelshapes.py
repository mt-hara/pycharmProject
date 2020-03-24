from typing import List
from dataclasses import dataclass
from abc import ABCMeta
from abc import abstractmethod


@dataclass
class ShapesDataClass:
    biz_type: int
    capital_form: int
    corp_type: int
    stock_status: bool
    stock_market: str
    iso9000: str
    iso14000: str


class ShapesState(metaclass=ABCMeta):
    @abstractmethod
    def choose(self, *args):
        pass


class ConcreteShapesState(ShapesState):
    def __init__(self, left_pos):
        # self.state = state
        self.left_pos = left_pos

    def choose(self, left_pos):
        pass

    def getconcretestate(self):
        return self


class VenderBizType(ConcreteShapesState):
    def __init__(self, left_pos):
        super().__init__(left_pos)
        # super(VenderBizType, self).__init__(left_pos)
        self.bizType = None

    def choose(self, left_pos):
        if 80 < self.left_pos < 225:
            self.retval = 1
        elif 145 < self.left_pos < 190:
            self.retval = 2
        self.bizType = self.retval
        print(self.bizType)


class StockStatus(ConcreteShapesState):
    def __init__(self, left_pos):
        super().__init__(left_pos)




def setconcstate(top_pos, left_pos):
    if 210 < top_pos < 225:
        return VenderBizType(left_pos)


class Context():
    def __init__(self, stateobj):
        self.state = stateobj

    def set_state(self, obj):
        self.state = obj

    def choose(self):
        self.state.choose(self)

    def get_state(self):
        return self.state.getconcretestate()


if __name__ == "__main__":
    top = 215
    left = 85
    obj = Context(setconcstate(top, left))
    obj.choose()

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

# class ShapeDataDTO():
#     def __init__(self, pos_list):
#         self.shapesdto = ShapesDataClass()
#         self.shapes_pos = pos_list
#
#
#     def pos_value(self, pos_data, pos_tag):
#         return pos_data[pos_tag]
#
#     def choose_category(self,t_pos, l_pos):
#         if 210 < t_pos < 225:
#             self.choose_biztype(l_pos)
#
#
#     def choose_biztype(self,l_pos):
#         if 80 < l_pos < 125:
#             ret_val = 1
#
