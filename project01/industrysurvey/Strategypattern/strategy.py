from abc import ABCMeta, abstractmethod

class Strategy(metaclass=ABCMeta):
    @abstractmethod
    def nextHand(self):
        pass

    @abstractmethod
    def study(self, win):
        pass

