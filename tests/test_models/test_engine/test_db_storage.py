#!/usr/bin/python3
""" Module for testing DB storage"""
import unittest
from models.state import State
from models import storage
import os

obj_storage = os.getenv("HBNB_TYPE_STORAGE")


class test_DbStorage(unittest.TestCase):
    """ Class to test the DB storage method """

    @unittest.skipIf(obj_storage != "db", "testing DB Storage Only")
    def test_new(self):
        """ New object is correctly added to DB """
        new = State(name="Washington")
        new.save()
        key = f"{new.__class__.__name__}.{new.id}"
        self.assertEqual(new, storage.all()[key])

    @unittest.skipIf(obj_storage != "db", "testing DB Storage Only")
    def test_all(self):
        """ db objects is properly returned """
        new = State(name="California")
        new.save()
        db_obj = storage.all()
        self.assertIsInstance(db_obj, dict)

    @unittest.skipIf(obj_storage != "db", "testing DB Storage Only")
    def test_empty(self):
        """ Data is saved to DB """
        new = State(name="Texas")
        new.save()
        db_obj = storage.all()
        self.assertNotEqual(len(db_obj), 0)

    @unittest.skipIf(obj_storage != "db", "testing DB Storage Only")
    def test_reload(self):
        """ Storage DB is successfully loaded """
        new = State(name="Kansas")
        new.save()
        key = f"{new.__class__.__name__}.{new.id}"
        new = None
        self.assertEqual(new, None)
        storage.close()
        storage.reload()
        new = storage.all()[key]
        self.assertIsInstance(new, State)

    @unittest.skipIf(obj_storage != "db", "testing DB Storage Only")
    def test_reload_empty(self):
        """ Load from an empty DB """
        storage.close()
        storage.__init__()
        storage.reload()
        db_obj = storage.all()
        self.assertEqual(len(db_obj), 0)

    @unittest.skipIf(obj_storage != "db", "testing DB Storage Only")
    def test_type_objects(self):
        """ Confirm objects is a dict """
        new = State(name="New York")
        new.save()
        key = f"{new.__class__.__name__}.{new.id}"
        db_obj = storage.all()[key]
        self.assertIsInstance(db_obj.to_dict(), dict)

    @unittest.skipIf(obj_storage != "db", "testing DB Storage Only")
    def test_key_format(self):
        """ Key is properly formatted """
        new = State(name="Arizona")
        new.save()
        key = f"{new.__class__.__name__}.{new.id}"
        db_obj = storage.all()
        self.assertIn(key, db_obj)

    @unittest.skipIf(obj_storage != "db", "testing DB Storage Only")
    def test_storage_var_created(self):
        """ DbStorage object storage created """
        from models.engine.db_storage import DBStorage
        print(type(storage))
        self.assertEqual(type(storage), DBStorage)
