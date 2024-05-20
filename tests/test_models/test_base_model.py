import unittest
from models.base_model import BaseModel
import uuid
from datetime import datetime

class TestBaseModel(unittest.TestCase):
    
    def setUp(self):
        self.instance = BaseModel()

    def test_instance_creation(self):
        self.assertIsInstance(self.instance, BaseModel)
    
    def test_id(self):
        self.assertIsInstance(self.instance.id, str)
        self.assertEqual(len(self.instance.id), 36)
    
    def test_created_at(self):
        self.assertIsInstance(self.instance.created_at, datetime)
    
    def test_updated_at(self):
        self.assertIsInstance(self.instance.updated_at, datetime)

    def test_save(self):
        previous_updated_at = self.instance.updated_at
        self.instance.save()
        self.assertNotEqual(previous_updated_at, self.instance.updated_at)

    def test_to_dict(self):
        instance_dict = self.instance.to_dict()
        self.assertEqual(instance_dict['__class__'], 'BaseModel')
        self.assertIsInstance(instance_dict['created_at'], str)
        self.assertIsInstance(instance_dict['updated_at'], str)

if __name__ == "__main__":
    unittest.main()
