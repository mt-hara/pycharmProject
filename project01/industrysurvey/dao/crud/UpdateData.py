from dao.BaseEngine import BaseSession, MetaBase
from dao.tablemodel.CustomerMaster import CustomerMaster
# from dao.tablemodel.StockStatusMaster import StockStatusMaster

# class Update(DataProsessing):
#     def InsOrUpdate(self, xldto):
#         UpdateData(xldto)
#         try:
#             with self.transaction() as session:
#                 update_customer = self.session.query(CustomerMaster).filter(CustomerMaster.customerCd == xldto.xlCustomerCd).first()
#                 update_customer.set_data(xldto)
#                 update_customer.stockstatus.set_data(xldto)
#         except Exception as e:
#             print(e)

class UpdateData(BaseSession):
    def __init__(self, xldto):
        super().__init__()
        self.ExecuteUpdate(xldto)


    def ExecuteUpdate(self,xldto):
        try:
            with self.transaction() as session:
                update_customer = self.session.query(CustomerMaster).filter(CustomerMaster.customerCd == xldto.xlCustomerCd).first()
                update_customer.set_data(xldto)
                update_customer.stockstatus.set_data(xldto)
        except Exception as e:
            print(e)
