from classes import Category
from classes import Product
from functions import load_json
from functions import create_category

list_products = load_json('products.json')
print(list_products)
a = create_category(list_products)
# a, b = load_category(list_products)
# print(a[0].product)
print(a[0]._Category__products[0].name)
# print(a[1].products)
# print(a[1].products)
print(Category.count_category)
print(Category.count_unic_goods)
b = Product('moto', 'катается', '2000000', 2)
c = Product.create_product('motos', 'vrrrr', 15000000, 4, a[0]._Category__products)
print(c)
c[3].price = 300000
print(c[3].price)
d = Product.create_product('motor', 'vrr', 120000, 8, a[0]._Category__products)
print(d[4].name)
e = Product.create_product('motor', 'vrr', 100000, 12, a[0]._Category__products)
print(e[4].quantity)
a[0].add_product_in_category(e[4])
print(a[0]._Category__products[5].quantity)
print(a[0]._Category__products[5].name)
print(a[0]._Category__products[5].price)
