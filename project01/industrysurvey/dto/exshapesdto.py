from abc import ABCMeta
from abc import abstractmethod


class IShapeState(metaclass=ABCMeta):
    @abstractmethod
    def choose(self, state_context):
        pass


class ConcreteState(IShapeState):
    def __init__(self, left_pos, dto):
        self.position = left_pos
        self.shapesdata = dto

    def choose(self, state_context):
        pass


# @singleton
class VenderBizType(ConcreteState):
    def __init__(self, left_pos, dto):
        super().__init__(left_pos, dto)

    def choose(self, state_context):
        if 80 < self.position < 125:
            self.shapesdata.CustomerBizType = 1
        elif 145 < self.position < 190:
            self.shapesdata.CustomerBizType = 2
        elif 200 < self.position < 285:
            self.shapesdata.CustomerBizType = 3
        elif 298 < self.position < 350:
            self.shapesdata.CustomerBizType = 4
        elif 360 < self.position < 400:
            self.shapesdata.CustomerBizType = 5
        elif 422 < self.position < 445:
            self.shapesdata.CustomerBizType = 6
        else:
            raise Exception("業種取得エラー")


class CapitalForm(ConcreteState):
    def __init__(self, left_pos, dto):
        super().__init__(left_pos, dto)

    def choose(self, state_context):
        if 80 < self.position < 125:
            self.shapesdata.CapitalForm = 1
        else:
            self.shapesdata.CapitalForm = 2
            if 180 < self.position < 235:
                self.shapesdata.CorporateType = 1
            elif 240 < self.position < 290:
                self.shapesdata.CorporateType = 2
            elif 295 < self.position < 400:
                self.shapesdata.CorporateType = 9


class StockStatus(ConcreteState):
    def __init__(self, left_pos, dto):
        super().__init__(left_pos, dto)

    def choose(self, state_context):
        if 340 < self.position < 410:
            self.shapesdata.stockListingStatus = 0
        else:
            self.shapesdata.stockListingStatus = 1
            if 80 < self.position < 125:
                self.shapesdata.stockMarket = "東証１部"
            elif 150 < self.position < 190:
                self.shapesdata.stockMarket = "東証２部"
            elif 210 < self.position < 300:
                self.shapesdata.stockMarket = "その他"


class ISOCertifStatus(ConcreteState):
    def __init__(self, left_pos, dto):
        super().__init__(left_pos, dto)

    def choose(self, state_context):
        if 25.5 < self.position < 100:
            self.shapesdata.ISO9001Certif = "取得済"
        elif 305 < self.position < 390:
            self.shapesdata.ISO14001Certif = "取得済"


class ISOSplan(ConcreteState):
    def __init__(self, left_pos, dto):
        super().__init__(left_pos, dto)

    def choose(self, state_context):
        if 25.5 < self.position < 100:
            self.shapesdata.ISO9001Certif = "取得予定"
        elif 305 < self.position < 390:
            self.shapesdata.ISO14001Certif = "取得予定"


class ISONoCerfit(ConcreteState):
    def __init__(self, left_pos, dto):
        super().__init__(left_pos, dto)

    def choose(self, state_context):
        if 25.5 < self.position < 100:
            self.shapesdata.ISO9001Certif = "取得予定なし"
        elif 305 < self.position < 390:
            self.shapesdata.ISO14001Certif = "取得予定なし"


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


def set_concrete_state(top_pos, left_pos, dto):
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
        return ISONoCerfit(left_pos, dto)
    if top_pos > 800:
        return False


class ShapesDataDTO():
    def __init__(self, shapadata):
        self.shapesdto = shapadata
        self.shapes_list = None

    def get_shapes_dt(self, lists):
        self.shapes_list = lists
        for dict in self.shapes_list:
            self.top = dict["top"]
            self.left = dict["left"]
            concrete_state = set_concrete_state(self.top, self.left, self.shapesdto)
            # タカノロゴを取得した際にエラーが発生するため、フラグを立ててエラーを回避する。
            if not concrete_state == False:
                state = StateContext(concrete_state)
                state.choose()
