from pathlib import Path

import pytest

from src.item import Item


@pytest.fixture
def item1(request):
    item = Item("Тестовый товар 1", 10.0, 5)

    def finalize():
        if item in Item.all:
            Item.all.remove(item)

    request.addfinalizer(finalize)
    return item


def test_calculate_total_price(item1):
    assert item1.calculate_total_price() == 50.0  # 10.0 * 5


def test_apply_discount(item1):
    item1.pay_rate = 0.8
    item1.apply_discount()
    assert item1.price == 8.0


def test_name_setter(item1):
    item1.name = 'New Name'
    assert item1.name == 'New Name'


def test_name_setter_truncate(item1):
    item1.name = 'SuperLongName'
    assert item1.name == 'SuperLongN'


def test_string_to_number():
    assert Item.string_to_number('5') == 5
    assert Item.string_to_number('5.0') == 5
    assert Item.string_to_number('5.5') == 5


def test_instantiate_from_csv():
    csv_file_path = Path(__file__).parent.parent / 'src' / 'items.csv'
    print(f"Путь к CSV-файлу: {csv_file_path}")

    expected_items_count = 5

    Item.instantiate_from_csv(str(csv_file_path))

    assert len(Item.all) == expected_items_count

    first_item = Item.all[0]
    assert isinstance(first_item, Item)


def test_clear_all_items():
    item1 = Item("Тестовый товар 1", 10.0, 5)
    item2 = Item("Тестовый товар 2", 15.0, 3)

    Item.clear_all_items()

    assert len(Item.all) == 0


def test_item_repr():
    item = Item("Смартфон", 10000, 20)
    assert repr(item) == "Item('Смартфон', 10000, 20)"


def test_item_str():
    item = Item("Смартфон", 10000, 20)
    assert str(item) == 'Смартфон'



