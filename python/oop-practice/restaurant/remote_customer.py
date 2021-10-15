"""Remote customer functionality"""


from .customer import Customer


class RemoteCustomer(Customer):
    """Remote customer."""
    def __init__(self, name, address, phone_number, surname=None, email=None, gender=None, birth_date=None):
        super().__init__(name, surname, phone_number, email, gender, birth_date, address)

    def use_internet_service(self, internet_service):
        """Uses internet service to make order."""
        menu = internet_service.enter()
        dishes = self._choose_dishes(menu)
        self.make_remote_order(dishes, internet_service)

    def make_remote_order(self, dishes, internet_service):
        """Makes remote order through internet service."""
        print(f'{self} makes remote order: {dishes}')
        internet_service.receive_dish_list(self, dishes)

    def receive_order(self, dishes, order):
        """Receives order from courier."""
        self.pay_for_order(order)
        super().receive_order(dishes, order)
