#!/usr/bin/python3

from models.base_model import BaseModel
from models.engine.db_storage import DBStorage
from models.engine.file_storage import FileStorage
from console import HBNBCommand
import unittest
from uuid import UUID
import json
import os


class TestHBNBCommand(unittest.TestCase):
    """"""
    def EOF_test(self):
        """"""
        with patch('sys.stdout', new=StringIO()) as _output:
            self.HBNB.onecmd("EOF")
            self.assertEqual("\n", _output.getvalue())


if __name__ == "__main__":
    unittest.main()
