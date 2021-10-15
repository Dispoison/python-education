"""Order functionality."""


class Order:
    """Order class."""
    all_orders = []

    def __init__(self, order_date, is_deliver, customer, responsible, dishes, total_price):
        self.order_date = order_date
        self.is_deliver = is_deliver
        self.customer = customer
        self.responsible = responsible
        self.dishes = dishes
        self.total_price = total_price
        self.status = 'accepted'
        Order.all_orders.append(self)

    def __repr__(self):
        return f'Order {len(Order.all_orders)}:\n\t' \
               f'- order date: {self.order_date}\n\t' \
               f'- is deliver: {self.is_deliver}\n\t' \
               f'- customer: {self.customer}\n\t' \
               f'- responsible: {self.responsible}\n\t' \
               f'- dishes: {self.dishes}\n\t' \
               f'- total_price: {self.total_price}\n\t' \
               f'- status: {self.status}\n\t'
