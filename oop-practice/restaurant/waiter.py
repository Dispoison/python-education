"""Waiter functionality."""


from datetime import datetime

from .employee import Employee
from .order import Order


class Waiter(Employee):
    """Guy who services customers."""
    def service(self, customer, menu):
        """Services customer."""
        print(f'{self} services {customer}')
        customer.receive_menu(self, menu)

    def accept_order(self, customer, dishes):
        """Accepts an order."""
        total_price = 0
        for dish in dishes:
            total_price += dish.price
        order = Order(order_date=datetime.now(), is_deliver=False, customer=customer,
                      responsible=self, dishes=dishes, total_price=total_price)
        self.bring_order_to_cook(order)

    def bring_order_to_cook(self, order):
        """Brings the order to cook."""
        self._walk()
        print(f'{self} brought order to cook')
        Employee.staff['Cook'].receive_order(order)

    def receive_order(self, dishes, order):
        """Receives the order from cook."""
        print(f'{self} got dishes from cook')
        self.bring_dishes_to_customer(dishes, order)

    def bring_dishes_to_customer(self, dishes, order):
        """Brings dishes to customer."""
        print(f'{self} brings order {dishes} to {order.customer}')
        order.customer.receive_order(dishes, order)

    @staticmethod
    def receive_money_for_order(money, order):
        """Receives money from customer."""
        if money == order.total_price:
            order.status = 'paid'
        else:
            raise ValueError
