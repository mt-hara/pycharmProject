from dao.TableModel.CustomerMaster import CustomerMaster
from dao.TableModel.BizConditionsMaster import BizConditionsMaster
from dao.TableModel.StockStatusMaster import StockStatusMaster
from dao.TableModel.MainProductMaster import MainProductMaster
from dao.TableModel.MainSupplierMaster import MainSupplierMaster
from dao.BaseEngine import BaseSession
from dao.TableDAO.InterfaceQueryExecute import IQueryExecute

class Instert(IQueryExecute, BaseSession):
    def execute(self, xldto):
        try:
            customer = CustomerMaster()
            # customer.create_relationship()
            customer.bizconditions = BizConditionsMaster()
            # customer.stockstatus = StockStatusMaster()
            # customer.mainsupplier = MainSupplierMaster()
            # customer.mainproduct = MainProductMaster()
            customer.set_data(xldto)
            customer.bizconditions.set_data(xldto)
            # customer.stockstatus.set_data(xldto)
            # customer.mainsupplier.set_data(xldto)
            # customer.mainproduct.set_data(xldto)

            with self.transaction() as session:
                self.session.add(customer)

        except Exception as e:
            print(e)
