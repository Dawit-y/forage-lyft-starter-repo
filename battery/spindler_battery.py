from battery.battery import Battery

class SpindlerBattery(Battery):
    def __init__(self, last_service_date, current_date) -> None:
        self._last_serive_date = last_service_date
        self._current_date = current_date

    def needs_service(self):
        if  self._current_date.year - self._last_serive_date.year > 2:
            return True
        else:
            return False