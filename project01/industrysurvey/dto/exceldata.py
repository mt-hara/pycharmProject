from dto.excelbase import AbsExcelApp
from dto.excelbase import AbsExcelWorkBook
import dataclasses

class ExcelData():
    def __init__(self, app, filepath):
        self.wb = AbsExcelWorkBook(app, filepath)
        self.ws = self.wb.xlws

@dataclasses.dataclass
class CustomerMaster:
    customercd : str
    ringino : str
    customername : str
    CustomerShortName : str
    excludeLaw : bool
    headOfficeZipCd : str
    headOfficeAddress1 : str
    headOfficeAddress2 : str
    headOfficeTel : str
    headOfficeFax : str
    BranchOfficeZipCd : str
    BranchOfficeAddress1 : str
    BranchOfficeAddress2 : str
    BranchOfficeTel : str
    BranchOfficeFax : str
    repName : str
    repKanaName : str
    repJobTitle : str
    repBirthday :str


if __name__ == "__main__":
    xlapp = AbsExcelApp()
    filename = "C:\\Users\\m-hara\\Desktop\\取引先コード取得済\\業態調査票（（株）清和光学製作所）.xlsx"
    xlbook = ExcelData(xlapp.app, filename)
    var = xlbook.ws.name
    print(var)
    xlapp.close_app()