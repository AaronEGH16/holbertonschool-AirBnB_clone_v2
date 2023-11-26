#!/usr/bin/python3
""" """
from tests.test_models.test_base_model import test_basemodel
from models.review import Review
import os
import unittest

obj_storage = os.getenv('HBNB_TYPE_STORAGE')


class test_review(test_basemodel):
    """ """

    def __init__(self, *args, **kwargs):
        """ """
        super().__init__(*args, **kwargs)
        self.name = "Review"
        self.value = Review

    @unittest.skipIf(obj_storage != "fs", "testing File Storage Only")
    def test_place_id(self):
        """ """
        new = self.value()
        self.assertEqual(type(new.place_id), str)

    @unittest.skipIf(obj_storage != "fs", "testing File Storage Only")
    def test_user_id(self):
        """ """
        new = self.value()
        self.assertEqual(type(new.user_id), str)

    @unittest.skipIf(obj_storage != "fs", "testing File Storage Only")
    def test_text(self):
        """ """
        new = self.value()
        self.assertEqual(type(new.text), str)
