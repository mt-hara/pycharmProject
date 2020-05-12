class ShapesDto():
    def __init__(self):
        self.__shCustomerBizType: str = ""  # shape only
        self.__shCapitalForm: str = ""  # shape only
        self.__shCorporateType: str = ""  # shape only
        self.__shStockListingStatus: str = ""  # shape only
        self.__shStockMarket: str = ""  # shape only
        self.__shISO9001Certif: str = ""  # shape or cell data
        self.__shISO9001Plan: str = ""  # shape or cell data
        self.__shISO9001NoCertif: str = ""  # shape or cell data
        self.__shISO14001Certif: str = ""  # shape or cell data
        self.__shISO14001Plan: str = ""  # shape or cell data
        self.__shISO14001NoCertif: str = ""  # shape or cell data

    @property
    def shCustomerBizType(self):
        return self.__shCustomerBizType

    @shCustomerBizType.setter
    def shCustomerBizType(self, param: str):
        self.__shCustomerBizType = param

    @property
    def shCapitalForm(self):
        return self.__shCapitalForm

    @shCapitalForm.setter
    def shCapitalForm(self, param: str):
        self.__shCapitalForm = param

    @property
    def shCorporateType(self):
        return self.__shCorporateType

    @shCorporateType.setter
    def shCorporateType(self, param: str):
        self.__shCorporateType = param

    @property
    def shStockListingStatus(self):
        return self.__shStockListingStatus

    @shStockListingStatus.setter
    def shStockListingStatus(self, param: str):
        self.__shStockListingStatus = param

    @property
    def shStockMarket(self):
        return self.__shStockMarket

    @shStockMarket.setter
    def shStockMarket(self, param: str):
        self.__shStockMarket = param

    @property
    def shISO9001Certif(self):
        return self.__shISO9001Certif

    @shISO9001Certif.setter
    def shISO9001Certif(self, param: str):
        self.__shISO9001Certif = param

    @property
    def shISO9001Plan(self):
        return self.__shISO9001Plan

    @shISO9001Plan.setter
    def shISO9001Plan(self, param: str):
        self.__shISO9001Plan = param

    @property
    def shISO9001NoCertif(self):
        return self.__shISO9001NoCertif

    @shISO9001NoCertif.setter
    def shISO9001NoCertif(self, param: str):
        self.__shISO9001NoCertif = param

    @property
    def shISO14001Certif(self):
        return self.__shISO14001Certif

    @shISO14001Certif.setter
    def shISO14001Certif(self, param: str):
        self.__shISO14001Certif = param

    @property
    def shISO14001Plan(self):
        return self.__shISO14001Plan

    @shISO14001Plan.setter
    def shISO14001Plan(self, param: str):
        self.__shISO14001Plan = param

    @property
    def shISO14001NoCertif(self):
        return self.__shISO14001NoCertif

    @shISO14001NoCertif.setter
    def shISO14001NoCertif(self, param: str):
        self.__shISO14001NoCertif = param
