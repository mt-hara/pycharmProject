from abc import ABCMeta, abstractmethod

class Creator(metaclass=ABCMeta):

    def create(self):
        return self.factory_method()

    @abstractmethod
    def factory_method(self):
        pass


class Product(metaclass=ABCMeta):
    @abstractmethod
    def method1(self):
        pass

    @abstractmethod
    def method2(self):
        pass

class ConcreteCreator(Creator):
    def factory_method(self):
        return ConcreteProduct()


class ConcreteProduct(Product):
    def method1(self):
        print("Method1")

    def method2(self):
        print("Method2")


if __name__ == "__main__":
    creator =ConcreteCreator()
    product = creator.factory_method()
    product.method1()
    product.method2()