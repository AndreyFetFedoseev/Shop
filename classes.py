class Category:
    """Категории под товары"""

    name: str
    description: str
    _products: list

    count_category = 0
    count_unic_goods = 0

    def __init__(self, name, description, products):
        self.name = name
        self.description = description
        self._products = products

        Category.count_category += 1
        Category.count_unic_goods += len(set(self._products))

    @property
    def product(self):
        for prod in self._products:
            print(f'{prod.name}, {prod.price1} руб. Остаток: {prod.quantity} шт.')
        return None

    def add_product_in_category(self, class_product):
        return self._products.append(class_product)


class Product:
    """Товар в магазине"""
    name: str
    description: str
    price: float
    quantity: int

    def __init__(self, name, description, price, quantity):
        self.name = name
        self.description = description
        self.price1 = price
        self.quantity = quantity

    @classmethod
    def create_product(cls, name, description, price, quantity, list_products):
        product = cls(name, description, price, quantity)
        for goods in list_products:
            if product.name == goods.name:
                goods.quantity += product.quantity
                if product.price1 > goods.price1:
                    goods.price1 = product.price1
        else:
            list_products.append(product)
        return list_products

    @property
    def price(self):
        return self.price1

    @price.setter
    def price(self, new_price):
        if new_price > 0:
            if self.price1 > new_price:
                solve = input('Если вы согласны понизить цену нажмите "y"').lower()
                if solve == 'y':
                    self.price1 = new_price
            else:
                self.price1 = new_price
        else:
            print('Цена введена некорректная')
