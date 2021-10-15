"""Menu functionality."""


class Menu:
    """Menu class with dishes list"""
    dishes = []

    def __getitem__(self, item):
        return self.dishes[item]

    def __len__(self):
        return len(self.dishes)

    @classmethod
    def add(cls, dish):
        """Add dish to menu dish list"""
        cls.dishes.append(dish)
