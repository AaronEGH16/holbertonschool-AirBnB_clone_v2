#!/usr/bin/python3
""" """
from tests.test_models.test_base_model import test_basemodel
from models.city import City
import os
import unittest

obj_storage = os.getenv('HBNB_TYPE_STORAGE')


class test_City(test_basemodel):
    """ """

    def __init__(self, *args, **kwargs):
        """ """
        super().__init__(*args, **kwargs)
        self.name = "City"
        self.value = City

    @unittest.skipIf(obj_storage != "fs", "testing File Storage Only")
    def test_state_id(self):
        """ """
        new = self.value()
        self.assertEqual(type(new.state_id), str)

    @unittest.skipIf(obj_storage != "fs", "testing File Storage Only")
    def test_name(self):
        """ """
        new = self.value()
        self.assertEqual(type(new.name), str)
