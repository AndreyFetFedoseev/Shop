class Category:
    """Категории под товары"""

    name: str
    description: str
    __products: list

    count_category = 0
    count_unic_goods = 0

    def __init__(self, name, description, products):
        self.name = name
        self.description = description
        self.__products = products

        Category.count_category += 1
        Category.count_unic_goods += len(set(self.__products))

    @property
    def product(self):
        for prod in self.__products:
            print(f'{prod.name}, {prod.price} руб. Остаток: {prod.quantity} шт.')
        return None

    def add_product_in_category(self, product1):
        return self.__products.append(product1)


class Product:
    """Товар в магазине"""
    name: str
    description: str
    price: float
    quantity: int

    def __init__(self, name, description, price, quantity):
        self.name = name
        self.description = description
        self.price = price
        self.quantity = quantity

    @classmethod
    def create_product(cls, name, description, price, quantity, list_products):
        product = cls(name, description, price, quantity)
        for goods in list_products:
            if product.name == goods.name:
                goods.quantity += product.quantity
                if product.price > goods.price:
                    goods.price = product.price
        else:
            list_products.append(product)
        return list_products

    @property
    def price(self):
        return self.price

    @price.setter
    def price(self, new_price):
        if new_price > 0:
            if self.price > new_price:
                solve = input('Если вы согласны понизить цену нажмите "y"').lower()
                if solve == 'y':
                    self.price = new_price
            else:
                self.price = new_price
        else:
            print('Цена введена некорректная')
