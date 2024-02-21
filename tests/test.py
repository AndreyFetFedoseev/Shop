import pytest
from classes import Category
from classes import Product
from functions import create_category


@pytest.fixture
def category_meat():
    return Category('Филе курицы', 'Область грудки, очищенная от киля и кожи', ['Мясо'])


@pytest.fixture
def product_smart():
    return Product('Samsung', 'Средство связи', 10000.50, 27)


def test_category_init(category_meat):
    """Тест класса Категория"""
    assert category_meat.name == 'Филе курицы'
    assert category_meat.description == 'Область грудки, очищенная от киля и кожи'
    assert category_meat.__products == ['Мясо']
    assert category_meat.count_category == 1
    assert category_meat.count_unic_goods == 1


def test_product_init(product_smart):
    """Тест класса Товар"""
    assert product_smart.name == 'Samsung'
    assert product_smart.description == 'Средство связи'
    assert product_smart.price == 10000.50
    assert product_smart.quantity == 27


def test_create_category():
    """В тесте кол-во категорий 3 и товаров 5, из-за тестов классов в файле"""
    list_test = [{'name': 'Смартфоны',
                  'description': 'Смартфоны, как средство не только коммуникации, но и получение дополнительных функций для удобства жизни',
                  'products': [{'name': 'Samsung Galaxy C23 Ultra', 'description': '256GB, Серый цвет, 200MP камера',
                                'price': 180000.0, 'quantity': 5},
                               {'name': 'Iphone 15', 'description': '512GB, Gray space', 'price': 210000.0,
                                'quantity': 8},
                               {'name': 'Xiaomi Redmi Note 11', 'description': '1024GB, Синий', 'price': 31000.0,
                                'quantity': 14}]},
                 {'name': 'Телевизоры',
                  'description': 'Современный телевизор, который позволяет наслаждаться просмотром, станет вашим другом и помощником',
                  'products': [{'name': '55" QLED 4K', 'description': 'Фоновая подсветка',
                                'price': 123000.0, 'quantity': 7}]}]

    a = create_category(list_test)
    assert a[0].name == 'Смартфоны'
    assert a[1].name == 'Телевизоры'
    assert a[
               0].description == 'Смартфоны, как средство не только коммуникации, но и получение дополнительных функций для удобства жизни'
    assert a[0].__products[0].name == 'Samsung Galaxy C23 Ultra'
    assert a[1].__products[0].name == '55" QLED 4K'
    assert a[0].__products[2].description == '1024GB, Синий'
    assert a[0].__products[1].price == 210000.0
    assert a[1].__products[0].quantity == 7
    assert Category.count_category == 3
    assert Category.count_unic_goods == 5
