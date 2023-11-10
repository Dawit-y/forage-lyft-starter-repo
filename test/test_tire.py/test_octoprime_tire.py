import unittest
from tire.octoprime_tire import OctoprimeTire

class TestOctoprimeTire(unittest.TestCase):
    
    def test_octoprime_tire_needs_service(self):
        octoprime_tire = OctoprimeTire()
        tire_wear = [1.2, 0.7, 0.6, 0.6]
        self.assertTrue(octoprime_tire.needs_service(tire_wear))

    def test_octoprime_tire_does_not_need_service(self):
        octoprime_tire = OctoprimeTire()
        tire_wear = [0.5, 0.7, 0.8, 0.5]
        self.assertFalse(octoprime_tire.needs_service(tire_wear))