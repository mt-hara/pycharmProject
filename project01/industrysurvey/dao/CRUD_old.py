from dao.BaseEngine import BaseSession
from abc import ABCMeta, abstractmethod
from dao.TableModel.CustomerMaster import CustomerMaster
from dao.TableModel.BizConditionsMaster import BizConditionsMaster
from dao.TableModel.StockStatusMaster import StockStatusMaster
from dao.TableModel.MainProductMaster import MainProductMaster
from dao.TableModel.MainSupplierMaster import MainSupplierMaster


class ExecuteNonQuery_1(BaseSession):
    # Execute ClassのwapperClass
    def __init__(self, xldto, *args):
        super().__init__()
        self.p = args
        self.xldto = xldto
        self.querytype = self.__has_record()
        self.execute()

    def execute(self):
        self.querytype.execute(self.xldto)

    def __has_record(self):
        # if "Delete" in self.p:
        #     print(self.p)
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
            customer.bizconditions = BizConditionsMaster()
            customer.stockstatus = StockStatusMaster()
            customer.mainsupplier = MainSupplierMaster()
            customer.mainproduct = MainProductMaster()
            customer.set_data(xldto)
            customer.bizconditions.set_data(xldto)
            customer.stockstatus.set_data(xldto)
            customer.mainsupplier.set_data(xldto)
            customer.mainproduct.set_data(xldto)

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
                update_customer.bizconditions.set_data(xldto)
                update_customer.stockstatus.set_data(xldto)
                update_customer.mainsupplier.set_data(xldto)
                update_customer.mainproduct.set_data(xldto)
        except Exception as e:
            print(e)


class DeleteAll():
    def __init__(self):
        # super().__init__()
        self.basesession = BaseSession()
        try:
            with self.basesession.transaction() as session:
                del_list = self.basesession.session.query(CustomerMaster).all()
                for item in del_list:
                    self.basesession.session.delete(item)

        except Exception as e:
            print(e)


class SelectAll(BaseSession):
    def __init__(self):
        super().__init__()
        self.result = None
        self.search()

    def search(self):
        self.result = self.session.query(CustomerMaster).all()
        return self.result


class Delete(Excecute, BaseSession):
    pass

if __name__ == "__main__":
    DeleteAll()