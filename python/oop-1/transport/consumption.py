from abc import ABC, abstractmethod


class Consumption(ABC):
    @property
    def resource(self):
        return self._resource

    @abstractmethod
    def get_unique_attributes(self):
        """Returns dictionary of unique attributes"""
        pass


class FuelConsumption(Consumption):
    def __init__(self, tank_volume):
        self._tank_volume = tank_volume
        self._resource = 'fuel'

    @property
    def tank_volume(self):
        """Fuel tank volume in liters"""
        return self._tank_volume

    def get_unique_attributes(self):
        return {'tank volume': self.tank_volume}


class ElectricityConsumption(Consumption):
    def __init__(self, battery_type):
        self._battery_type = battery_type
        self._resource = 'electricity'

    @property
    def battery_type(self):
        """Transport battery type"""
        return self._battery_type

    def get_unique_attributes(self):
        return {'battery type': self.battery_type}


class MechanicalEnergyConsumption(Consumption):
    def __init__(self):
        self._resource = 'mechanical energy'

    def get_unique_attributes(self):
        return None


class OrganicEnergyConsumption(Consumption):
    def __init__(self, food_weight_rate):
        self._resource = 'organic food'
        self._food_weight_rate = food_weight_rate

    @property
    def food_weight_rate(self):
        """Percentage of food per body weight"""
        return self._food_weight_rate

    def get_unique_attributes(self):
        return {'food weight rate': self.food_weight_rate}

    @staticmethod
    def calc_food_amount(weight, food_weight_rate):
        return weight * food_weight_rate

