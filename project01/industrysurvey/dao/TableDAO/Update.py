from dao.TableModel.CustomerMaster import CustomerMaster
from dao.BaseEngine import BaseSession
from dao.TableDAO.InterfaceQueryExecute import IQueryExecute

class Update(IQueryExecute, BaseSession):
    def execute(self, xldto):
        try:
            with self.transaction() as session:
                update_customer = self.session.query(CustomerMaster).filter(CustomerMaster.customerCd == xldto.xlCustomerCd).first()
                update_customer.set_data(xldto)
                update_customer.bizconditions.set_data(xldto)
                # update_customer.stockstatus.set_data(xldto)
                # update_customer.mainsupplier.set_data(xldto)
                # update_customer.mainproduct.set_data(xldto)
        except Exception as e:
            print(e)