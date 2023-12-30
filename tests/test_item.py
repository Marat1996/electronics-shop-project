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
    assert item1.price == 8.0  # 10.0 * 0.8


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
