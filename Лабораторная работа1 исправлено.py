# TODO Написать 3 класса с документацией и аннотацией типов
# TODO работоспособность экземпляров класса проверить с помощью doctest
import doctest


class Car:
    def __init__(self, brand: str, max_speed: float, year: int):
        """
        Создание и подготовка к работе объекта "Автомобиль"

        :param brand: Марка автомобиля
        :param max_speed: Максимальная скорость
        :param year: Год выпуска

        Примеры:
        >>> car = Car('Toyota', 180, 2020)  # инициализация экземпляра класса
        """
        if not isinstance(brand, str):
            raise TypeError("Марка автомобиля должна быть типа str")
        if len(brand) == 0:
            raise ValueError("Марка автомобиля не может быть пустой строкой")
        self.brand = brand

        if not isinstance(max_speed, (int, float)):
            raise TypeError("Максимальная скорость должна быть типа int или float")
        if max_speed <= 0:
            raise ValueError("Максимальная скорость должна быть положительным числом")
        self.max_speed = float(max_speed)

        if not isinstance(year, int):
            raise TypeError("Год выпуска должен быть типа int")
        if year <= 0:
            raise ValueError("Год выпуска должен быть положительным числом")
        self.year = year

    def start(self) -> str:
        """
        Функция которая запускает двигатель автомобиля

        :return: Сообщение о запуске двигателя

        Примеры:
        >>> car = Car('Toyota', 180, 2020)
        >>> car.start()
        """
        ...

    def stop(self) -> str:
        """
        Функция которая останавливает двигатель автомобиля

        :return: Сообщение об остановке двигателя

        Примеры:
        >>> car = Car('BMW', 200, 2021)
        >>> car.stop()
        """
        ...


class Cat:
    def __init__(self, name: str, age: int, breed: str):
        """
        Создание и подготовка к работе объекта "Кошка"

        :param name: Имя кошки
        :param age: Возраст кошки
        :param breed: Порода кошки

        Примеры:
        >>> cat = Cat('Мурка', 3, 'Сиамская')  # инициализация экземпляра класса
        """
        if not isinstance(name, str):
            raise TypeError("Имя кошки должно быть типа str")
        if len(name) == 0:
            raise ValueError("Имя кошки не может быть пустой строкой")
        self.name = name

        if not isinstance(age, int):
            raise TypeError("Возраст кошки должен быть типа int")
        if age <= 0:
            raise ValueError("Возраст кошки должен быть положительным числом")
        self.age = age

        if not isinstance(breed, str):
            raise TypeError("Порода кошки должна быть типа str")
        if len(breed) == 0:
            raise ValueError("Порода кошки не может быть пустой строкой")
        self.breed = breed

    def eat(self) -> str:
        """
        Функция которая имитирует процесс еды

        :return: Сообщение о том, что кошка ест

        Примеры:
        >>> cat = Cat('Мурка', 3, 'Сиамская')
        >>> cat.eat()
        """
        ...

    def sleep(self) -> str:
        """
        Функция которая имитирует процесс сна

        :return: Сообщение о том, что кошка спит

        Примеры:
        >>> cat = Cat('Барсик', 5, 'Британская')
        >>> cat.sleep()
        """
        ...


class Smartphone:
    def __init__(self, model: str, price: float, storage: int):
        """
        Создание и подготовка к работе объекта "Смартфон"

        :param model: Модель смартфона
        :param price: Цена смартфона
        :param storage: Объем памяти в ГБ

        Примеры:
        >>> phone = Smartphone('iPhone', 999.99, 256)  # инициализация экземпляра класса
        """
        if not isinstance(model, str):
            raise TypeError("Модель смартфона должна быть типа str")
        if len(model) == 0:
            raise ValueError("Модель смартфона не может быть пустой строкой")
        self.model = model

        if not isinstance(price, (int, float)):
            raise TypeError("Цена смартфона должна быть типа int или float")
        if price <= 0:
            raise ValueError("Цена смартфона должна быть положительным числом")
        self.price = float(price)

        if not isinstance(storage, int):
            raise TypeError("Объем памяти должен быть типа int")
        if storage <= 0:
            raise ValueError("Объем памяти должен быть положительным числом")
        self.storage = storage

    def get_price(self) -> float:
        """
        Функция которая возвращает цену смартфона

        :return: Цена смартфона

        Примеры:
        >>> phone = Smartphone('iPhone', 999.99, 256)
        >>> phone.get_price()
        """
        ...

    def describe(self) -> str:
        """
        Функция которая возвращает описание смартфона

        :return: Строка с описанием модели и цены

        Примеры:
        >>> phone = Smartphone('Samsung', 799.0, 128)
        >>> phone.describe()
        """
        ...


if __name__ == "__main__":
    doctest.testmod()