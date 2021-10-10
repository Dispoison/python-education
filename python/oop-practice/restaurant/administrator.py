"""Administrator functionality"""


from .employee import Employee


class Administrator(Employee):
    """Administrator class."""
    def manage(self):
        """Manages the restaurant."""
        print(f'{self.__class__.__name__} {self._name}  manages')
