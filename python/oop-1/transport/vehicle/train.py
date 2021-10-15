from .vehicle import Vehicle


class Train(Vehicle):
    def __init__(self, manufacturer, model, weight, seating_capacity, max_speed, consumption, wagons):
        super(Train, self).__init__(manufacturer, model, weight, seating_capacity, max_speed, consumption)
        self._wheels = wagons

    @property
    def wagons(self):
        """Number of train wagons"""
        return self._wheels

    def __call__(self, *args, **kwargs):
        print("Toot-toot")

    def get_info(self):
        return f'{super().get_info()}- wagons: {self.wagons}'
