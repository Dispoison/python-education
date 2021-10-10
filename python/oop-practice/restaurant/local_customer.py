"""Local customer functionality"""


from .customer import Customer


class LocalCustomer(Customer):
    """Customer in the restaurant."""
    def receive_menu(self, waiter, menu):
        """Menu getting method."""
        dishes = self._choose_dishes(menu)
        self.make_local_order(dishes, waiter)

    def make_local_order(self, dishes, waiter):
        """Order creation method."""
        print(f'{self} makes order in the restaurant: {dishes}')
        waiter.accept_order(self, dishes)

    def receive_order(self, dishes, order):
        """Method of receiving an order from a waiter."""
        super().receive_order(dishes, order)
        self.pay_for_order(order)
