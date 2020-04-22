from dao.TableModel.AllCustomerMaster import AllCustomerMaster
from dao.BaseEngine import BaseSession
from dao.TableDAO.InterfaceQueryExecute import IQueryExecute

class UpdateAll(IQueryExecute, BaseSession):
    def execute(self, xldto):
        try:
            with self.transaction() as session:
                update_customerall = session.query(AllCustomerMaster).filter(AllCustomerMaster.customerCd == xldto.xlCustomerCd).first()
                update_customerall.set_data(xldto)
        except Exception as e:
            raise