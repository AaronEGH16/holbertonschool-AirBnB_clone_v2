#!/usr/bin/python3

from models.base_model import BaseModel
from models.engine.db_storage import DBStorage
from models.engine.file_storage import FileStorage
from unittest.mock import patch
from console import HBNBCommand
import unittest
from uuid import UUID
import json
import os
from io import StringIO


class TestHBNBCommand(unittest.TestCase):
    """"""
    def test_EOF(self):
        """"""
        with patch('sys.stdout', new=StringIO()) as _output:
            self.HBNB = HBNBCommand()
            with self.assertRaises(SystemExit):
                self.HBNB.onecmd("EOF")
            self.assertEqual("\n", _output.getvalue())

    def test_quit(self):
        """"""
        with patch('sys.stdout', new=StringIO()) as _output:
            self.HBNB = HBNBCommand()
            with self.assertRaises(SystemExit):
                self.HBNB.onecmd("quit")
            self.assertEqual("", _output.getvalue())


if __name__ == "__main__":
    unittest.main()
