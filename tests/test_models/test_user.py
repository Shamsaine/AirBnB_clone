import unittest
from models.user import User

class TestUser(unittest.TestCase):
    
    def setUp(self):
        self.instance = User()

    def test_instance_creation(self):
        self.assertIsInstance(self.instance, User)
    
    def test_attributes(self):
        self.assertTrue(hasattr(self.instance, "email"))
        self.assertTrue(hasattr(self.instance, "password"))
        self.assertTrue(hasattr(self.instance, "first_name"))
        self.assertTrue(hasattr(self.instance, "last_name"))

if __name__ == "__main__":
    unittest.main()
