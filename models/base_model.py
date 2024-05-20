#!/usr/bin/python3  # Use python3 for shebang

"""Base class for all models in the project.

Defines common attributes and methods for other classes to inherit.
"""

import models
import uuid
from datetime import datetime


class BaseModel:
    """
    The BaseModel class serves as the foundation
    for all models in the application.
    It defines common attributes (id, created_at, updated_at) and methods.

    Attributes:
        id (str): A unique string identifier generated using UUID.
        created_at (datetime): The datetime when the instance is created.
        updated_at (datetime): The datetime when the instance is last updated.

    """

    def __init__(self, *args: object, **kwargs: dict) -> None:
        """
        Initializes the base model with attributes
        from a dictionary (if provided).

        Args:
            *args (object, optional): Unused arguments. Defaults to object.
            **kwargs (dict, optional): Dictionary containing attributes
            for the model. Defaults to dict.

        Raises:
            ValueError: If 'created_at' or 'updated_at' is present in kwargs
            but not a valid ISO format string.
        """

        if kwargs:
            for key, value in kwargs.items():
                if key in ("created_at", "updated_at"):
                    try:
                        value = datetime.strptime(
                            value, "%Y-%m-%dT%H:%M:%S.%f"
                            )
                    except ValueError:
                        raise ValueError(
                            "Invalid datetime format for {}. Expected ISO format.".format(key)
                            )
                    setattr(self, key, value)
                else:
                    setattr(self, key, value)
        else:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = self.created_at
        models.storage.new(self)  # Call storage to save the instance

    def __str__(self) -> str:
        """
        Returns a string representation of the model instance.

        Returns:
            str: A string representation of the object in the format:
                [<class name>] (<id>) <attributes>
        """
        return f"[{self.__class__.__name__}] ({self.id}) {self.__dict__}"

    def save(self) -> None:
        """
        Updates the updated_at attribute with the current datetime.
        """
        self.updated_at = datetime.now()

    def to_dict(self) -> dict:
        """
        Returns a dictionary representation of the model instance.

        Returns:
            dict: A dictionary containing all attributes from __dict__,
                  class name, and formatted timestamps (ISO format).
        """
        obj_dict = self.__dict__.copy()
        obj_dict["__class__"] = self.__class__.__name__
        obj_dict["created_at"] = self.created_at.isoformat()
        obj_dict["updated_at"] = self.updated_at.isoformat()
        return obj_dict
