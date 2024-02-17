class Category:
    """Категории под товары"""

    count_category = 0
    def __init__(self, name, description, goods):
        self.name = name
        self.description = description
        self.goods = goods

        Category.count_category += 1


class Product:
    """Товар в магазине"""

    count_unic_goods = 0
    def __init__(self, name, description, pay, count):
        self.name = name
        self.description = description
        self.pay = pay
        self.count = count

        Product.count_unic_goods += 1
