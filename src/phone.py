from src.item import Item

class Phone(Item):
    """
    Класс для представления смартфона в магазине.
    """
    def __init__(self, name: str, price: float, quantity: int, number_of_sim: int) -> None:
        """
        Создание экземпляра класса Phone.

        :param name: Название смартфона.
        :param price: Цена за единицу смартфона.
        :param quantity: Количество смартфонов в магазине.
        :param number_of_sim: Количество поддерживаемых сим-карт.
        """
        super().__init__(name, price, quantity)
        self.number_of_sim = number_of_sim

    def __add__(self, other) -> int:
        """
        Переопределение оператора + для сложения объектов класса Phone.

        :param other: Другой объект класса Phone или его потомка.
        :return: Суммарное количество товара (без учета сим-карт).
        """
        if isinstance(other, Phone):
            return self.quantity + other.quantity
        return NotImplemented

    def __repr__(self) -> str:
        """
        Возвращает строковое представление объекта для использования в консоли и дебаге.
        """
        return f"Phone('{self.name}', {self.price}, {self.quantity}, {self.number_of_sim})"
