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
# @dataclass
# class AllCustomerMaster:
#     CustomerCd: str  # H3
#     ringiNo: str  #  ""
#     CustomerName: str  # H5
#     CustomerKanaName: str  # H4
#     CustomerShortName: str  # ""
#     excludeLaw: bool  # false
#     headOfficeZipCd: str  # I7
#     headOfficeAddress1: str  # H8
#     headOfficeAddress2: str  # ""
#     headOfficeTel: str  # X7
#     headOfficeFax: str  # AH7
#     BranchOfficeZipCd: str  # I10
#     BranchOfficeAddress1: str  # H11
#     BranchOfficeAddress2: str  # ""
#     BranchOfficeTel: str  # X10
#     BranchOfficeFax: str  # AH10
#     repName: str  # H14
#     repKanaName: str  # H13
#     repJobTitle: str  # AD13
#     repBirthday: str  # AD14 + "年" + AH14 + "月" + AK14 + "日"
#     employees: int  # k22
#     employeeMonth: int  # I23
#     employeeYear: int  # O23
#     CapitalForm: int  # shape 取得
#     CorporateType: str  # shape 取得
#     OtherCorpType: str  # ""
#     CustomerCapital: float  # H18
#     establishedMonth: int  # I19
#     establishedYear: int  # O19
#     AccountClosingMonth: int  # M21
#     ReturnOnEquity: float  # I20
#     ISO9001Certif: str  # D50 shape 取得 取得済 取得予定 取得予定なし
#     ISO9001ResistedNo: str  # N50
#     ISO9001CertifPlanYM: str  # N51 + "年" + R51 "月"
#     ISO14001Certif: str  # V50 shape 取得 取得 取得済 取得予定 取得予定なし
#     ISO14001ResistedNo: str  # AF50
#     ISO14001CertifPlanYM: str  # AF51 + "年" + AJ51 "月"
#     OtherCertif: str  # I53
#     CustomerCategory: str  # ""
#     CustomerBizType: int  # shape 取得
#     picName: str  # H57
#     picKanaName: str  # ""
#     PicEmailAddress: str  # H58
#     picDept: str  # H59
#     picPosition: str  # G59
#     sameHeadOffice: str  # ""
#     contactZipCd: str  # H55
#     contactAddress1: str  # C56
#     contactAddress2: str  # ""
#     contactTel: str  # H60
#     contactFax: str  # G60
#     contactInfo: str  # ""
#     FTA: int  # 0 1:取引基本契約書 締結済
#     FTANotice: str  # ""
#     QAA: int  # 0 1:品質保証協定書 締結済
#     QAANotice: str  # ""
#     NDA: int  # 0 1:秘密保持契約書 締結済
#     NDANotice: str  # ""
#     otherContract: str  # ""
#     stockListingStatus: bool  # 0:非上場　1:上場 shape 取得
#     stockMarket: str  # shape 取得 Text
#     MainStockholder_1: str  # U19
#     MainStockholder_2: str  # U20
#     MainStockholder_3: str  # U21
#     MainStockholder_4: str  # U22
#     MainStockholder_5: str  # U23
#     ratioSH_1: float  # AK19
#     ratioSH_2: float  # AK20
#     ratioSH_3: float  # AK21
#     ratioSH_4: float  # AK22
#     ratioSH_5: float  # AK23
#     mainCustomer_1: str  # C28
#     mainCustomer_2: str  # C29
#     mainCustomer_3: str  # C30
#     mainCustomer_4: str  # C31
#     mainCustomer_5: str  # C32
#     CurPrdYear: str  # M26
#     CurPrdSales_1: float  # M28
#     CurPrdSales_2: float  # M29
#     CurPrdSales_3: float  # M30
#     CurPrdSales_4: float  # M31
#     CurPrdSales_5: float  # M32
#     CurPrdSales_Our: float  # M34
#     CurPrdSales_Other: float  # M33
#     CurPrdSalesRatio_1: float  # S28
#     CurPrdSalesRatio_2: float  # S29
#     CurPrdSalesRatio_3: float  # S30
#     CurPrdSalesRatio_4: float  # S31
#     CurPrdSalesRatio_5: float  # S32
#     CurPrdSalesRatio_Our: float  # S34
#     CurPrdSalesRatio_Othor: float  # S33
#     CurPrdSales_Sum: float  # M35
#     CurPrdOperatingProfit: float  # M36
#     CurPrdOrdinaryincome: float  # M37
#     PrevPrdYear: str  # V26
#     PrevPrdSales_1: float  # V28
#     PrevPrdSales_2: float  # V29
#     PrevPrdSales_3: float  # V30
#     PrevPrdSales_4: float  # V31
#     PrevPrdSales_5: float  # V32
#     PrevPrdSales_Our: float  # V34
#     PrevPrdSales_Other: float  # V33
#     PrevPrdSalesRatio_1: float  # AB28
#     PrevPrdSalesRatio_2: float  # AB29
#     PrevPrdSalesRatio_3: float  # AB30
#     PrevPrdSalesRatio_4: float  # AB31
#     PrevPrdSalesRatio_5: float  # AB32
#     PrevPrdSalesRatio_Our: float  # AB34
#     PrevPrdSalesRatio_Other: float  # AB33
#     PrevPrdSales_Sum: float  # V35
#     PrevPrdOperatingProfit: float  # V36
#     PrevPrdOrdinaryIncome: float  # V37
#     LastPrdYear: str  # AE26
#     lastPrdSales_1: float  # AE28
#     lastPrdSales_2: float  # AE29
#     lastPrdSales_3: float  # AE30
#     lastPrdSales_4: float  # AE31
#     lastPrdSales_5: float  # AE32
#     lastPrdSales_Our: float  # AE34
#     lastPrdSales_Other: float  # AE33
#     lastPrdSalesRatio_1: float  # AK28
#     lastPrdSalesRatio_2: float  # AK29
#     lastPrdSalesRatio_3: float  # AK30
#     lastPrdSalesRatio_4: float  # AK31
#     lastPrdSalesRatio_5: float  # AK32
#     lastPrdSalesRatio_Our: float  # AK34
#     lastPrdSalesRatio_Other: float  # AK33
#     lastPrdSales_sum: float  # AE35
#     lastPrdOperatingProfit: float  # AE36
#     lastPrdOrdinaryincome: float  # AE37
#     CurPrdMainProducts: str  # M38
#     MainSupplier_1: str  # W42
#     MainSupplier_2: str  # W43
#     MainSupplier_3: str  # W44
#     MainSupplier_4: str  # W45
#     MainSupplier_5: str  # W46
#     MainSupplierValue_1: float  # AG42
#     MainSupplierValue_2: float  # AG43
#     MainSupplierValue_3: float  # AG44
#     MainSupplierValue_4: float  # AG45
#     MainSupplierValue_5: float  # AG46
#     MainSupplierRatio_1: float  # AK42
#     MainSupplierRatio_2: float  # AK43
#     MainSupplierRatio_3: float  # AK44
#     MainSupplierRatio_4: float  # AK45
#     MainSupplierRatio_5: float  # AK46
#     MainProducts_1: str  # C42
#     MainProducts_2: str  # C43
#     MainProducts_3: str  # C44
#     MainProducts_4: str  # C45
#     MainProducts_5: str  # C46
#
#     def set_cell_data(self, ws):
#         pass
