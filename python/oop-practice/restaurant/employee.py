"""Employee functionality."""


from abc import ABC
from time import sleep

from .person import Person


class Employee(Person, ABC):
    """Abstract employee class."""
    staff = dict()

    def __init__(self, name, surname, phone_number, email, gender, birth_date, address, passport_id):
        super().__init__(name, surname, phone_number, email, gender, birth_date, address)
        self._passport_id = passport_id
        Employee.staff[self.__class__.__name__] = self

    def __call__(self):
        self._walk()

    def _walk(self):
        """Walks for one second."""
        print(f'{self} is walking...')
        sleep(1)

    def quit(self):
        """Leaves from the job."""
        print(f'{self._name} leave from job')
