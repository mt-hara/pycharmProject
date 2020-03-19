from iterators.abstract_display import AbstractDisplay

class CharDisplay(AbstractDisplay):

    def __init__(self, ch: str):
        if len(ch) >1:
            raise TypeError("文字は1文字")
        self.__ch = ch

    def open(self):
        print("<<", end = '')

    def print(self):
        print(self.__ch, end = '')

    def close(self):
        print(">>")

if __name__ == "__main__":
    d1 = CharDisplay('H')
    d1.display()