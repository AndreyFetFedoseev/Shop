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
    def products(self):
        return self.__products

    @property
    def product(self):
        """
        Выводит список товаров в классе Категории
        """
        for prod in self.__products:
            print(f'{prod.name}, {prod.price1} руб. Остаток: {prod.quantity} шт.')

    def add_product_in_category(self, class_product):
        """
        Добавляет в список класса Категории объект товара
        """
        return self.__products.append(class_product)


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
        """
        Создает объект товара и добавляет в список, а если совпадает название товара,
        то добавляет только кол-во и выставляет большую цену
        """
        product = cls(name, description, price, quantity)
        for goods in list_products:
            if product.name == goods.name:
                goods.quantity += product.quantity
                if product.price > goods.price:
                    goods.price = product.price
        for goods in list_products:
            if product.name == goods.name:
                break
        else:
            list_products.append(product)
        return product

    @property
    def price(self):
        return self.price1

    @price.setter
    def price(self, new_price):
        """
        Метод при обращении без скобок,
        который меняет цену товара
        """
        if new_price > 0:
            if self.price1 > new_price:
                solve = input('Если вы согласны понизить цену нажмите "y"').lower()
                if solve == 'y':
                    self.price1 = new_price
            else:
                self.price1 = new_price
        else:
            print('Цена введена некорректная')

    @price.deleter
    def price(self):
        """Удаляет цену товара"""
        print('Цена неопределена')
        self.price1 = None
