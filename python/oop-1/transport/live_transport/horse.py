from .live_transport import LiveTransport
from ..movable import Movable


class Horse(LiveTransport, Movable):
    def __init__(self, name, weight, seating_capacity, max_speed, consumption):
        super(Horse, self).__init__(name, weight, seating_capacity, max_speed, consumption)

    def __call__(self, *args, **kwargs):
        print("Igogo")
