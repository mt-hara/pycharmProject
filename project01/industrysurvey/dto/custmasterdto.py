from dataclasses import dataclass, fields, asdict, astuple
from excelcls.concexcel import ConcExcelApp
from excelcls.concexcel import ConcExcelWorkBook

@dataclass
class CustomerMaster(ConcExcelWorkBook):
    def __init__(self, app, filepath):
        super().__init__(app, filepath)
        self.set_data(self.ws)

    CustomerCd: str = ""
    ringNo: str = ""
    CustomerName: str = ""
    CustomerKanaName: str = ""
    CustomerShortName: str = ""
    excludeLaw: bool = False
    headOfficeZipCd: str = ""
    headOfficeAddress1: str = ""
    headOfficeAddress2: str = ""
    headOfficeTel: str = ""
    headOfficeFax: str = ""
    BranchOfficeZipCd: str = ""
    BranchOfficeAddress1: str = ""
    BranchOfficeAddress2: str = ""
    BranchOfficeTel: str = ""
    BranchOfficeFax: str = ""
    repName: str = ""
    repKanaName: str = ""
    repJobTitle: str = ""
    repBirthday: str = ""
    employees: int = None
    employeeMonth: int = None
    employeeYear: int = None
    CapitalForm: int = None
    CorporateType: int = None
    OtherCorpType: str = ""
    establishedMonth: int = None
    establishedYear: int = None
    AccountClosingMonth: int = None
    ReturnOnEquity: float = None
    ISO9001Certif: str = ""
    ISO9001ResistedNo: str = ""
    ISO9001CertifPlanYM: str = ""
    ISO14001Certif: str = ""
    ISO14001ResistedNo: str = ""
    ISO14001CertifPlanYM: str = ""
    OtherCertif: str = ""
    CustomerCategory: str = ""
    CustomerBizType: int = None
    picName: str = ""
    picKanaName: str = ""
    PicEmailAddress: str = ""
    picDept: str = ""
    picPosition: str = ""
    sameHeadOffice: bool = False
    contactZipCd: str = ""
    contactAddress1: str = ""
    contactAddress2: str = ""
    contactTel: str = ""
    contactFax: str = ""
    contactInfo: str = ""


    def set_data(self, ws):
        self.CustomerCd = ws.range("H3").value
        self.CustomerName = ws.range("H5").value
        self.CustomerKanaName = ws.range("H4").value
        self.employees = int(ws.range("K22").value)





if __name__ == "__main__":
    xlapp = ConcExcelApp()
    filename = "C:\\Users\\m-hara\\Desktop\\取引先コード取得済\\業態調査票（㈱八木熊）.xlsx"

    mst = CustomerMaster(xlapp.app,filename)

    print(repr(mst))

    mst.wb_close()
    xlapp.close_app()

