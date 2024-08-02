import csv


class Item:

    pay_rate = 0.8
    all = []

    def __init__(self, name: str, price: float, quantity: int):

        # Run validation to the received arguments

        assert price > 0
        assert quantity >= 0

        self.__name = name  # we can restrict of changing of the name
        self.__price = price
        self.quantity = quantity

        Item.all.append(self)

    @property
    def name(self):  # we can restrict the user changing the name
        return self.__name

    @property
    def price(self):
        return self.__price

    @name.setter
    def name(self, value):   # this can set the name as value even though property decorator is there
        print("You are trying to change......")
        if len(value) > 10:
            raise Exception("The name is too long!!!")
        else:
            self.__name = value

    def print_item(self):
        print(self.name, self.__price, self.quantity)

    def apply_discount(self):
        self.__price = self.__price * self.pay_rate # if we write Item.pay_rate if we change for instance down we
        # will not get the discount apllied

    def apply_increment(self, increment):
        self.__price = self.__price + self.__price * increment

    def __repr__(self): # it will give us the object instances created
        return f"{self.__class__.__name__}('{self.name}',{self.__price},{self.quantity})"

    @classmethod
    def instantiate_from_csv(cls):
        with open('items.csv', 'r') as f:
            reader = csv.DictReader(f)
            items = list(reader)

        for item in items:
            Item(
                name=item.get('name'),
                price=float(item.get('price')),
                quantity=int(item.get('quantity')),
            )

    @staticmethod
    def is_integer(num):
        if isinstance(num, float):
            return num.is_integer()
        elif isinstance(num, int):
            return True
        else:
            return False

    def __connect(self, smp_server):
        pass

    def __prepare_body(self):  # this is same as private method in other languages
        return f"""
        Hello Someone.
        we have  {self.name} {self.quantity} times
        Regards, Pavan
    """

    def __send(self):
        pass

    def send_email(self):
        self.__connect('')
        self.__prepare_body()
        self.__send()
