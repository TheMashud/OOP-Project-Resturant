from abc import ABC, abstractmethod
class User(ABC):
    def __init__(self, name, ) -> None:
        self.name = name

class Customer(User):
    def __init__(self, name, money) -> None:
        self.wallet = money
        self.__order = None
        super().__init__(name)

    @property
    def order(self):
        return self.__order
    
    @order.setter
    def order(self, order):
        self.__order = order

    def place_order(self, order):
        self.order = order
        print(f'{self.name} placed an order {order.items}')

    def eat_Food(self , order):
        print(f'{self.name} item food {order.items}')

    def pay_for_order(sekf, amount):
        pass

    def give_tipe(self, tips_amount):
        pass

    def write_review(Self, stars):
        pass