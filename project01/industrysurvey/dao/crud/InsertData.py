from dao.BaseEngine import BaseSession, MetaBase
from dao.tablemodel.CustomerMaster import CustomerMaster
from dao.tablemodel.StockStatusMaster import StockStatusMaster
from dao.crud.ExecuteInterface import Excecute


class Insert(Excecute):
    def __init__(self,xldto):
        super().__init__()

    def execute(self,xldto):
        print("Insert")

    # def execute(self, state_context):
    #     try:
    #         customer = CustomerMaster()
    #         customer.stockstatus = StockStatusMaster()
    #         customer.set_data(self.xldto)
    #         customer.stockstatus.set_data(self.xldto)
    #         with self.transaction() as sesstion:
    #             self.session.add(customer)
    #     except Exception as e:
    #         print(e)


#     def InsOrUpdate(self, xldto):
#         InsertData(xldto)
#         try:
#             customer = CustomerMaster()
#             customer.stockstatus = StockStatusMaster()
#             customer.set_data(xldto)
#             customer.stockstatus.set_data(xldto)
#
#             with self.transaction() as sesstion:
#                 self.session.add(customer)
#         except Exception as e:
#             print(e)
#
#
# class InsertData(BaseSession):
#     def __init__(self, xldto):
#         super().__init__()
#         self.ExceuteInstert(xldto)
#
#     def ExceuteInstert(self, xldto):
#         try:
#             customer = CustomerMaster()
#             customer.stockstatus = StockStatusMaster()
#             customer.set_data(xldto)
#             customer.stockstatus.set_data(xldto)
#
#             with self.transaction() as sesstion:
#                 self.session.add(customer)
#         except Exception as e:
#             print(e)
