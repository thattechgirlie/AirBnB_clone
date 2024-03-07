#!/usr/bin/python3
"""This is a representatio of class Review."""

from models.base_model import BaseModel

class Review(BaseModel):
    """Manages objects in class Review
    Representing a review.
    Attributes:
        place_id (str): This is the Place id.
        user_id (str): This is the User id.
        text (str): This is the text to review.
    """

    place_id = ""
    user_id = ""
    text = ""
