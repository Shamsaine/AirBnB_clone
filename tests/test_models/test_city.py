import unittest
from models.city import City

class TestCity(unittest.TestCase):
    
    def setUp(self):
        self.instance = City()

    def test_instance_creation(self):
        self.assertIsInstance(self.instance, City)
    
    def test_attributes(self):
        self.assertTrue(hasattr(self.instance, "state_id"))
        self.assertTrue(hasattr(self.instance, "name"))

if __name__ == "__main__":
    unittest.main()
