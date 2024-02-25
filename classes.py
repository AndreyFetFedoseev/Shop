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

    def __str__(self):
        # return f'Категория: {self.name}\nКоличество товаров: {', '.join([x.name for x in self.products])}'
        return f'Категория: {self.name}\nКоличество товаров: {len(self)}'

    def __len__(self):
        quant = 0
        for prods in self.products:
            quant += prods.quantity
        return quant

    @property
    def products(self):
        return self.__products

    @property
    def product(self):
        """
        Выводит список товаров в классе Категории
        """
        str_product = ''
        for prod in self.__products:
            str_product += f'{prod.name}, {prod.price1} руб. Остаток: {prod.quantity} шт.' + '\n'
        return str_product

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

    def __str__(self):
        return f'Наименование товара: {self.name}, {self.price} руб., Остаток: {self.quantity} шт.'

    def __add__(self, other):
        return self.price * self.quantity + other.price * other.quantity

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


class ViewCategory:
    """Класс для просмотра товаров в категории"""

    def __init__(self, class_category):
        self.class_category = class_category

    def __iter__(self):
        self.current_index = -1
        return self

    def __next__(self):
        # t = ''
        # for x in self.Category.products:
        #     t += x.name + '\n'
        # return t
        if self.current_index + 1 < len(self.class_category.products):
            self.current_index += 1
            return self.class_category.products[self.current_index].name
        else:
            raise StopIteration
