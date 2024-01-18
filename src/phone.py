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
        Переопределение оператора сложения для экземпляров класса Phone и Item.

        :param other: Другой экземпляр класса Phone или Item.
        :return: Сумма количества товара в магазине.
        """
        if isinstance(other, (Phone, Item)):
            return self.quantity + other.quantity
        else:
            raise TypeError("Нельзя сложить Phone или Item с объектами других классов.")
