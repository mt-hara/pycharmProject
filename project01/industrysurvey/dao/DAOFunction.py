import re


class YearMonthGenerator():
    def __init__(self, year, month):
        self.year = year
        self.month = month

    # @property
    # def year(self):

    def year_month(self):
        if (self.year is not None) and (self.month is not None):
            y_value = EraYearToADYear(self.year).ret_year
            result = str(y_value) + "年" + str(self.month) + "月"
            return result
        else:
            return None


class YearMonthDayGenerator(YearMonthGenerator):
    def __init__(self, year, month, day):
        super().__init__(year, month)
        self.day = day

    def year_month_day(self):
        if (self.year is not None) and (self.month is not None) and (self.day is not None):
            y_value = EraYearToADYear(self.year).ret_year
            result = str(y_value) + "年" + str(self.month) + "月" + str(self.day) + "日"
            return result
        else:
            return None


class EraYearToADYear():
    def __init__(self, year):
        self.cur_year = year
        self.ret_year = None
        self.era_to_ad()
        # self.return_result()

    def __get_year_value(self):
        return re.sub("\\D", "", self.cur_year)

    def era_to_ad(self):
        conv_year = self.__get_year_value()
        if len(conv_year) == 4:
            self.ret_year = conv_year
        else:
            era_val = re.search("\D+", self.cur_year).group()
            if era_val in ["大正", "T", "t"]:
                self.ret_year = str(1911 + int(conv_year))
            elif era_val in ["昭和", "S", "s"]:
                self.ret_year = str(1925 + int(conv_year))
            elif era_val in ["平成", "H", "h"]:
                self.ret_year = str(1988 + int(conv_year))
            elif era_val in ["令和", "R", "r"]:
                self.ret_year = str(2018 + int(conv_year))


class ISOCertifGenerator():
    def __init__(self, certif, plan, nocertif):
        self.certif = certif
        self.plan = plan
        self.nocertif = nocertif

    def certif_condition(self):
        if self.certif == "取得済":
            return "取得済"
        elif self.plan == "取得予定":
            return "取得予定"
        elif self.nocertif == "取得予定なし":
            return "取得予定なし"
        else:
            return ""

