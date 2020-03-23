from dataclasses import dataclass, fields, asdict, astuple
from excelcls.concreteexcel import ConcreateExcelWorkBook
from excelcls.concreteexcel import ExcelData


@dataclass
class CustomerMasterDTO:
    pass

@dataclass
class AllCustomerMaster:
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
    stockMarket: str=""
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

    def get_cell_data(self, ws):
        self.get_shape_data()
        self.CustomerCd: str = str(ws.range("H3").value)
        self.CustomerName: str = ws.range("H5").value
        self.CustomerKanaName: str = ws.range("H4").value
        self.employees: int = int(ws.range("K22").value)

    def get_shape_data(self):
        for dictval in self.sh_pos:
            top_pos: float = dictval["top"]
            left_pos: float = dictval["left"]

            # 業種分類 venderBizType
            # 1 メーカー |1
            # 2 商社 |2
            # 3 メーカー&商社 |3
            # 4 代理店 |4
            # 5 卸売 | 5
            # 6 その他 | 6
            if 210 < top_pos < 225:
                if  80 < left_pos < 125:
                    print("メーカー")
                elif 145 < left_pos < 190:
                    print("商社")
                elif 200 < left_pos < 285:
                    print("メーカー＆商社")
                elif 298 < left_pos < 350:
                    print("代理店")
                elif 360 < left_pos < 400:
                    print("卸売")
                elif 422 < left_pos < 445:
                    print("その他")
                else:
                    print("else")
            # 資本形態 CapitalForm
            #1 個人 | 個人 1
            #2 法人 | 法人 2
            #       | その他 9
            elif 222 < top_pos < 238:
                if 80 < left_pos < 125:
                    print("個人")
                else:
                    print("法人")
                    # CorporateType
                    # 1 株式会社 | 株式会社 1
                    # 2 有限会社 | 有限会社 2
                    # 3 その他 | その他 9
                    if 180 < left_pos < 235:
                        print("株式会社")
                    elif 240 < left_pos < 290:
                        print("有限会社")
                    elif 295 < left_pos < 400:
                        print("その他")
            # 上場区分 stockStatusId
            # 上場 | 1
            # 非上場 | 0
            elif 237 < top_pos < 253:
                if 340 < left_pos < 410:
                    print("非上場")
                else:
                    print("上場")
                    # stockMarket string
                    if 80 < left_pos < 125:
                        print("東証1部")
                    elif 150 < left_pos < 190:
                        print("東証2部")
                    elif 210 < left_pos < 300:
                        print("その他")
            # ISO認認証取得区分
            elif 690 < top_pos < 717:
                if 25.5 < left_pos < 100:
                    #ISO9001Certif
                    print("ISO9000取得済み")
                elif 305 < left_pos < 390:
                    #ISO14001Certif
                    print("ISO14000取得済み")
            elif 720 < top_pos < 731:
                if 25.5 < top_pos < 100:
                    print("ISO9000取得予定")
                elif 305 < left_pos < 390:
                    print("ISO14000取得予定")
            elif 733 < top_pos < 747:
                if 25.5 < left_pos < 100:
                    print("ISO9000予定なし")
                elif 305 < left_pos < 390:
                    print("ISO14000予定なし")
            elif top_pos>800:
                pass

if __name__ == "__main__":
    # xlapp = ConApp()
    # filename = "C:\\Users\\m-hara\\Desktop\\取引先コード取得済\\業態調査票（㈱八木熊）.xlsx"
    filename = "C:\\Users\\m-hara\\Desktop\\取引先コード取得済\\業態調査表（ワタキューセイモア株式会社）.xlsx"

    # mst = CustomerMaster(xlapp.app, filename)

    # print(repr(mst))

    # for i in mst.sh_pos:
    #     print("top = " + str(i["top"]))
    #     print("left= " + str(i["left"]))
    #
    # mst.wb_close()
    # xlapp.close_app()
