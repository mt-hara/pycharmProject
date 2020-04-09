from dao.BaseEngine import BaseSession, MetaBase
from abc import ABCMeta, abstractmethod
from dao.tablemodel.CustomerMaster import CustomerMaster
from dao.tablemodel.StockStatusMaster import StockStatusMaster


class ExecuteNoneQuery(BaseSession):
    def __init__(self, xldto):
        super().__init__()
        self.xldto = xldto
        self.querytype = self.__has_record()
        self.execute()

    def execute(self):
        self.querytype.execute(self.xldto)

    def __has_record(self):
        param = self.xldto.xlCustomerCd
        result = self.session.query(CustomerMaster).filter(CustomerMaster.customerCd == param).all()
        if len(result) == 0:
            return Insert()
        else:
            return Update()


class Excecute(metaclass=ABCMeta):
    @abstractmethod
    def execute(self, xldto):
        pass


class Insert(Excecute, BaseSession):
    def execute(self, xldto):
        try:
            customer = CustomerMaster()
            customer.stockstatus = StockStatusMaster()
            customer.set_data(xldto)
            customer.stockstatus.set_data(xldto)

            with self.transaction() as session:
                self.session.add(customer)
        except Exception as e:
            print(e)


class Update(Excecute, BaseSession):
    def execute(self, xldto):
        try:
            with self.transaction() as session:
                update_customer = self.session.query(CustomerMaster).filter(CustomerMaster.customerCd == xldto.xlCustomerCd).first()
                update_customer.set_data(xldto)
                update_customer.stockstatus.set_data(xldto)
        except Exception as e:
            print(e)
