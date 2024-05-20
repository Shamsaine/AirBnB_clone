#!/usr/bin/python3
"""
City module containing the City class
"""

from models.base_model import BaseModel


class City(BaseModel):
    """City class that inherits from BaseModel
    Attributes:
        state_id (str): The ID of the state the city belongs to.
        name (str): The name of the city.
    """
    state_id = ""
    name = ""
