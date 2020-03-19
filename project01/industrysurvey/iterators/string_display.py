from iterators.abstract_display import AbstractDisplay

class StringDisplay(AbstractDisplay):

    def __init__(self,string: str):
        self.___string = string
        self.__width = len(string.encode('utf-8'))

    def open(self):
        self.print_line()

    def print(self):
        print('|%s|' % self.___string)

    def close(self):
        self.print_line()

    def print_line(self):
        print("+" , end = '')
        for i in range(self.__width):
            print("-" , end = '')
        print("+")

if __name__ == "__main__":
    sdisp = StringDisplay("Hello World.")
    sdisp.display()