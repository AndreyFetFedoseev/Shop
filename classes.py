class Category:
    """Категории под товары"""

    name: str
    description: str
    goods: list

    count_category = 0
    count_goods = 0

    def __init__(self, name, description, goods):
        self.name = name
        self.description = description
        self.goods = goods

        Category.count_category += 1
        Category.count_unic_goods = len(set(self.goods))


class Product:
    """Товар в магазине"""
    name: str
    description: str
    pay: float
    count: int

    def __init__(self, name, description, pay, count):
        self.name = name
        self.description = description
        self.pay = pay
        self.count = count
