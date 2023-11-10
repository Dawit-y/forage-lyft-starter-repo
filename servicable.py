from abc import ABC, abstractclassmethod

class Serviceable(ABC):

    @abstractclassmethod
    def needs_service() -> bool:
        pass