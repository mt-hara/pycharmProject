import sys
import traceback
import pathlib
# import logging
# LogModule = logging.getLogger(__name__)

_log_file= "/LogModule"
class ErrorTest():
    def __init__(self):
        pass

    def raise_error(self):
        try:
            raise AttributeError
        except Exception as e:
            # type_, value, traceback_ = sys.exc_info()
            # print(traceback.format_exception(type_, value, traceback_))
            raise



class Main():

    def __init__(self):
        # logging.debug("DEBUG")
        self.err= ErrorTest()

    def err_test(self):
        _log_file_path = pathlib.Path(_log_file) / "LogModule.LogModule"
        # _log_file_path = tmp / "LogModule.LogModule"
        try:
            self.err.raise_error()
        except AttributeError as e:

            type_, value, traceback_ = sys.exc_info()
            indata=str(traceback.format_exception(type_, value, traceback_))
            with open(_log_file_path, "a", encoding="utf-8") as f:
                f.write(indata)
            # logging.exception(traceback.format_exception(type_, value, traceback_))





if __name__ == "__main__":
    c = Main()
    c.err_test()
