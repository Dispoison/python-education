"""Customer functionality."""


from abc import ABC, abstractmethod
from time import sleep
from random import randint

from .person import Person


class Customer(Person, ABC):
    """Abstract customer class."""
    def _think(self):
        """Thinks for one second."""
        print(f'{self} is thinking...')
        sleep(1)

    def _eat(self):
        """Eats for one second."""
        print(f'{self} is eating...')
        sleep(1)

    def _choose_dishes(self, menu):
        """Chooses the dishes."""
        self._think()
        dish_number = randint(1, len(menu))
        dishes = [menu[randint(0, len(menu)-1)] for _ in range(dish_number)]
        return dishes

    @abstractmethod
    def receive_order(self, dishes, order):
        """Receives order from responsible."""
        print(f'{self} receives the order')
        self._eat()

    def pay_for_order(self, order):
        """Pays for order to responsible."""
        print(f'{self} pays for the order {order.total_price} griven')
        order.responsible.receive_money_for_order(order.total_price, order)
