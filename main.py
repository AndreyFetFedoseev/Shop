from classes import Category
from classes import Product
from functions import load_json
from functions import create_category

list_products = load_json('products.json')
print(list_products)
a = create_category(list_products)
# a, b = load_category(list_products)
print(a[0].product)
# print(a[0].products[0].name)
# print(a[1].products)
# print(a[1].products)
# # print(b[2].name)
# # print(b[0].name)
print(Category.count_category)
print(Category.count_unic_goods)
