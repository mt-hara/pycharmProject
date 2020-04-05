# from __future__ import annotations
from abc import ABCMeta, abstractmethod, ABC


class Creator(metaclass=ABCMeta):
    @abstractmethod
    def factory_method(self):
        pass

    def some_operation(self):
        product = self.factory_method()
        result = f"Creator: The same creator's code has just worked with {product.operation()}"

        return result


class ConcreteCreator1(Creator):
    def factory_method(self):
        return ConcreteProduct1()


class ConcreteCreator2(Creator):
    def factory_method(self):
        return ConcreteProduct2()


class Product(metaclass=ABCMeta):
    @abstractmethod
    def operation(self):
        pass


class ConcreteProduct1(Product):
    def operation(self) -> str:
        return "{Result to the ConcreteProduct1}"


class ConcreteProduct2(Product):
    def operation(self) -> str:
        return "{Result to the ConcreteProduct2}"


def client_code(creator: Creator) -> None:
    # creator.some_operation()
    t = creator.some_operation()
    print(t)
    # print(f"{creator.some_operation()}")


if __name__ == "__main__":
    print("App: Launched with the ConcreteCreator1")
    client_code(ConcreteCreator1())
    print("\n")

    print("App: Launched with the ConcreteCreator2")
    client_code(ConcreteCreator2())
