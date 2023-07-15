#!/usr/bin/python3
"""Defines the User class"""

from models.base_model import BaseModel


class User(BaseModel):
    """
    Defines a user and inherits from BaseModel
    """
    email = ""
    paswword = ""
    first_name = ""
    last_name = ""
