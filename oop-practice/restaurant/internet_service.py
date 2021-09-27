"""Internet service functionality."""


from datetime import datetime

from .employee import Employee
from .order import Order


class InternetService:
    """Internet service class."""
    def __init__(self, menu):
        self.menu = menu

    def enter(self):
        """Returns restaurant menu."""
        return self.menu

    def receive_dish_list(self, customer, dishes):
        """Receives dish list from remote customer."""
        self._set_order(customer, dishes)

    @staticmethod
    def _set_order(customer, dishes):
        """Sets up the order and transmits it to the cook over the Internet."""
        total_price = 0
        for dish in dishes:
            total_price += dish.price
        order = Order(order_date=datetime.now(), is_deliver=True, customer=customer,
                      responsible=Employee.staff['Courier'], dishes=dishes, total_price=total_price)
        Employee.staff['Cook'].receive_order(order)
