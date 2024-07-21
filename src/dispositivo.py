from abc import ABC, abstractmethod

class Dispositivo(ABC):
    @abstractmethod
    def get_status(self):
        pass
