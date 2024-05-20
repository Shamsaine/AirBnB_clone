import unittest
from models.state import State

class TestState(unittest.TestCase):
    
    def setUp(self):
        self.instance = State()

    def test_instance_creation(self):
        self.assertIsInstance(self.instance, State)
    
    def test_name(self):
        self.assertTrue(hasattr(self.instance, "name"))

if __name__ == "__main__":
    unittest.main()
