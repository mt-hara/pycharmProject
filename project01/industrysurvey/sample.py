from abc import ABCMeta, abstractmethod

class Print(metaclass=ABCMeta):
    @abstractmethod
    def printWeak(self):
        pass

    @abstractmethod
    def printString(self):
        pass

class Bunner():
    """
    適合される側
    """
    def __init__(self, string):
        self.__string = string

    def showWithParen(self):
        print("({0})".format(self.__string))

    def showWithAster(self):
        print("*{0}*".format(self.__string))

class PrintBanner(Bunner,Print):
    """
    適合する側
    """
    def __init__(self, string):
        super(PrintBanner, self).__init__(string)

    def printWeak(self):
        self.showWithParen()

    def printString(self):
        self.showWithAster()

def startMain():
    p = PrintBanner("Hello")
    p.printWeak()
    p.printString()

if __name__ == "__main__":
    startMain()