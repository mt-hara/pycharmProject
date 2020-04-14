from abc import ABCMeta,abstractmethod

class IQueryExecute(metaclass=ABCMeta):
    @abstractmethod
    def execute(self, xldto):
        pass