from excelapp.concreteexcel import ExcelApp, ExcelWorkBook
from excelapp.shape_state import GetExcelShapePos,ShapePosToValue
from dto.excel_sheet_dto import ExcelSheetDTO
from dto.shapes_dto import ShapesDto


class main():
    def __init__(self, filename):
        self.baseapp = ExcelApp()
        self.app = self.baseapp.app
        self.wb = ExcelWorkBook()
        self.wb.open_wb(self.app, filename)
        self.ws = self.wb.xlws

    def close(self):
        self.wb.close_workbook()
        self.baseapp.close_App()

    # @property
    # def ws(self):
    #     return self.ws
    #
    # @ws.setter
    # def ws(self,param):
    #     self.ws = param


# def myfunc(filername):
#     baseapp = ExcelApp()
#     app = baseapp.app
#
#     wb = ExcelWorkBook()
#     wb.open_wb(app,filename)
#     ws = wb.xlws
#
#     # Shapeポジション取得
#     shapes_pos = ExcelShapePos(ws)
#     sheet_dto = ExcelSheetDTO(ws)
#
#
#     # Shapes_posから選択値を取得



if __name__ == "__main__":
    filename = "C:\\Users\\m-hara\\Desktop\\取引先コード取得済\\業態調査票（ＮＣＤ NakajimaControlDesign）.xlsx"
    excls = main(filename)
    ws = excls.ws
    data = ExcelSheetDTO(ws)
    shape_dto = ShapesDto()

    shapeposcls = GetExcelShapePos()
    result = shapeposcls.shapes_position(ws)
    # for i in result:
    #     print(i)

    posvalcls = ShapePosToValue(shape_dto)
    posvalcls.set_shapes_data(result)
    print(shape_dto.shCustomerBizType)
    print(shape_dto.shCapitalForm)
    print(shape_dto.shCorporateType)
    # for x in r:
    #     print(x)

    # data.xlCustomerCd = "12345"
    # data.xlCustomerName = "test name"
    # for k, v in data.__dict__.items():
    #     print(k,v)

    # print(data.xlCustomerCd)
    # print(data.xlCustomerName)

    excls.close()

    # filename = "C:\\Users\\m-hara\\Desktop\\取引先コード取得済\\業態調査票（㈱八木熊）.xlsx"
    # filename = ["C:\\Users\\m-hara\\Desktop\\取引先コード取得済\\業態調査票（㈱八木熊）.xlsx", \
    #             "C:\\Users\\m-hara\\Desktop\\取引先コード取得済\業態調査票（イヌイ株式会社）.xlsx"]
    # app = ExcelApp().app
    # wb = ExcelWorkBook()
    # wb.open_wb(app,filename)
