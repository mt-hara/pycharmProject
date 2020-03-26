from typing import List
from dataclasses import dataclass
from abc import ABCMeta
from abc import abstractmethod


def singleton(class_):
    instance = {}

    def getinstance(*args, **kwargs):
        if class_ not in instance:
            instance[class_] = class_(*args, **kwargs)
        return instance[class_]

    return getinstance


@singleton
@dataclass
class ShapesDataClass:
    biz_type: int
    capital_form: int
    corp_type: int
    stock_status: bool
    stock_market: str
    iso9000: str
    iso14000: str


class IShapeState(metaclass=ABCMeta):
    @abstractmethod
    def choose(self, state_context, dto):
        pass


class ConcreteState(IShapeState):
    def __init__(self, left_pos):
        self.position = left_pos

    def choose(self, state_context,dto):
        pass


@singleton
class VenderBizType(ConcreteState):
    def __init__(self, left_pos):
        super().__init__(left_pos)
        self.bizType = None

    def choose(self, state_context, dto):
        if 80 < self.position < 125:
            dto.biz_type = 1
        elif 145 < self.position < 190:
            dto.biz_type = 2
        elif 200 < self.position < 285:
            dto.biz_type = 3
        elif 298 < self.position < 350:
            dto.biz_type = 4
        elif 360 < self.position < 400:
            dto.biz_type = 5
        elif 422 < self.position < 445:
            dto.biz_type = 6
        else:
            raise Exception("業種取得エラー")


class StockStatus(ConcreteState):
    pass


class ISOCertifStatus(ConcreteState):
    pass


class ISOSplan(ConcreteState):
    pass


class ISONoCerfit(ConcreteState):
    pass


class StateContext():
    def __init__(self, state_type, dto):
        self.set_state(state_type)
        self.dto = dto

    @property
    def curt_state(self):
        return self.__curt_state

    @curt_state.setter
    def curt_state(self, obj):
        self.__curt_state = obj

    def set_state(self, new_state):
        self.__curt_state = new_state

    def choose(self):
        self.curt_state.choose(self,self.dto)


def set_concrete_state(top_pos, left_pos):
    if 210 < top_pos < 225:
        return VenderBizType(left_pos)
    if 237 < top_pos < 238:
        return StockStatus(left_pos)
    if 690 < top_pos < 717:
        return ISOCertifStatus(left_pos)
    if 720 < top_pos < 731:
        return ISOSplan(left_pos)
    if 733 < top_pos < 747:
        return ISONoCerfit(left_pos)


class main():
    def __init__(self):
        self.top: float = 0
        self.left: float = 0
        # self.dto = None
        self.init()

    def init(self):
        self.top = 215
        self.left = 150
        self.dto = ShapesDataClass
        self.concrete_state = set_concrete_state(self.top, self.left)
        state = StateContext(self.concrete_state,self.dto)
        state.choose()
        print(state.dto.biz_type)

        # print(self.dto.biz_type)


if __name__ == "__main__":
    main()
    # top = 215
    # left = 189
    # dto = ShapesDataClass
    # sc = StateContext(set_concrete_state(top,left,dto))
    # sc.choose()
    # print(dto.biz_type)