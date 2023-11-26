#!/usr/bin/python3
""" """
from tests.test_models.test_base_model import test_basemodel
from models.amenity import Amenity
import os
import unittest

obj_storage = os.getenv('HBNB_TYPE_STORAGE')


class test_Amenity(test_basemodel):
    """ """

    def __init__(self, *args, **kwargs):
        """ """
        super().__init__(*args, **kwargs)
        self.name = "Amenity"
        self.value = Amenity

    @unittest.skipIf(obj_storage != "fs", "testing File Storage Only")
    def test_name2(self):
        """ """
        new = self.value()
        self.assertEqual(type(new.name), str)
