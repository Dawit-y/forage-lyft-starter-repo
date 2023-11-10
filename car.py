from servicable import Serviceable

class Car(Serviceable):
    def __init__(self, engine, battery, tire):
        self._engine = engine
        self._battery = battery
        self._tire = tire

    def needs_service(self):
        pass
