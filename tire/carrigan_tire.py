from tire.tire import Tire


class CarriganTire(Tire):
    def needs_service(self, tire_wear):
        return any(wear >= 0.9 for wear in tire_wear)