import sys
# from dao.BaseEngine import BaseEngine
from dao.BaseEngine import BaseSession, MetaBase
from dao.tablemodel.CustomerMaster import CustomerMaster
from dao.tablemodel.StockStatusMaster import StockStatusMaster
from abc import ABCMeta, abstractmethod


# from dao.TableModel.BizConditionsMaster import BizConditionsMaster
# from dao.TableModel.MainProductMaster import MainProductMaster
# from dao.TableModel.MainSupplierMaster import MainSupplierMaster


class TableMigration(BaseSession):
    def __init__(self):
        super().__init__()
        try:
            MetaBase().metadata.create_all(self.engine)
        except Exception as e:
            print(e)


# class AllCustomer(BaseSession):
#     def __init__(self):
#         super().__init__()
#
#     def has_record(self,param):
#         # with self.transaction() as session:
#         result = self.session.query(CustomerMaster).filter(CustomerMaster.CustomerCd == param).all()
#         if len(result) == 0:
#             return True
#         else:
#             return False
#
#     def select(self):
#         # with self.transaction() as session:
#         ret = self.session.query(CustomerMaster).all()
#         return ret
#
#     def insert(self, xldto):
#         if self.has_record(xldto.xlCustomerCd) is True:
#             with self.transaction() as session:
#                 customer = CustomerMaster(xldto)
#                 self.session.add(customer)
#                 # AllCustomerMaster().insert().values(CustomerCd = cd)
#                 # self.session.add(i)
#         else:
#             self.update(xldto)
#
#     def update(self,xldto):
#         print("Update")

# class Migration():
#     def __init__(self):
#         self.e = BaseEngine().engine
#
#     def CustomerMaster(self):
#         Base().metadata.create_all(self.e)

# strategy insterface
class DataProcessing(BaseSession, metaclass=ABCMeta):
    @abstractmethod
    def InsOrUpdate(self, xldto):
        pass


class ExecuteNoneQuery(BaseSession):
    def __init__(self, xldto):
        super().__init__()
        self.xldto = xldto
        self.querytype = self.__has_record()
        self.InsOrUpdate()

    def InsOrUpdate(self):
        self.querytype.InsOrUpdate(self, self.xldto)

    def __has_record(self):
        param = self.xldto.xlCustomerCd
        result = self.session.query(CustomerMaster).filter(CustomerMaster.customerCd == param).all()
        if len(result) == 0:
            return Insert
        else:
            return Update


class Insert(DataProcessing):
    def InsOrUpdate(self, xldto):
        try:
            customer = CustomerMaster()
            customer.stockstatus = StockStatusMaster()
            customer.set_data(xldto)
            customer.stockstatus.set_data(xldto)

            with self.transaction() as session:
                self.session.add(customer)
        except Exception as e:
            print(e)


class Update(DataProcessing):
    def InsOrUpdate(self, xldto):
        try:
            with self.transaction() as session:
                update_customer = self.session.query(CustomerMaster).filter(CustomerMaster.customerCd == xldto.xlCustomerCd).first()
                update_customer.set_data(xldto)
                update_customer.stockstatus.set_data(xldto)
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


if __name__ == "__main__":
    DeleteAll()
    # TableMigration()
    # t = ExecuteNoneQuery(123).has_record()
    # print(t)
    # cli = AllCustomer()
    # li = cli.select()
    # for i in li:
    #     for k, v in i.__dict__.items():
    #         print("{} = {}".format(k,v))
    # for i in li:
    #     for k, v in i:
    #         print("{} = {}".format(k,v))
    # cli.insert("12334", "test")

    # cli.select()
    # strfld = cli.like_select("シーシーエス")
    # print(str(strfld))
    # cli.update("001002",None)

# class Customers(BaseSession):
#     def __init__(self, dbpath):
#         super().__init__(dbpath)
#
#     def select(self):
#         with self.transaction() as session:
#             for i in self.session.query(CustomerData):
#                 print("id = {} : name = {}".format(i.customerCd, i.customerName))
#
#     def like_select(self, keyword):
#         with self.transaction() as session:
#             for i in self.session.query(CustomerData).filter(CustomerData.customerName.like('%' +
#                                                                                             keyword + '%')):
#                 return i.customerCd
#
#     def update(self, keyword, param):
#         with self.transaction() as session:
#             i = self.session.query(CustomerData).filter(CustomerData.customerCd ==
#                                                         keyword).first()
#             print(":{}:{}:{}".format(i.customerCd, i.customerName, i.fld1))
#             i.fld1 = param
#             print(":{}:{}:{}".format(i.customerCd, i.customerName, i.fld1))
