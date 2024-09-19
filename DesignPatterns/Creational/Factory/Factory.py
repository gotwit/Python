from __future__ import annotations
from abc import ABC, abstractmethod


class Creator(ABC):
    """
    The Creator class declares the factory method that is supposed to return an object of a Product class.
    The Creator's subclasses usually provide the implementation of this method.
    """

    # @abstractmethod
    # def factory(self):
    #     return Product()

    @abstractmethod
    def factory(self) -> Product:
        return Product()

    def business_logic(self) -> str:
        """
        Creator's primary responsibility is not creating products. Usually, it contains some core business logic
        that relies on Product objects, returned by the factory method.
        Subclasses can directly change that business logic by overriding the factory method and returning a 
        different type of product from it.
        """
        # Call the factory method to create a Product object.
        product = self.factory()

        # Now, use the product.
        result = f"Creator: The same creator's code has just worked with {product.operation()}"

        return result


"""
Concrete creators override the factory method in order to change the resulting product's type.
"""


class ConcreteCreator1(Creator):
    """
    Signature of the method still uses the abstract product type,
    even though the concrete product is actually returned from the method.
    This way the creator can stay independent of concrete product classes.
    """

    def factory(self) -> Product:
        return ConcreteProduct1()


class ConcreteCreator2(Creator):
    def factory(self) -> Product:
        return ConcreteProduct2()


class Product(ABC):
    """
    The Product interface declares the operations that all concrete products must implement.
    """

    @abstractmethod
    def operation(self) -> str:
        return "this is Product operation"


"""
Concrete Products provide various implementations of the Product interface.
"""


class ConcreteProduct1(Product):
    def operation(self) -> str:
        return "{Result of ConcreteProduct1}"


class ConcreteProduct2(Product):
    def operation(self) -> str:
        return "{Result of ConcreteProduct2}"


def client(creator: Creator) -> None:
    print(f"Client: I'm not aware of the creator's class, but it still works.\n"
          f"{creator.business_logic()}", end="")


if __name__ == "__main__":
    print("App: Launched with the ConcreteCreator1.")
    client(ConcreteCreator1())
    print()
    print("App: Launched with the ConcreteCreator2.")
    client(ConcreteCreator2())
