from item import Item


class Phone(Item):

    def __init__(self, name: str, price: float, quantity: int, broken_phones=0):

        super().__init__(
            name, price, quantity
        )

        # Run validation to the received arguments

        assert broken_phones >= 0, f"broken_phones {broken_phones} is not greater than zero"
