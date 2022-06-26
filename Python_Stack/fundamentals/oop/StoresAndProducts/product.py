class Product:
    def __init__(self, name, price, category):
        self.name = name
        self._price = price
        self.category = category

    @property
    def price(self):
        return self._price

    @price.setter
    def price(self, value):
        if value > 0:
            self._price = value

    def update_price(self, percent_change, is_increased):
        if is_increased:
            self.price += (self.price * percent_change) / 100
        else:
            self.price -= (self.price * percent_change) / 100

    def print_info(self):
        print(f"{self.name} | {self.category} | ${self.price}")

    def __str__(self):
        return f"{self.name} | {self.category} | ${self.price}"

    def __hash__(self):
        return hash(self.name)

    def __eq__(self, other):
        return (other.name == self.name) and (other.category == self.category)
