from dao.BaseEngine import BaseSession, MetaBase
from abc import ABCMeta, abstractmethod
from typing import Dict, Any
from dao.TableModel.CustomerMaster import CustomerMaster
from dao.TableModel.StockStatusMaster import StockStatusMaster
# from dao.crud.InsertData import Insert
# from dao.crud.UpdateData import Update

class IExecuteState(BaseSession, metaclass=ABCMeta):
    @abstractmethod
    def execute(self, state_context):
        pass

class ConcExecuteState(IExecuteState):
    def __init__(self, xldto):
        super().__init__()
        self.xldto =xldto

    def execute(self, state_context):
        pass


class StateContext():
    def __init__(self, state_type):
        self.set_state(state_type)

    @property
    def curt_state(self):
        return self.__curt_state

    @curt_state.setter
    def curt_state(self, obj):
        self.__curt_state = obj

    def set_state(self, new_state):
        self.__curt_state = new_state

    def excecute(self):
        self.curt_state.execute(self)


class SetContext():
    def __init__(self, xldto):
        self.xldto = xldto
        self.exectype = self._set_concrete_state()

    def _set_concrete_state(self):
        base = BaseSession()
        param = self.xldto.xlCustomerCd
        result = base.session.query(CustomerMaster).filter(CustomerMaster.customerCd == param).all()
        if len(result) == 0:
            return Insert(self.xldto)
        else:
            return Update(self.xldto)


class ExecuteNonQuery():
    def __init__(self, xldto):
        self.xldto = xldto
        self.create_context()

    def create_context(self):
        state_factory = SetContext(self.xldto)
        concrete_state = state_factory.exectype
        state = StateContext(concrete_state)
        state.excecute()


class Insert(ConcExecuteState):
    def __init__(self,xldto):
        super().__init__(xldto)

    def execute(self, state_context):
        try:
            customer = CustomerMaster()
            customer.stockstatus = StockStatusMaster()
            customer.set_data(self.xldto)
            customer.stockstatus.set_data(self.xldto)
            with self.transaction() as sesstion:
                self.session.add(customer)
        except Exception as e:
            print(e)

class Update(ConcExecuteState):
    def __init__(self, xldto):
        super().__init__(xldto)

    def execute(self, state_context):
        try:
            with self.transaction() as session:
                update_customer = self.session.query(CustomerMaster).filter(CustomerMaster.customerCd == self.xldto.xlCustomerCd).first()
                update_customer.set_data(self.xldto)
                update_customer.stockstatus.set_data(self.xldto)
        except Exception as e:
            print(e)


# class SubExecuteNonQuery():
#     # SelectOparationクラスのラッパークラス
#     def __init__(self, xldao):
#         self.xldao = xldao
#         self.select_init()
#         self.select_execute()
#
#     def select_init(self):
#         self.select_operation = SelectOperation(self.xldao)
#
#     def select_execute(self):
#         self.select_operation.InsOrUpdate()
#
#
# class SelectOperation():
#     def __init__(self, xldao):
#         self.xldao = xldao
#         self.querytype = chose_context(self.xldao)
#
#     def InsOrUpdate(self):
#         self.querytype.InsOrUpdate(self.xldao)
#
#
# def chose_context(xldto):
#     base = BaseSession()
#     param = xldto.xlCustomerCd
#     result = base.session.query(CustomerMaster).filter(CustomerMaster.customerCd == param).all()
#     if len(result) == 0:
#         # return Insert()
#         pass
#     else:
#         # return Update()
#         pass

#
# class DataProsessing(BaseSession,metaclass=ABCMeta):
#     @abstractmethod
#     def InsOrUpdate(self, xldto):
#         pass


# class Insert(DataProsessing):
#     def InsOrUpdate(self, xldto):
#         InsertData(xldto)
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


# class Update(DataProsessing):
#     def InsOrUpdate(self, xldto):
#         UpdateData(xldto)
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