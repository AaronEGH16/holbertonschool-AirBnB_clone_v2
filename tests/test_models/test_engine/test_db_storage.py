#!/usr/bin/python3
""" Module for testing DB storage"""
import unittest
from models.base_model import BaseModel
from models import storage
import os

obj_storage = os.getenv("HBNB_TYPE_STORAGE")


class test_DbStorage(unittest.TestCase):
    """ Class to test the DB storage method """

    @unittest.skipIf(obj_storage != "db", "testing DB Storage Only")
    def setUp(self):
        """ Set up test environment """

    @unittest.skipIf(obj_storage != "db", "testing DB Storage Only")
    def test_new(self):
        """ New object is correctly added to __objects """

    @unittest.skipIf(obj_storage != "db", "testing DB Storage Only")
    def test_all(self):
        """ __objects is properly returned """

    @unittest.skipIf(obj_storage != "db", "testing DB Storage Only")
    def test_empty(self):
        """ Data is saved to DB """

    @unittest.skipIf(obj_storage != "db", "testing DB Storage Only")
    def test_save(self):
        """ DbStorage save method """

    @unittest.skipIf(obj_storage != "db", "testing DB Storage Only")
    def test_reload(self):
        """ Storage DB is successfully loaded """

    @unittest.skipIf(obj_storage != "db", "testing DB Storage Only")
    def test_reload_empty(self):
        """ Load from an empty DB """

    @unittest.skipIf(obj_storage != "db", "testing DB Storage Only")
    def test_reload_from_nonexistent(self):
        """ Nothing happens if DB does not exist """

    @unittest.skipIf(obj_storage != "db", "testing DB Storage Only")
    def test_type_objects(self):
        """ Confirm objects is a dict """

    @unittest.skipIf(obj_storage != "db", "testing DB Storage Only")
    def test_key_format(self):
        """ Key is properly formatted """

    @unittest.skipIf(obj_storage != "db", "testing DB Storage Only")
    def test_storage_var_created(self):
        """ DbStorage object storage created """
