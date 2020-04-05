import collections.abc

class Book():
    def __init__(self, name):
        self.name = name

    def getname(self):
        return self.name

class BookShelf(collections.abc.Iterable):
    def __init__(self):
        self.__books = []

    def getbookat(self, index):
        return self.__books[index]

    def appendbook(self, book):
        self.__books.append(book)

    def __len__(self):
        return len(self.__books)

    def __iter__(self):
        return BookShelfIterator(self)


class BookShelfIterator(collections.abc.Iterator):
    __index = 0
    def __init__(self, bookshelf):
        self.__bookshelf = bookshelf

    def __next__(self):
        try:
            ret = self.__bookshelf.getbookat(self.__index)
            self.__index += 1
            return ret
        except IndexError:
            raise StopIteration

if __name__ == '__main__':
    bookshelf = BookShelf()
    bookshelf.appendbook(Book("ドラえもん"))
    bookshelf.appendbook(Book("パーマン"))
    bookshelf.appendbook(Book("キテレツ大百科"))
    bookshelf.appendbook(Book("オバケのQ太郎"))

    for book in bookshelf:
        print(book.getname())
    for book in bookshelf:
        print(book.getname())