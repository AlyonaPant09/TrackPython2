# TODO Написать 3 класса с документацией и аннотацией типов
# TODO работоспособность экземпляров класса проверить с помощью doctest
from abc import ABC
import doctest


class Vehicle(ABC):
    """Транспортное средство."""
    def __init__(self, brand: str, max_speed: float):
        self.brand = brand
        self.max_speed = max_speed
    def start(self) -> str:
        ...
    def stop(self) -> str:
        ...


class Car(Vehicle):
    """Легковой автомобиль."""
    def start(self) -> str:
        """>>> Car('Toyota', 180).start()\n        'Двигатель запущен'"""
        return "Двигатель запущен"
    def stop(self) -> str:
        """>>> Car('BMW', 200).stop()\n        'Двигатель остановлен'"""
        return "Двигатель остановлен"


class Animal(ABC):
    """Животное."""
    def __init__(self, name: str, age: int):
        self.name = name
        self.age = age
    def eat(self) -> str:
        ...
    def sleep(self) -> str:
        ...


class Cat(Animal):
    """Кошка."""
    def eat(self) -> str:
        """>>> Cat('Мурка', 3).eat()\n        'Кошка ест'"""
        return "Кошка ест"
    def sleep(self) -> str:
        """>>> Cat('Барсик', 5).sleep()\n        'Кошка спит'"""
        return "Кошка спит"


class Product(ABC):
    """Товар."""
    def __init__(self, name: str, price: float):
        self.name = name
        self.price = price
    def get_price(self) -> float:
        ...
    def describe(self) -> str:
        ...


class Smartphone(Product):
    """Смартфон."""
    def get_price(self) -> float:
        """>>> Smartphone('iPhone', 999.99).get_price()\n        999.99"""
        return self.price
    def describe(self) -> str:
        """>>> Smartphone('Samsung', 799.0).describe()\n        'Смартфон Samsung за 799.0 руб.'"""
        return f"Смартфон {self.name} за {self.price} руб."


if __name__ == "__main__":
    doctest.testmod()