# Class that controls the storage of objects in files
import json

from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review
from models.user import User
from models.base_model import BaseModel


class FileStorage:
    """FileStorage class responsible for managing storage of objects in files
    
    Attributes:
        __file_path (str): The path to the file where objects are stored.
        __objects (dict): A dictionary containing the objects stored in memory.
    """
    __file_path = "file.json"
    __objects = {
        "State": State,
        "City": City,
        "Amenity": Amenity,
        "Place": Place,
        "Review": Review,
        "User": User
    }

    def all(self):
        """Return all objects currently stored in memory
        
        Returns:
            dict: A dictionary containing all objects stored in memory.
        """
        return self.__objects

    def new(self, obj):
        """Add a new object to the storage
        
        Args:
            obj (BaseModel): The object to be added to storage.
        """
        key = "{}.{}".format(obj.__class__.__name__, obj.id)
        self.__objects[key] = obj

    def save(self):
        """Save all objects currently stored in memory to a file"""
        serialized_objects = {key: obj.to_dict() for key, obj in self.__objects.items()}
        with open(self.__file_path, 'w') as file:
            json.dump(serialized_objects, file)

    def reload(self):
        """Reload objects from file into memory"""
        try:
            with open(self.__file_path, 'r') as file:
                data = json.load(file)
                for key, value in data.items():
                    class_name, obj_id = key.split('.')
                    obj = eval(class_name)(**value)
                    self.__objects[key] = obj
        except FileNotFoundError:
            pass
