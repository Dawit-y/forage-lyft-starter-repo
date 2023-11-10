from abc import ABC, abstractmethod

class Tire(ABC):
    def __init__(self) -> None:
        pass

    @abstractmethod
    def needs_service(self, tire_wear):
        pass