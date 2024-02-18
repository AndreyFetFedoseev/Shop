import pytest
from classes import Category
from classes import Product


@pytest.fixture
def category_meat():
    return Category('Филе курицы', 'Область грудки, очищенная от киля и кожи', ['Мясо'])


@pytest.fixture
def product_smart():
    return Product('Samsung', 'Средство связи', 10000.50, 27)


def test_category_init(category_meat):
    assert category_meat.name == 'Филе курицы'
    assert category_meat.description == 'Область грудки, очищенная от киля и кожи'
    assert category_meat.products == ['Мясо']
    assert category_meat.count_category == 1
    assert category_meat.count_unic_goods == 1


def test_product_init(product_smart):
    assert product_smart.name == 'Samsung'
    assert product_smart.description == 'Средство связи'
    assert product_smart.price == 10000.50
    assert product_smart.quantity == 27
