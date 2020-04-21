import sys
import traceback
class ErrorTest():
    def __init__(self):
        pass

    def raise_error(self):
        try:
            raise AttributeError
        except AttributeError as e:
            raise



class Main():
    def __init__(self):
        self.err= ErrorTest()

    def err_test(self):
        try:
            self.err.raise_error()
        except AttributeError as e:
            type_, value, traceback_ = sys.exc_info()
            print(traceback.format_exception(type_, value, traceback_))





if __name__ == "__main__":
    c = Main()
    c.err_test()
