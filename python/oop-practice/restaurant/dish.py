"""Dish functionality."""


from .menu import Menu


class Dish:
    """Dish class."""
    def __init__(self, name, category, price, weight):
        self.name = name
        self.category = category
        self.price = price
        self.weight = weight
        Menu.add(self)

    def __repr__(self):
        return self.name
