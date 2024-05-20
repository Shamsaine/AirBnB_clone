import unittest
from models.review import Review

class TestReview(unittest.TestCase):
    
    def setUp(self):
        self.instance = Review()

    def test_instance_creation(self):
        self.assertIsInstance(self.instance, Review)
    
    def test_attributes(self):
        self.assertTrue(hasattr(self.instance, "place_id"))
        self.assertTrue(hasattr(self.instance, "user_id"))
        self.assertTrue(hasattr(self.instance, "text"))

if __name__ == "__main__":
    unittest.main()
