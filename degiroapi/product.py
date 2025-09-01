from datetime import datetime


class Product:
    def __init__(self, product):
        self.props = product  # for later access to any property which is not included below
        self.__id = product['id']
        self.__name = product['name']
        self.__isin = product.get('isin')
        self.__symbol = product['symbol']
        self.__currency = product['currency']
        self.__product_type = product['productTypeId']
        self.__tradable = product['tradable']
        self.__close_price = product.get('closePrice')
        close_price_date = product.get('closePriceDate')
        self.__close_price_date = datetime.strptime(close_price_date, '%Y-%m-%d').date() if close_price_date else None
        expiration_date = product.get('expirationDate')
        self.__expiration_date = datetime.strptime(expiration_date, '%d-%m-%Y').date() if expiration_date else None
        self.__strike_price = product.get('strikePrice')

    def __getitem__(self, item):
        """e.g. product["exchangeId"] """
        return self.props[item]

    @property
    def id(self):
        return self.__id

    @property
    def name(self):
        return self.__name

    @property
    def isin(self):
        return self.__isin

    @property
    def symbol(self):
        return self.__symbol

    @property
    def currency(self):
        return self.__currency

    @property
    def product_type(self):
        return self.__product_type

    @property
    def tradable(self):
        return self.__tradable

    @property
    def close_price(self):
        return self.__close_price

    @property
    def close_price_date(self):
        return self.__close_price_date

    @property
    def expiration_date(self):
        return self.__expiration_date

    @property
    def strike_price(self):
        return self.__strike_price

    @property
    def is_option(self):  # stock option?
        return self.product_type == 8

    @property
    def is_fx(self):  # manual forex trade
        return self.product_type == 3
