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



    # if val is None:
    #     return None
    # if type(val) is int:
    #     return val

def conv_str_to_int(val):
    if not val.inumeric() == True:
        try:
            float(val)
            return float(val)
        except  ValueError:
            return None
    else:
        return int(val)




if __name__ == "__main__":
    s =check("123.0",float)
    print(s)
    print(type(s))

    # a2 = conv_str_to_int(456)
    # print("{}:{}".format(a2,type(a2)))

