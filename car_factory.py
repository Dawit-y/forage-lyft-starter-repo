from car import Car
from engine.capulet_engine import CapuletEngine
from engine.sternman_engine import SternmanEngine
from engine.willoughby_engine import WilloughbyEngine

from battery.nubbin_battery import NubbinBattery
from battery.spindler_battery import SpindlerBattery

from tire.octoprime_tire import OctoprimeTire
from tire.carrigan_tire import CarriganTire

class CarFactory:
    def __init__(self) -> None:
        pass

    def create_calliope(self, current_date, last_service_date, current_mileage, last_service_mileage):
        engine = CapuletEngine(current_mileage=current_mileage,last_service_mileage=last_service_mileage)
        battery = SpindlerBattery(last_service_date=last_service_date, current_date=current_date)
        tire = OctoprimeTire()
        car = Car(engine=engine, battery=battery, tire=tire)
        return car
    
    def create_glissade(self, current_date, last_service_date, current_mileage, last_service_mileage):
        engine = WilloughbyEngine(current_mileage=current_mileage,last_service_mileage=last_service_mileage)
        battery = SpindlerBattery(last_service_date=last_service_date, current_date=current_date)
        tire = CarriganTire()
        car = Car(engine=engine, battery=battery, tire=tire)
        return car
    
    def create_palindrome(self, current_date, last_service_date, warning_light_on):
        engine = SternmanEngine(warning_light_is_on=warning_light_on)
        battery = SpindlerBattery(last_service_date=last_service_date, current_date=current_date)
        tire = OctoprimeTire()
        car = Car(engine=engine, battery=battery, tire=tire)
        return car
    
    def create_rorschach(self, current_date, last_service_date, current_mileage, last_service_mileage):
        engine = WilloughbyEngine(current_mileage=current_mileage,last_service_mileage=last_service_mileage)
        battery = NubbinBattery(last_service_date=last_service_date, current_date=current_date)
        tire = CarriganTire()
        car = Car(engine=engine, battery=battery,tire=tire)
        return car
    
    def create_thovex(self, current_date, last_service_date, current_mileage, last_service_mileage):
        engine = CapuletEngine(current_mileage=current_mileage,last_service_mileage=last_service_mileage)
        battery = NubbinBattery(last_service_date=last_service_date, current_date=current_date)
        tire = OctoprimeTire()
        car = Car(engine=engine, battery=battery, tire=tire)
        return car
    