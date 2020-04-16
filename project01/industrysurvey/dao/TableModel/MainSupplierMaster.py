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
        self.mainSupplier_1: str = xldto.xlMainSupplier_1
        self.mainSupplier_2: str = xldto.xlMainSupplier_2
        self.mainSupplier_3: str = xldto.xlMainSupplier_3
        self.mainSupplier_4: str = xldto.xlMainSupplier_4
        self.mainSupplier_5: str = xldto.xlMainSupplier_5
        self.mainSupplierValue_1: int = xldto.xlMainSupplierValue_1
        self.mainSupplierValue_2: int = xldto.xlMainSupplierValue_2
        self.mainSupplierValue_3: int = xldto.xlMainSupplierValue_3
        self.mainSupplierValue_4: int = xldto.xlMainSupplierValue_4
        self.mainSupplierValue_5: int = xldto.xlMainSupplierValue_5
        self.mainSupplierRatio_1: float = xldto.xlMainSupplierRatio_1
        self.mainSupplierRatio_2: float = xldto.xlMainSupplierRatio_2
        self.mainSupplierRatio_3: float = xldto.xlMainSupplierRatio_3
        self.mainSupplierRatio_4: float = xldto.xlMainSupplierRatio_4
        self.mainSupplierRatio_5: float = xldto.xlMainSupplierRatio_5

