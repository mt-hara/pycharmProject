from dao.TableModel.AllCustomerMaster import AllCustomerMaster
from dao.BaseEngine import BaseSession
from dao.TableDAO.InterfaceQueryExecute import IQueryExecute

class InsertAll(IQueryExecute, BaseSession):
    def execute(self, xldto):
        try:
            customerall= AllCustomerMaster()
            customerall.set_data(xldto)
            with self.transaction() as session:
                session.add(customerall)

        except Exception as e:
            print(e)