import sys
import traceback
from excelapp.ExcelApp import ExcelApp, ExcelWorkBook
from dto.ExcelSheetDTO import ExcelSheetDTO
from excelapp.shapeState import ShapesPosToValue


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
    filename = "C:\\Users\\m-hara\\Desktop\\取引先コード取得済\\業態調査票（（株）清和光学製作所）.xlsx"
    excls = main(filename)
    ws = excls.ws
    # shape_dto = ShapesDto()
    # shapeposcls = ExcelShapePosition(ws)
    # shapes_pos_value = shapeposcls.shapes_position()
    # shape_pos_cls = ExcelShapePosition(ws)
    # shape_pos = shape_pos_cls.shapes_pos
    # ConvertPosToValue(shape_dto, shape_pos)
    # pos_to_val_cls.set_shapes_data()

    try:
        data = ExcelSheetDTO(ws)
    except AttributeError as e:
        type_, value, traceback_ = sys.exc_info()
        print(traceback.format_exception(type_, value, traceback_))
        excls.close()
        quit()
    else:
        print("biztype : {}".format(data.xlCustomerBizType))
        print("capitalform : {}".format(data.xlCapitalForm))
        print("corptype : {}".format(data.xlCorporateType))
        print("stockstatus : {}".format(data.xlStockListingStatus))
        print("stockmarket : {}".format(data.xlStockMarket))
        print("iso9001certif : {}".format(data.xlISO9001Certif))
        print("iso9000plan : {}".format(data.xlISO9001Plan))
        print("iso19001nocertif : {}".format(data.xlISO9001NoCertif))
        print("iso14001certif : {}".format(data.xlISO14001Certif))
        print("iso14001plan : {}".format(data.xlISO14001Plan))
        print("iso14001nocertif : {}".format(data.xlISO14001NoCertif))

        print("=====================================================")
        for x, y in data.shapes_dto.__dict__.items():
            print("{}:{}".format(x, y))
    # for x1, y1 in shape_dto.__dict__.items():
    #     print("{}:{}".format(x1, y1))

    # v = ShapesPosToValue(ws)
    # shape_list = v.pos_list()
    # for x in shape_list:
    #     print(x)

    # x = v.shapes_dto
    # print(x.shCustomerBizType)
    # for v,k in x.__dict__.items():
    #     print("{}:{}".format(v,k))


    # result = shapeposcls.shapes_position(ws)
    # for i in result:
    #     print(i)

    # posvalcls = ShapePosToValue(shape_dto)
    # posvalcls.set_shapes_data(result)
    print("finish")
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
