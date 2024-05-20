# tests/mock_storage.py
from models.base_model import BaseModel

class MockStorage:
    __objects = {}

    def all(self):
        return self.__objects

    def new(self, obj):
        self.__objects[f"{obj.__class__.__name__}.{obj.id}"] = obj

    def save(self):
        pass

    def reload(self):
        pass

    def classes(self):
        return {
            "BaseModel": BaseModel
        }
