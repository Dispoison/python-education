"""Cook functionality."""


from time import sleep

from .employee import Employee


class Cook(Employee):
    """Guy who cooks dishes."""
    @staticmethod
    def __cook(dish):
        """Cooking a dish"""
        sleep(1)
        cooked = f'Cooked {dish.name}'
        print(cooked)
        return cooked

    def receive_order(self, order):
        """Receives order from waiter."""
        dishes, order = self.do_order(order)
        order.status = 'cooked'
        self.call_responsible_for_order(dishes, order)

    @staticmethod
    def call_responsible_for_order(dishes, order):
        """Call the employee in charge of the order"""
        order.responsible()
        order.responsible.receive_order(dishes, order)

    def do_order(self, order):
        """Cooks all dishes in order"""
        order.status = 'cooking'
        dishes = [self.__cook(dish) for dish in order.dishes]
        sleep(1)
        return dishes, order
