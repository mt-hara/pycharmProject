class ExcelShapesDTO():
    def __init__(self):
        self.__biz_type = None
        self.__capital_form = None
        self.__corp_type = None
        self.__stock_status = None
        self.__stock_market = ""
        self.__i9000_certif = ""
        self.__i14000_certif = ""

    @property
    def biz_type(self):
        return self.biz_type

    @biz_type.setter
    def biz_type(self,param):
        self.__biz_type = param

    @property
    def capital_form(self):
        return self.__capital_form

    @capital_form.setter
    def capital_form(self, param):
        self.__capital_form = param

    @property
    def corp_type(self):
        return self.__corp_type

    @corp_type.setter
    def corp_type(self, param):
        self.__corp_type = param

    @property
    def stock_status(self):
        return self.__stock_status

    @stock_status.setter
    def stock_status(self, param):
        self.__stock_status = param

    @property
    def stock_market(self):
        return self.__stock_market

    @stock_market.setter
    def stock_market(self, param):
        self.__stock_market = param

    @property
    def i9000_certif(self):
        return self.__i9000_certif

    @i9000_certif.setter
    def i9000_certif(self, param):
        self.__i9000_certif = param

    @property
    def i14000_certif(self):
        return self.__i14000_certif

    @i14000_certif.setter
    def i14000_certif(self,param):
        self.__i14000_certif = param


class GetShapeData():
    pass




