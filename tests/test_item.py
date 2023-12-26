"""Здесь надо написать тесты с использованием pytest для модуля item."""
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


@pytest.fixture
def item2(request):
    item = Item("Тестовый товар 2", 20.0, 3)

    def finalize():
        if item in Item.all:
            Item.all.remove(item)

    request.addfinalizer(finalize)
    return item


def test_calculate_total_price(item1, item2):
    assert item1.calculate_total_price() == 50.0  # 10.0 * 5
    assert item2.calculate_total_price() == 60.0  # 20.0 * 3


def test_all_items_list(item1, item2):
    assert len(Item.all) == 2
    assert item1 in Item.all
    assert item2 in Item.all
    Item.all.clear()
