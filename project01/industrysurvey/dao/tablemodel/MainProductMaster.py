from dao.BaseEngine import MetaBase
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, Float, Boolean, ForeignKey


class MainProductMaster(MetaBase):
    __tablename__ = "mainproductmaster"
    customerCd: str = Column(String, ForeignKey("customermaster.customerCd"), primary_key=True)
    mainProducts_1: str = Column(String)
    mainProducts_2: str = Column(String)
    mainProducts_3: str = Column(String)
    mainProducts_4: str = Column(String)
    mainProducts_5: str = Column(String)

    def set_data(self, xldto):
        self.mainProducts_1 = xldto.xlMainProducts_1
        self.mainProducts_2 = xldto.xlMainProducts_2
        self.mainProducts_3 = xldto.xlMainProducts_3
        self.mainProducts_4 = xldto.xlMainProducts_4
        self.mainProducts_5 = xldto.xlMainProducts_5