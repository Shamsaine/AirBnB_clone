import unittest
from models.amenity import Amenity

class TestAmenity(unittest.TestCase):
    
    def setUp(self):
        self.instance = Amenity()

    def test_instance_creation(self):
        self.assertIsInstance(self.instance, Amenity)
    
    def test_name(self):
        self.assertTrue(hasattr(self.instance, "name"))

if __name__ == "__main__":
    unittest.main()
