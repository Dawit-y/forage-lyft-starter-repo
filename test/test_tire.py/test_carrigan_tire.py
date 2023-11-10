import unittest
from tire.carrigan_tire import CarriganTire

class TestCarriganTire(unittest.TestCase):
    
    def test_carrigan_tire_needs_service(self):
        carrigan_tire = CarriganTire()
        tire_wear = [0.8, 0.9, 0.85, 0.92]
        self.assertTrue(carrigan_tire.needs_service(tire_wear))

    def test_carrigan_tire_does_not_need_service(self):
        carrigan_tire = CarriganTire()
        tire_wear = [0.8, 0.85, 0.88, 0.89]
        self.assertFalse(carrigan_tire.needs_service(tire_wear))