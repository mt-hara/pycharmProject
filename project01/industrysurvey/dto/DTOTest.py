class DTOTest():
    def __init__(self, number, name):
        self.__number = number
        self.__name = name

    def create(self, number, name):
        self.number = number
        self.name = name

    @property
    def number(self):
        return self.__number

    @number.setter
    def number(self, param):
        self.__number = param

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, param):
        self.__name = param