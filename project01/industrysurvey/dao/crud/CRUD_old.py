from dao.BaseEngine import BaseSession, MetaBase
from abc import ABCMeta, abstractmethod
from typing import Dict, Any
from dao.tablemodel.CustomerMaster import CustomerMaster
from dao.tablemodel.StockStatusMaster import StockStatusMaster


class ExecuteNonQuery():
    # SelectOparationクラスのラッパークラス
    def __init__(self, xldao):
        self.xldao = xldao
        self.select_init()
        self.select_execute()

    def select_init(self):
        self.select_operation = SelectOperation(self.xldao)

    def select_execute(self):
        self.select_operation.InsOrUpdate()


class SelectOperation():
    def __init__(self, xldao):
        self.xldao = xldao
        self.querytype = chose_context(self.xldao)

    def InsOrUpdate(self):
        self.querytype.InsOrUpdate(self.xldao)


def chose_context(xldto):
    base = BaseSession()
    param = xldto.xlCustomerCd
    result = base.session.query(CustomerMaster).filter(CustomerMaster.customerCd == param).all()
    if len(result) == 0:
        return InsertData()
    else:
        return UpdateData()


class DataProsessing(BaseSession,metaclass=ABCMeta):
    @abstractmethod
    def InsOrUpdate(self, xldto):
        pass


class InsertData(DataProsessing):
    def InsOrUpdate(self, xldto):
        try:
            customer = CustomerMaster()
            customer.stockstatus = StockStatusMaster()
            customer.set_data(xldto)
            customer.stockstatus.set_data(xldto)

            with self.transaction() as sesstion:
                self.session.add(customer)
        except Exception as e:
            print(e)


class UpdateData(DataProsessing):
    def InsOrUpdate(self, xldto):
        try:
            with self.transaction() as session:
                update_customer = self.session.query(CustomerMaster).filter(CustomerMaster.customerCd == xldto.xlCustomerCd).first()
                update_customer.set_data(xldto)
                update_customer.stockstatus.set_data(xldto)
        except Exception as e:
            print(e)
