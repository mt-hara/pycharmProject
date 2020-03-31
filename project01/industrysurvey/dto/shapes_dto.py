class ShapesDto():
    def __init__(self):
        self.__shCustomerBizType: int = 0
        self.__shCapitalForm: int = 0
        self.__shCorporateType: str = ""
        self.__shStockListingStatus: int = 0
        self.__shStockMarket: str = ""
        self.__shISO9001Certif: str = ""
        self.__shISO9001Plan: str = ""
        self.__shISO9001NoCertif: str = ""
        self.__shISO14001Certif: str = ""
        self.__shISO14001Plan: str = ""
        self.__shISO14001NoCertif: str = ""

    @property
    def shCustomerBizType(self):
        return self.__shCustomerBizType

    @shCustomerBizType.setter
    def shCustomerBizType(self,param: int):
        self.__shCustomerBizType = param

    @property
    def shCapitalForm(self):
        return self.__shCapitalForm

    @shCapitalForm.setter
    def shCapitalForm(self, param: int):
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
    def shStockListingStatus(self, param: int):
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


        # : str = ""
        # : str = ""
        # shISO9001Plan: str = ""
        # shISO9001NoCertif: str = ""
        # shISO14001Certif: str = ""
        # shISO14001Plan: str = ""
        # shISO14001NoCertif: str = ""