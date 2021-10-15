from abc import ABC, abstractmethod

from ..transport import Transport


class Vehicle(Transport, ABC):
    def __init__(self, manufacturer, model, weight, seating_capacity, max_speed, consumption):
        self._manufacturer = manufacturer
        self._model = model
        self._weight = weight
        self._seating_capacity = seating_capacity
        self._max_speed = max_speed
        self._consumption = consumption

    @property
    def manufacturer(self):
        """Manufacturer name"""
        return self._manufacturer

    @property
    def model(self):
        """Model name"""
        return self._model

    @property
    def weight(self):
        """Transport weight in kilograms"""
        return self._weight

    @property
    def seating_capacity(self):
        """Number of people who can be seated in a transport"""
        return self._seating_capacity

    @property
    def max_speed(self):
        """Max transport speed km/h"""
        return self._max_speed

    @property
    def consumption(self):
        """Consumption object"""
        return self._consumption

    def __str__(self):
        return f'{self.manufacturer} {self.model}'

    def __eq__(self, other):
        return self.weight == other.weight

    def __ne__(self, other):
        return self.weight != other.weight

    def __lt__(self, other):
        return self.weight < other.weight

    def __gt__(self, other):
        return self.weight > other.weight

    def __le__(self, other):
        return self.weight <= other.weight

    def __ge__(self, other):
        return self.weight >= other.weight

    def __enter__(self):
        print('Starts the trip at point A')

    def __exit__(self, exc_type, exc_val, exc_tb):
        print('Ends the trip at point B')

    @abstractmethod
    def __call__(self, *args, **kwargs):
        pass

    def get_info(self):
        """Get transport info"""
        info = f'{self.manufacturer} {self.model}:\n\t' \
               f'- weight: {self.weight} kg\n\t' \
               f'- seating capacity: {self.seating_capacity} places\n\t' \
               f'- max speed: {self.max_speed} km/h\n\t' \
               f'- consume: {self.consumption.resource}\n\t'
        consume_properties = self.consumption.get_unique_attributes()
        if consume_properties:
            info += f''.join([f'- {key}: {value}\n\t' for key, value in consume_properties.items()])
        return info

    @classmethod
    def move(cls):
        print(f"{cls.__name__} drives from A to B")
