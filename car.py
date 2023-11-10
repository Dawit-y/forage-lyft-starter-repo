from servicable import Serviceable

class Car(Serviceable):
    def __init__(self, engine, battery ):
        self._engine = engine
        self._battery = battery

    def needs_service(self):
        pass
