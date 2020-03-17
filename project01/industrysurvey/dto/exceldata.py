from dto.excelbase import AbsExcelApp
from dto.excelbase import AbsExcelWorkBook
import dataclasses


class ExcelData():
    def __init__(self, app, filepath):
        self.wb = AbsExcelWorkBook(app, filepath)
        self.ws = self.wb.xlws
        # self.customercd = ""
        # self.customername = ""
        self.customermaster = CustomerMaster
        self.get_exdata()

    def get_exdata(self):
        self.customermaster.CustomerCd = str(self.ws.range("H3").value)
        self.customermaster.CustomerName = self.ws.range("H5").value
        self.customermaster.CustomerKanaName=self.ws.range("H4").value

@dataclasses.dataclass
class CustomerMaster:
    CustomerCd: str
    # ringino: str
    CustomerName: str
    CustomerKanaName: str #H4
    CustomerShortName: str #""
    # excludeLaw: bool
    # headOfficeZipCd: str
    # headOfficeAddress1: str
    # headOfficeAddress2: str
    # headOfficeTel: str
    # headOfficeFax: str
    # BranchOfficeZipCd: str
    # BranchOfficeAddress1: str
    # BranchOfficeAddress2: str
    # BranchOfficeTel: str
    # BranchOfficeFax: str
    # repName: str
    # repKanaName: str
    # repJobTitle: str
    # repBirthday: str
    # employees: int
    # employeeMonth: int
    # employeeYear: int
    # CapitalForm: int
    # CorporateType: int
    # OtherCorpType: str
    # establishedMonth: int
    # establishedYear: int
    # AccountClosingMonth: int
    # ReturnOnEquity: float
    # ISO9001Certif: str
    # ISO9001ResistedNo: str
    # ISO9001CertifPlanYM: str
    # ISO14001Certif: str
    # ISO14001ResistedNo: str
    # ISO14001CertifPlanYM: str
    # OtherCertif:str
    # CustomerCategory: str
    # CustomerBizType: int
    # picName: str
    # picKanaName: str
    # PicEmailAddress: str
    # picDept: str
    # picPosition: str
    # sameHeadOffice: bool
    # contactZipCd: str
    # contactAddress1: str
    # contactAddress2: str
    # contactTel: str
    # contactFax: str
    # contactInfo: str


if __name__ == "__main__":
    xlapp = AbsExcelApp()
    filename = "C:\\Users\\m-hara\\Desktop\\取引先コード取得済\\業態調査票（（株）清和光学製作所）.xlsx"
    xlbook = ExcelData(xlapp.app, filename)
    # var = xlbook.ws.name
    # print(var)
    # print(xlbook.customercd)
    # print(xlbook.customername)
    print(xlbook.customermaster.CustomerCd)
    print(xlbook.customermaster.CustomerName)
    print(xlbook.customermaster.CustomerKanaName)
    xlapp.close_app()
