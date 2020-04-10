# s = '123456789'
# s1 = "123.45"
# s2 = "非公開"
import sys
import re
def check(val, valuetype):
    if valuetype == type(val):
        return val

    if valuetype == int:
        if type(val) is str:
            pass


    paramtype = type(val)
    if paramtype is str:
        if bool(re.compile("^\d+\.?\d*\Z").match(val)):
            try:
                result = int(val)
                return result
            except ValueError:
                result = float(val)
                return result
    else:
        return val


    def is_numeric(param):
        return bool(re.compile("^\d+\.?\d*\Z").match(param))

def conv_str_to_int(val):
    if type(val) == str:
        if not val.inumeric() == True:
            try:
                float(val)
                return float(val)
            except  ValueError:
                return None
        else:
            return int(val)
    return val

def ymd(year,month,day):
    if not ((year is None) and (month is None) and (day is None)):
        return year + "/" + month + "/" + day
    else:
        return "No Data"

def has_year(year):
    if year == None:
        return None

def is_ad_year(year):
    y_num =re.sub("\\D", "", year)
    return y_num

def era_to_ad(year):

    y_value = is_ad_year(year)
    if len(y_value) == 4:
        return y_value
    else:
        era_value = re.search("\D+", year).group()
        if era_value in ["大正", "T", "t"]:
            return str(1911 + int(y_value))
        elif era_value in ["昭和", "S", "s"]:
            return str(1925 + int(y_value))
        elif era_value in["平成", "H", "h"]:
            return str(1988 + int(y_value))
        elif era_value in ["令和", "R", "r"]:
            return str(2018 + int(y_value))

if __name__ == "__main__":
    # s =check("123.0",floait)
    # print(s)
    # print(type(s))

    # a2 = conv_str_to_int(-456)
    # print("{}:{}".format(a2,type(a2)))
    #
    # print(ymd("1981","7", "12"))

    d = era_to_ad("S56")
    print("{}:{}".format(d,type(d)))

    d2 = era_to_ad("R1")
    print("{}:{}".format(d2,type(d2)))
