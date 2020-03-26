from typing import List
from dataclasses import dataclass, fields
from abc import ABCMeta
from abc import abstractmethod
from abstractdto.abscustomermstrdto import ShapesDataClass

# def singleton(class_):
#     class class_w(class_):
#         _instance = None
#         def __new__(class_, *args, **kwargs):
#             if class_w._instance is None:
#                 class_w._instance = super(class_w, class_).__new__(class_, *args, **kwargs)
#                 class_w._instance._sealed = False
#             return class_w._instance
#         def __init__(self, *args, **kwargs):
#             if self._sealed:
#                 return
#             super(class_w, self).__init__(*args, **kwargs)
#             self._sealed = True
#     class_w.__name__ = class_.__name__
#     return class_w
#

# def singleton(class_):
#     instance = {}
#
#     def getinstance(*args, **kwargs):
#         if class_ not in instance:
#             instance[class_] = class_(*args, **kwargs)
#         return instance[class_]
#
#     return getinstance


class IShapeState(metaclass=ABCMeta):
    @abstractmethod
    def choose(self, state_context):
        pass


class ConcreteState(IShapeState):
    def __init__(self, left_pos,dto):
        self.position = left_pos
        self.shapesdata = dto

    def choose(self, state_context):
        pass


# @singleton
class VenderBizType(ConcreteState):
    def __init__(self, left_pos,dto):
        super().__init__(left_pos,dto)
        # self.bizType = None

    def choose(self, state_context):
        if 80 < self.position < 125:
            self.shapesdata.biz_type = 1
        elif 145 < self.position < 190:
            self.shapesdata.biz_type = 2
        elif 200 < self.position < 285:
            self.shapesdata.biz_type = 3
        elif 298 < self.position < 350:
            self.shapesdata.biz_type = 4
        elif 360 < self.position < 400:
            self.shapesdata.biz_type = 5
        elif 422 < self.position < 445:
            self.shapesdata.biz_type = 6
        else:
            raise Exception("業種取得エラー")


class CapitalForm(ConcreteState):
    def __init__(self, left_pos, dto):
        super().__init__(left_pos, dto)

    def choose(self, state_context):
        if 80 < self.position < 125:
            self.shapesdata.stock_status=1
        else:
            self.shapesdata.stock_status=2
            if 180 < self.position < 235:
                self.shapesdata.corp_type = 1
            elif 240 < self.position < 290:
                self.shapesdata.corp_type = 2
            elif 295 < self.position < 400:
                self.shapesdata.corp_type = 9


class StockStatus(ConcreteState):
    def __init__(self, left_pos, dto):
        super().__init__(left_pos, dto)

    def choose(self, state_context):
        if 340 < self.position < 410:
            self.shapesdata.stock_status = 0
        else:
            self.shapesdata.stock_status = 1
            if 80 < self.position < 125:
                self.shapesdata.stock_market = "東証１部"
            elif 150 < self.position < 190:
                self.shapesdata.stock_market = "東証２部"
            elif 210 < self.position < 300:
                self.shapesdata.stock_market = "その他"



class ISOCertifStatus(ConcreteState):
    pass


class ISOSplan(ConcreteState):
    pass


class ISONoCerfit(ConcreteState):
    pass


class StateContext():
    def __init__(self, state_type):
        self.set_state(state_type)

    @property
    def curt_state(self):
        return self.__curt_state

    @curt_state.setter
    def curt_state(self, obj):
        self.__curt_state = obj

    def set_state(self, new_state):
        self.__curt_state = new_state

    def choose(self):
        self.curt_state.choose(self)


def set_concrete_state(top_pos, left_pos,dto):
    if 210 < top_pos < 225:
        return VenderBizType(left_pos, dto)
    if 222 < top_pos < 238:
        return CapitalForm(left_pos, dto)
    if 246 < top_pos < 256:
        return StockStatus(left_pos, dto)
    if 690 < top_pos < 717:
        return ISOCertifStatus(left_pos, dto)
    if 720 < top_pos < 731:
        return ISOSplan(left_pos, dto)
    if 733 < top_pos < 747:
        return ISONoCerfit(left_pos,dto)


class main():
    def __init__(self):
        self.top: float = 0
        self.left: float = 0
        # self.dto = None
        self.init()

    def init(self):
        self.top = 215
        self.left = 210
        self.top2 = 230
        self.left2= 90
        self.dto = ShapesDataClass()
        state = StateContext(set_concrete_state(self.top,self.left,self.dto))
        state.choose()
        print(self.dto.biz_type)

        #
        # self.concrete_state = set_concrete_state(self.top2, self.left2)
        # state = StateContext(self.concrete_state)
        # state.choose()


        # print(self.dto.biz_type)
        # print(self.dto.stock_status)
        # print(self.dto.__dict__)
        # print(self.dto.biz_type)
        # print(self.dto.capital_form)


if __name__ == "__main__":
    main()
    # top = 215
    # left = 189
    # dto = ShapesDataClass
    # sc = StateContext(set_concrete_state(top,left,dto))
    # sc.choose()
    # print(dto.biz_type)
