import xlwings as xlw
import tkinter
import tkinter.messagebox as msgbox
from excelcls.absexcel import AbstractExcelApp
from excelcls.absexcel import AbstractExcelWorkBook

root = tkinter.Tk()
root.withdraw()


class ConcExcelApp(AbstractExcelApp):
    def __init__(self):
        super().__init__()
        self.wbinst = None


    def get_wb(self, filepath):
        self.wbinst = ConcExcelworkBook()
        self.wbinst.open_wb(self.app, filepath)

    def close_wb(self):
        pass


class ConcExcelworkBook(AbstractExcelWorkBook):
    def __init__(self):
        super().__init__()

    def open_wb(self, app,filepath):
        try:
            self.xlwb = app.books.open(filepath)
            global inch
            inch = self.xlwb
        except AttributeError:
            msgbox.showinfo("エラー", "ファイル読み込みエラー")
            exit(0)
        else:
            self.select_sheet()
            return self.xlwb

    def select_sheet(self):
        try:
            self.xlws = self.xlwb.sheets[0]
        except AttributeError:
            msgbox.showinfo("エラー", "シート読み込みエラー")
            exit(0)

    def close_wb(self):
        self.xlwb.close()





if __name__ == "__main__":
    # filename = ["C:\\Users\\m-hara\\Desktop\\取引先コード取得済\\業態調査票（㈱八木熊）.xlsx", \
    #             "C:\\Users\\m-hara\\Desktop\\取引先コード取得済\業態調査票（イヌイ株式会社）.xlsx"]
    filename = "C:\\Users\\m-hara\\Desktop\\取引先コード取得済\\業態調査票（㈱八木熊）.xlsx"

    app = ConcExcelApp()
    # for i in filename:
    #     app.get_wb(i)
        # app.close_wb()
    app.get_wb(filename)


