from tire.tire import Tire


class OctoprimeTire(Tire):
    def needs_service(self, tire_wear):
        return sum(tire_wear) >= 3