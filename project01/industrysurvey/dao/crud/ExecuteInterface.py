from abc import ABCMeta, abstractmethod

class Excecute(metaclass=ABCMeta):
    @abstractmethod
    def execute(self, xldto):
        pass