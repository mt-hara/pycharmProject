import collections.abc
from dto.DTOTest import DTOTest

class ItemShelf(collections.abc.Iterable):
    def __init__(self):
        self.__items = []

    def getitemat(self, index):
        return self.__items[index]

    def appenditem(self,item):
        self.__items.append(item)

    def __len__(self):
        return len(self.__items)

    def __iter__(self):
        return ItemShelfIterator(self)


class ItemShelfIterator(collections.abc.Iterator):

    __index = 0

    def __init__(self,itemshelf):
        self.__itemshelf = itemshelf

    def __next__(self):
        try:
            ret = self.__itemshelf.getitemat(self.__index)
            self.__index += 1
            return ret
        except IndexError:
            raise StopIteration


if __name__ == "__main__":
    item_shelf = ItemShelf()
    item_shelf.appenditem(DTOTest(1,"test1"))
    item_shelf.appenditem(DTOTest(2,"test2"))


    for item in item_shelf:
        print(id(item))
