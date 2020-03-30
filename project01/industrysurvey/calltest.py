from sample.abscustomermstrdto_copy import DataCls
from dataclasses import asdict
def main(param):
    data = DataCls()
    data.customerCd=param
    print(data.customerCd)

if __name__ == "__main__":
    data1=DataCls()
    data1.customerCd="123"
    data2= DataCls()
    data2.customerCd="AAA"
    print(asdict(data1))
    print(asdict(data2))
    print(id(data1))
    print(id(data2))




    # filename = "C:\\Users\\m-hara\\Desktop\\取引先コード取得済\\業態調査票（㈱八木熊）.xlsx"
    # filename = ["C:\\Users\\m-hara\\Desktop\\取引先コード取得済\\業態調査票（㈱八木熊）.xlsx", \
    #             "C:\\Users\\m-hara\\Desktop\\取引先コード取得済\業態調査票（イヌイ株式会社）.xlsx"]
    # app = ExcelApp().app
    # wb = ExcelWorkBook()
    # wb.open_wb(app,filename)


