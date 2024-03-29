from abc import ABC, abstractmethod


class SampleProduct(ABC):
    """Абстрактный класс для создания классов Товаров"""

    @abstractmethod
    def __str__(self):
        pass

    @abstractmethod
    def __add__(self, other):
        pass

    @classmethod
    @abstractmethod
    def create_product(cls, name, description, price, quantity, list_products):
        pass

    @property
    @abstractmethod
    def price(self):
        pass

    @price.setter
    @abstractmethod
    def price(self, new_price):
        pass

    @price.deleter
    @abstractmethod
    def price(self):
        pass


class MixinRepr:
    """Общий вывод для всех классов"""

    def __init__(self):
        print(repr(self))

    def __repr__(self):
        """Описание создания экземпляра класса"""
        dict_attr = vars(self)
        list_attribute = []
        for attribute in dict_attr.values():
            if type(attribute) is int or type(attribute) is float:
                list_attribute.append(str(attribute))
            elif attribute is None:
                continue
            else:
                list_attribute.append(f"'{attribute}'")
        str_repr = ', '.join(list_attribute)
        return f'{self.__class__.__name__}({str_repr})'


class Category(MixinRepr):
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
        super().__init__()

    def __str__(self):
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
        if not isinstance(class_product, Product):
            raise ValueError('Объект не принадлежит к классу Товар')
        if class_product.quantity > 0:
            return self.__products.append(class_product)
        else:
            raise ValueError('Товар с нулевым кол-ом не может быть добавлен')

    def average_price(self):
        sum_product = 0
        try:
            for product in self.__products:
                sum_product += product.price
            average_price = sum_product / len(self.__products)
        except ZeroDivisionError:
            print('В категории нет товаров')
            return 0
        else:
            return average_price


class Product(SampleProduct, MixinRepr):
    """Товар в магазине"""
    name: str
    description: str
    price: float
    quantity: int

    def __init__(self, name, description, price, quantity, color=None):
        self.name = name
        self.description = description
        self.price1 = price
        self.quantity = quantity
        self.color = color
        super().__init__()

    def __str__(self):
        return f'Наименование товара: {self.name}, {self.price} руб., Остаток: {self.quantity} шт.'

    def __add__(self, other):
        if not type(other) is type(self):
            raise TypeError('Невозможно сложить, т.к. товары из разных категорий')
        return self.price * self.quantity + other.price * other.quantity

    @classmethod
    def create_product(cls, name, description, price, quantity, list_products):
        """
        Создает объект товара и добавляет в список, а если совпадает название товара,
        то добавляет только кол-во и выставляет большую цену
        """
        if quantity > 0:
            product = cls(name, description, price, quantity)
        else:
            raise ValueError('Товар с нулевым кол-ом не может быть добавлен')
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


class ViewCategory(MixinRepr):
    """Класс для просмотра товаров в категории"""

    def __init__(self, class_category):
        self.class_category = class_category
        super().__init__()

    def __iter__(self):
        self.current_index = -1
        return self

    def __next__(self):
        if self.current_index + 1 < len(self.class_category.products):
            self.current_index += 1
            return self.class_category.products[self.current_index].name
        else:
            raise StopIteration


class Smartphone(Product, MixinRepr):
    """Категория товара 'Смартфоны'"""

    def __init__(self, name, description, price, quantity, color, efficiency, model, internal_memory):
        super().__init__(name, description, price, quantity, color)
        self.efficiency = efficiency
        self.model = model
        self.internal_memory = internal_memory


class LawnGrass(Product, MixinRepr):
    """Категория товара 'Трава газонная'"""

    def __init__(self, name, description, price, quantity, color, country_origin, germination_period):
        super().__init__(name, description, price, quantity, color)
        self.country_origin = country_origin
        self.germination_period = germination_period
