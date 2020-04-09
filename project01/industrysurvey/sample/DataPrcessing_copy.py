from dao.BaseEngine import BaseSession, MetaBase
from abc import ABCMeta, abstractmethod
from typing import Dict, Any
from dao.tablemodel.CustomerMaster import CustomerMaster
from dao.tablemodel.StockStatusMaster import StockStatusMaster
# from dao.crud.InsertData import InsertData
# from dao.crud.UpdateData import UpdateData

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
        return Insert()
    else:
        return Update()


class DataProsessing(BaseSession,metaclass=ABCMeta):
    @abstractmethod
    def InsOrUpdate(self, xldto):
        pass


class Insert(DataProsessing):
    def InsOrUpdate(self, xldto):
        pass
        # try:
        #     customer = CustomerMaster()
        #     customer.stockstatus = StockStatusMaster()
        #     customer.set_data(xldto)
        #     customer.stockstatus.set_data(xldto)
        #
        #     with self.transaction() as sesstion:
        #         self.session.add(customer)
        # except Exception as e:
        #     print(e)


class Update(DataProsessing):
    def InsOrUpdate(self, xldto):
        pass

        # try:
        #     with self.transaction() as session:
        #         update_customer = self.session.query(CustomerMaster).filter(CustomerMaster.customerCd == xldto.xlCustomerCd).first()
        #         update_customer.set_data(xldto)
        #         update_customer.stockstatus.set_data(xldto)
        # except Exception as e:
        #     print(e)


class DeleteAll(BaseSession):
    def __init__(self):
        super().__init__()

        try:
            with self.transaction() as session:
                def_list = self.session.query(CustomerMaster).all()
                if not len(def_list) == 0:
                    for item in def_list:
                        self.session.delete(item)
        except Exception as e:
            print(e)


class SelectAll(BaseSession):
    def __init__(self):
        super().__init__()
        self.select()

    def select(self):
        result = self.session.query(CustomerMaster).all()
        return result