from abc import ABC, abstractmethod


class Transport(ABC):
    @abstractmethod
    def __call__(self, *args, **kwargs):
        pass

    @abstractmethod
    def get_info(self):
        pass

    @classmethod
    @abstractmethod
    def move(cls):
        pass
