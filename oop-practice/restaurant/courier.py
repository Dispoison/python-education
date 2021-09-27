"""Courier functionality"""


from .employee import Employee


class Courier(Employee):
    """Guy who delivers orders."""
    def receive_order(self, dishes, order):
        """Method of receiving an order from the cook."""
        print(f'{self} got dishes from cook')
        self.deliver_dishes_to_customer(dishes, order)

    def deliver_dishes_to_customer(self, dishes, order):
        """Delivery method to remote customer."""
        print(f'{self} deliver order to {order.customer}')
        self._walk()
        order.customer.receive_order(dishes, order)

    @staticmethod
    def receive_money_for_order(money, order):
        """Method of receiving money upon delivery of order."""
        if money == order.total_price:
            order.status = 'paid'
        else:
            raise ValueError
