import json
from classes import Category
from classes import Product


def load_json(file_name):
    """Функция преобразования json файла для python"""
    with open(file_name, 'r', encoding='utf-8') as file:
        return json.load(file)


def create_category(list_products):
    """Функция для создания объектов классов с помещением объектов Товаров в класс Категорий"""
    list_category = []
    list_class_product = []
    for dict_category in list_products:
        for product in dict_category['products']:
            class_product = Product(product['name'], product['description'], product['price'], product['quantity'])
            list_class_product.append(class_product)
        class_category = Category(dict_category['name'], dict_category['description'], list_class_product)
        list_category.append(class_category)
        list_class_product = []
    return list_category
