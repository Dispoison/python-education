from .vehicle import Vehicle


class WaterTransport(Vehicle):
    def __init__(self, manufacturer, model, weight, seating_capacity, max_speed, consumption, volume_submerged):
        super(WaterTransport, self).__init__(manufacturer, model, weight, seating_capacity, max_speed, consumption)
        self._volume_submerged = volume_submerged

    @property
    def volume_submerged(self):
        """Displaced water volume"""
        return self._volume_submerged

    def __call__(self, *args, **kwargs):
        print("Wuwuwuwu")

    def get_info(self):
        return f'{super().get_info()}- volume submerged: {self.volume_submerged} liters'

