from .vehicle import Vehicle


class AirTransport(Vehicle):
    def __init__(self, manufacturer, model, weight, seating_capacity, max_speed, consumption, max_altitude):
        super(AirTransport, self).__init__(manufacturer, model, weight, seating_capacity, max_speed, consumption)
        self._max_altitude = max_altitude

    @property
    def max_altitude(self):
        return self._max_altitude

    def __call__(self, *args, **kwargs):
        print("Whiyuuuu")

    def get_info(self):
        return f'{super().get_info()}- max altitude: {self.max_altitude} m'
