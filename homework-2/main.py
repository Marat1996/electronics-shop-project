from pathlib import Path
from src.item import Item

if __name__ == '__main__':
    # Получить абсолютный путь к текущему файлу
    current_file_path = Path(__file__)

    # Построить путь к файлу items.csv в каталоге src
    csv_file_path = current_file_path.parent / 'src' / 'items.csv'

    # Теперь мы в корневом каталоге проекта, где находится src/items.csv
    Item.instantiate_from_csv(csv_file_path)

    # Остальной код остается без изменений
    item = Item('Телефон', 10000, 5)

    # длина наименования товара меньше 10 символов
    item.name = 'Смартфон'
    assert item.name == 'Смартфон'

    # длина наименования товара больше 10 символов
    item.name = 'СуперСмартфон'
    # Exception: Длина наименования товара превышает 10 символов.

    assert len(Item.instances) == 5  # в файле 5 записей с данными по товарам

    item1 = Item.instances[0]
    assert item1.name == 'Смартфон'

    assert Item._string_to_number('5') == 5
    assert Item._string_to_number('5.0') == 5
    assert Item._string_to_number('5.5') == 5
