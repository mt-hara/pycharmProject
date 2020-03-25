from typing import List
from dataclasses import dataclass
from abc import ABCMeta
from abc import abstractmethod
from singleton import singleton
@dataclass
class ShapesDataClass:
    biz_type: int
    capital_form: int
    corp_type: int
    stock_status: bool
    stock_market: str
    iso9000: str
    iso14000: str


class IShapeState(metaclass=ABCMeta,singleton):
    def __init__(self,value):
        self.l_pos = value

    @abstractmethod
    def choose(self, state_context):
        pass


class VenderBizType(IShapeState):
    def __init__(self,value):
        super(VenderBizType, self).__init__(value)

    def choose(self, state_context):
        pass


class StockStatus(IShapeState):
    pass

class ISOCertifStatus(IShapeState):
    pass

class ISOSplan(IShapeState):
    pass


class ISONoCerfit(IShapeState):
    pass

class StateContext():
    def __init__(self, state_type):
        self.set_state(state_type)

    @property
    def curt_state(self):
        return self.__curt_state

    @curt_state.setter
    def curt_state(self, obj):
        self.__curt_state =  obj

    def set_state(self, new_state):
        self.__curt_state = new_state

    def choose(self,left_pos):
        self.curt_state.choose(self, left_pos)


def setconcstate(top_pos, left_pos):
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

