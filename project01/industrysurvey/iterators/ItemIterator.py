from abc import ABCMeta, abstractmethod


class Aggregate(metaclass=ABCMeta):
    @abstractmethod
    def iterator(self):
        pass


class Iterator(metaclass=ABCMeta):
    @abstractmethod
    def hasnext(self) -> bool:
        pass

    @abstractmethod
    def next(self) -> object:
        pass


class ItemShelfItetator(Iterator):
    def __init__(self,ItemShelf):
        self.__itemshelf = ItemShelf
        self.__index = 0

    def hasnext(self) -> bool:
        if self.__index < self.__itemshelf.getlength():
            return True
        else:
            return False

    def next(self) -> object:
        item = self.__itemshelf.getitemat(self.__index)
        self.__index += 1
        return item

    def get_length(self):
        return  self.__itemshelf.getlength()


class ItemShelf(Aggregate):
    def __init__(self):
        self.__items = []
        self.__last = 0

    def getitemat(self, index):
        return self.__items[index]

    def append(self, item):
        self.__items.append(item)
        # self.__items[self.__last] = item
        self.__last += 1

    def getlength(self):
        return self.__last

    def iterator(self):
        return ItemShelfItetator(self)