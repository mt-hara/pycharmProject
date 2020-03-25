# class Singleton():
#     __instance = None
#
#     @staticmethod
#     def getInstance():
#         if Singleton.__instance == None:
#             Singleton()
#         return Singleton.__instance
#
#     def __init__(self):
#         if Singleton.__instance != None:
#             raise Exception("This is singleton")
#         else:
#             Singleton.__instance = self

class Singleton(type):
    def __init__(cls,name, bases, dict):
        super(Singleton, cls).__init__(name,bases,dict)
        cls.instance = None

    def __call__(cls, *args, **kwargs):
        if cls.instance is None:
            cls.instance = super(Singleton, cls).__call__(*args, **kwargs)
        else:
            raise ("singleton error")

        return cls.instance