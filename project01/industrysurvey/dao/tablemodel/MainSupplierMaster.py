from dao.BaseEngine import MetaBase
from sqlalchemy import Column, Integer, String, Float, Boolean, ForeignKey


class MainSupplierMaster(MetaBase):
    __tablename__ = "mainsuppliermaster"
    customerCd: str = Column(String, ForeignKey("customermaster.customerCd"), primary_key=True)
    mainSupplier_1: str = Column(String)
    mainSupplier_2: str = Column(String)
    mainSupplier_3: str = Column(String)
    mainSupplier_4: str = Column(String)
    mainSupplier_5: str = Column(String)
    mainSupplierValue_1: int = Column(Integer)
    mainSupplierValue_2: int = Column(Integer)
    mainSupplierValue_3: int = Column(Integer)
    mainSupplierValue_4: int = Column(Integer)
    mainSupplierValue_5: int = Column(Integer)
    mainSupplierRatio_1: float = Column(Float)
    mainSupplierRatio_2: float = Column(Float)
    mainSupplierRatio_3: float = Column(Float)
    mainSupplierRatio_4: float = Column(Float)
    mainSupplierRatio_5: float = Column(Float)

    def set_data(self, xldto):
        self.mainSupplier_1 = xldto.xlMainSupplier_1
        self.mainSupplier_2 = xldto.xlMainSupplier_2
        self.mainSupplier_3 = xldto.xlMainSupplier_3
        self.mainSupplier_4 = xldto.xlMainSupplier_4
        self.mainSupplier_5 = xldto.xlMainSupplier_5
