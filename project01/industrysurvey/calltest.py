from sample.abscustomermstrdto_copy import DataCls
from abstractdto.abs_excel_sheet_dto import AbstractExcelSheetDTO

from dataclasses import asdict
def main(param):
    data = DataCls()
    data.customerCd=param
    print(data.customerCd)

if __name__ == "__main__":
    data = AbstractExcelSheetDTO()
    # data.xlCustomerCd = 12345
    # data.xlEmployees=12
    for k, v in data.__dict__.items():
        print(k,v)

    print(type(data.xlCustomerCd))




    # filename = "C:\\Users\\m-hara\\Desktop\\取引先コード取得済\\業態調査票（㈱八木熊）.xlsx"
    # filename = ["C:\\Users\\m-hara\\Desktop\\取引先コード取得済\\業態調査票（㈱八木熊）.xlsx", \
    #             "C:\\Users\\m-hara\\Desktop\\取引先コード取得済\業態調査票（イヌイ株式会社）.xlsx"]
    # app = ExcelApp().app
    # wb = ExcelWorkBook()
    # wb.open_wb(app,filename)


