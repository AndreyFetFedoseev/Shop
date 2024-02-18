class Category:
    """Категории под товары"""

    name: str
    description: str
    products: list

    count_category = 0
    count_unic_goods = 0

    def __init__(self, name, description, products):
        self.name = name
        self.description = description
        self.products = products

        Category.count_category += 1
        Category.count_unic_goods = len(set(self.products))


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
