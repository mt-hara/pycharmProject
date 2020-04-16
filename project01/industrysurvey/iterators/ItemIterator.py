from abc import ABCMeta, abstractmethod
from dto.DTOTest import DTOTest

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

# if __name__ == "__main__":
#     item_shelf = ItemShelf()
#     item_shelf.append(DTOTest(1, "test1"))
#     item_shelf.append(DTOTest(2, "test2"))
#     item_shelf.append(DTOTest(3, "test3"))
#     item_shelf.append(DTOTest(4, "test4"))
#     it = item_shelf.iterator()
#     i = 0
#     while it.hasnext():
#         i = i +1
#         item = it.next()
#         print("{}:number = {} : name = {}".format(i,item.number,item.name))
