#!/usr/bin/python3

"""
This class is composed of optional amenity details to be supplied
in addition to the baseclass i.e BaseModel class attributes. Also, it
inherit all its parent (all BaseModel) methods.

"""

from models.base_model import BaseModel


class Amenity(BaseModel):
    """This class contains all the optional amenity details to be supplied

    Attributes:
        Fields:
            name:string - The Amenity name
    """
    name = ""
