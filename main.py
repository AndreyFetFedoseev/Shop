from classes import Category
from classes import Product
from classes import Smartphone
from classes import LawnGrass
from classes import ViewCategory
from functions import load_json
from functions import create_category

list_products = load_json('products.json')
print(list_products)
a = create_category(list_products)
print(a[0].products[1].name)
print(a[1].products[0].name)
print(Category.count_category)
print(Category.count_unic_goods)
b = Product('Motorola', 'катается', 2000000, 2)
a[0].product
a[1].product
c = Product.create_product('Vivo', 'creative', 15000000, 4, a[0].products)
print(c.price)
a[0].products[3].price = 300000
print(a[0].products[3].price)
d = Product.create_product('Honor', 'top', 120000, 8, a[0].products)
e = Product.create_product('Honor', 'top', 150000, 12, a[0].products)
a[0].add_product_in_category(c)
print(a[0].products[2].quantity)
print(a[0].products[3].name)
print(a[0].products[4].name)
a[0].product
print(a[0])
print(f'{c}\n{d}\n{b}')
print(b + c)
print(b + d)
aa = ViewCategory(a[0])
for x in aa:
    print(x)
# git rm -r --cached папка/
f = Smartphone('Huawei', 'Прекрасен', 40000, 36,'black', 'Бешеная', 'P40', 128)
# print(f + d)
print(f + f)
# print(d + f)
print(d + d)
# print(a + d)
# print(d + a)
g = LawnGrass('Чернозем', 'Плодородная', 50000, 2, 'black', 'Russia', 'Faster')
# print(f + g)
# print(g + f)
print(g + g)
# a[0].add_product_in_category(a)
