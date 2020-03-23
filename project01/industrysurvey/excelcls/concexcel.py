import xlwings as xlw
import tkinter
import tkinter.messagebox as msgbox
from excelcls.absexcel import AbstractExcelApp
from excelcls.absexcel import AbstractExcelWorkBook


root = tkinter.Tk()
root.withdraw()


class concExcelApp(AbstractExcelApp):
    def __init__(self):
        super().__init__()
        self.instwb = concExcelworkBook()

    def get_wb(self, filepath):
        # self.xlwb = concExcelworkBook().open_wb(self.app,filepath)
        self.instwb.open_wb(self.app,filepath)

    def close_wb(self):
        self.instwb.close_wb()

    def select_sheet(self):
        self.instwb.select_sheet()

class concExcelworkBook(AbstractExcelWorkBook):
    def __init__(self):
        super().__init__()

    @classmethod
    def ret_xlwb(cls):
        return cls.exlwb

    def open_wb(self, app, filepath):
        try:
            self.xlwb = app.books.open(filepath)
        except AttributeError:
            msgbox.showinfo("エラー", "ファイル読み込みエラー")
            exit(0)

    def close_wb(self):
        self.xlwb.close()

    def select_sheet(self):
        self.xlws = self.xlwb.sheets[0]


if __name__ == "__main__":
    # filename = ["C:\\Users\\m-hara\\Desktop\\取引先コード取得済\\業態調査票（㈱八木熊）.xlsx", \
    #             "C:\\Users\\m-hara\\Desktop\\取引先コード取得済\業態調査票（イヌイ株式会社）.xlsx"]
    filename = "C:\\Users\\m-hara\\Desktop\\取引先コード取得済\\業態調査票（㈱八木熊）.xlsx"

    app = concExcelApp()
    app.get_wb(filename)
    app.select_sheet()
    print(app.instwb.xlws.range("H5").value)



    #     app.close_wb()
    # app.close_app()