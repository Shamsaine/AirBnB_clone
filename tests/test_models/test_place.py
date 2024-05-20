import unittest
from models.place import Place

class TestPlace(unittest.TestCase):
    
    def setUp(self):
        self.instance = Place()

    def test_instance_creation(self):
        self.assertIsInstance(self.instance, Place)
    
    def test_attributes(self):
        self.assertTrue(hasattr(self.instance, "city_id"))
        self.assertTrue(hasattr(self.instance, "user_id"))
        self.assertTrue(hasattr(self.instance, "name"))
        self.assertTrue(hasattr(self.instance, "description"))
        self.assertTrue(hasattr(self.instance, "number_rooms"))
        self.assertTrue(hasattr(self.instance, "number_bathrooms"))
        self.assertTrue(hasattr(self.instance, "max_guest"))
        self.assertTrue(hasattr(self.instance, "price_by_night"))
        self.assertTrue(hasattr(self.instance, "latitude"))
        self.assertTrue(hasattr(self.instance, "longitude"))
        self.assertTrue(hasattr(self.instance, "amenity_ids"))

if __name__ == "__main__":
    unittest.main()
