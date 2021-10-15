from .vehicle import Vehicle


class AutoTransport(Vehicle):
    def __init__(self, manufacturer, model, weight, seating_capacity, max_speed, consumption, wheels):
        super(AutoTransport, self).__init__(manufacturer, model, weight, seating_capacity, max_speed, consumption)
        self._wheels = wheels

    @property
    def wheels(self):
        """Number of car wheels"""
        return self._wheels

    def __call__(self, *args, **kwargs):
        print("Beep-beep")

    def get_info(self):
        return f'{super().get_info()}- wheels: {self.wheels}'
