#!/usr/bin/python3
"""This represents the City class."""


from models.base_model import BaseModel

class City(BaseModel):
    """Manages objects in the class
    Representing a city.
    Attributes:
        state_id (str): this is the state id.
        name (str): Name of the city.
    """
    state_id = ""
    name = ""
