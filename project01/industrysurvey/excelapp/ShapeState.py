from abc import ABCMeta
from abc import abstractmethod
from typing import Dict, Any
from dto.ExcelShapesDTO import ShapesDto


class IShapeState(metaclass=ABCMeta):
    @abstractmethod
    def choose(self, state_context):
        pass


class ConcreteState(IShapeState):
    def __init__(self, left_pos, dto):
        self.position = left_pos
        self.shapes_dto = dto

    def choose(self, state_context):
        pass


class VenderBizType(ConcreteState):
    """
    業種分類取得
    biztype = l : メーカー
    biztype = 2 : 商社
    biztype = 3 : メーカー＆商社
    biztype = 4 : 代理店
    biztype = 5 : 卸売
    biztype = 6 : その他
    """

    def __init__(self, left_pos, dto):
        super().__init__(left_pos, dto)
        self.biztype: str = ""

    def choose(self, state_context):
        if 80 < self.position < 125:
            self.biztype = "1"
        elif 145 < self.position < 190:
            self.biztype = "2"
        elif 200 < self.position < 285:
            self.biztype = "3"
        elif 298 < self.position < 350:
            self.biztype = "4"
        elif 360 < self.position < 400:
            self.biztype = "5"
        elif 422 < self.position < 445:
            self.biztype = "6"
        else:
            raise Exception("業種取得エラー")

        self.shapes_dto.shCustomerBizType = self.biztype


class CapitalForm(ConcreteState):
    """
    資本形態　会社形態
    capital_form = 1 : 個人
    capital_form = 2 : 法人
    corp_type = 1 : 株式会社
    corp_type = 2 : 有限会社
    corp_type = 9 : その他
    """

    def __init__(self, left_pos, dto):
        super().__init__(left_pos, dto)
        self.capital_form: str = ""
        self.corp_type: str = ""

    def choose(self, state_context):
        if 80 < self.position < 125:
            self.capital_form = "1"
            self.corp_type = None
        elif 150 < self.position < 235:
            self.capital_form = "2"
            self.corp_type = "1"
        elif 240 < self.position < 290:
            self.capital_form = "2"
            self.corp_type = "2"
        elif 295 < self.position < 400:
            self.capital_form = "2"
            self.corp_type = "9"

        self.shapes_dto.shCapitalForm = self.capital_form
        self.shapes_dto.shCorporateType = self.corp_type


class StockStatus(ConcreteState):
    """
    株式の状況
    stock_status = 0 : 非上場
    stock_status = 1 : 上場
    stock_market = 東証１部、東証2部、その他
    """

    def __init__(self, left_pos, dto):
        super().__init__(left_pos, dto)
        self.stock_status: str = ""
        self.stock_market: str = ""

    def choose(self, state_context):
        if 340 < self.position < 410:
            self.stock_status = "0"
        else:
            self.stock_status = "1"
            if 80 < self.position < 125:
                self.stock_market = "東証１部"
            elif 150 < self.position < 190:
                self.stock_market = "東証２部"
            elif 210 < self.position < 300:
                self.stock_market = "その他"

        self.shapes_dto.shStockListingStatus = self.stock_status
        self.shapes_dto.shStockMarket = self.stock_market


class ISOCertifStatus(ConcreteState):
    def __init__(self, left_pos, dto):
        super().__init__(left_pos, dto)
        self.iso9000_certif: str = ""
        self.iso14000_certif: str = ""

    def choose(self, state_context):
        if 25.5 < self.position < 100:
            self.iso9000_certif = "取得済"
        elif 290 < self.position < 345:
            self.iso14000_certif = "取得済"

        self.shapes_dto.shISO9001Certif = self.iso9000_certif
        self.shapes_dto.shISO14001Certif = self.iso14000_certif


class ISOSplan(ConcreteState):
    def __init__(self, left_pos, dto):
        super().__init__(left_pos, dto)
        self.iso9000_plan: str = ""
        self.iso14000_plan: str = ""

    def choose(self, state_context):
        if 25.5 < self.position < 100:
            self.iso9000_plan = "取得予定"
        elif 290 < self.position < 345:
            self.iso14000_plan = "取得予定"

        self.shapes_dto.shISO9001Plan = self.iso9000_plan
        self.shapes_dto.shISO9001Plan = self.iso14000_plan


class ISONoCerfit(ConcreteState):
    def __init__(self, left_pos, dto):
        super().__init__(left_pos, dto)
        self.iso9000_no_certif: str = ""
        self.iso14000_no_certif: str = ""

    def choose(self, state_context):
        if 25.5 < self.position < 100:
            self.iso9000_no_certif = "取得予定なし"
        elif 290 < self.position < 345:
            self.iso14000_no_certif = "取得予定なし"

        self.shapes_dto.shISO9001NoCertif = self.iso9000_no_certif
        self.shapes_dto.shISO9001NoCertif = self.iso14000_no_certif


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


class SetConcreteState():
    def __init__(self, top, left, dto):
        self.top_pos = top
        self.left_pos = left
        self.shapes = dto
        self.state = self._set_concrete_state()

    def _set_concrete_state(self):
        if 210 < self.top_pos < 225:
            return VenderBizType(self.left_pos, self.shapes)
        if 222 < self.top_pos < 238:
            return CapitalForm(self.left_pos, self.shapes)
        if 246 < self.top_pos < 256:
            return StockStatus(self.left_pos, self.shapes)
        if 715 < self.top_pos < 730:
            return ISOCertifStatus(self.left_pos, self.shapes)
        if 735 < self.top_pos < 745:
            return ISOSplan(self.left_pos, self.shapes)
        if 750 < self.top_pos < 765:
            return ISONoCerfit(self.left_pos, self.shapes)
        else:
            return False


class ShapesPosToValue():
    def __init__(self, xlws):
        self.__shape_dto = ShapesDto()
        self.__shape_pos_list = self.__get_shapes_position(xlws)
        self.__get_shapes_data(self.__shape_dto)

    @property
    def shapes_dto(self):
        return self.__shape_dto

    def __get_shapes_position(self, xlws):
        shape_pos_cls = ExcelShapePosition(xlws)
        return shape_pos_cls.shapes_pos

    def __get_shapes_data(self, dto):
        conv_pos_cls = ConvertPosToValue(dto, self.__shape_pos_list)
        conv_pos_cls.set_shapes_data()


class ConvertPosToValue():
    def __init__(self, shape_dto, shape_pos_list):
        self.shapesdto = shape_dto
        self.shape_list = shape_pos_list

    def set_shapes_data(self):
        # self.shape_list = shape_pos_list
        for dict in self.shape_list:
            self.top = dict["top"]
            self.left = dict["left"]
            state_factory = SetConcreteState(self.top, self.left, self.shapesdto)
            concrete_state = state_factory.state
            # タカノロゴを取得した際にエラーが発生するため、フラグを立ててエラーを回避する。
            if not concrete_state == False:
                state = StateContext(concrete_state)
                state.choose()

        return self.shapesdto


class ExcelShapePosition():
    def __init__(self, xlws):
        self.shapes_pos = []
        self.xlws = xlws
        self.get_shapes_position()

    def get_shapes_position(self):
        # self.xlws = xlws
        shapes = self.xlws.shapes
        for sh in shapes:
            var: Dict[str, Any] = {"top": sh.top, "left": sh.left}
            self.shapes_pos.append(var)
        return self.shapes_pos
