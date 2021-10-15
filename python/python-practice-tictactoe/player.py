class Player:
    def __init__(self, name, sign):
        self.name = name
        self.sign = sign

    def __str__(self):
        return f'{self.name}[{self.sign}]'
