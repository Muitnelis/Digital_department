from abc import ABC, abstractmethod

class Car(ABC):
    def __init__(self, brand: str, model: str, year: int):
        self.brand = brand
        self.model = model
        self.year = year

    @abstractmethod
    def description(self) -> str:
        """
        Абстрактный метод для вывода описания автомобиля.
        """

    def __str__(self) -> str:
        return f"{self.brand} {self.model} ({self.year})"

    def __repr__(self) -> str:
        return f"{self.__class__.__name__}('{self.brand}', '{self.model}', {self.year})"

class BMW(Car):
    def __init__(self, model: str, year: int, series: str):
        super().__init__("BMW", model, year)
        self.series = series

    def description(self) -> str:
        """
        Метод для вывода описания автомобиля BMW.
        Дочерний класс BMW расширяет функционал базового класса Car.
        """
        return f"BMW {self.series} {self.model} ({self.year})"

    def update_series(self, new_series: str):
        """
        Метод для обновления серии автомобиля BMW.
        Атрибут series инкапсулирован для безопасного доступа.
        """
        self.series = new_series
