#!/usr/bin/python3
"""
    Test for class Review Model
"""
import unittest
import pep8
from datetime import datetime
from models.base_model import BaseModel
from models.engine import file_storage
from models.engine.file_storage import FileStorage
import os


class TestPep8B(unittest.TestCase):
    """ Check for pep8 validation. """
    def test_pep8(self):
        """ test base and test_base for pep8 conformance """
        style = pep8.StyleGuide(quiet=True)
        file1 = 'models/engine/file_storage.py'
        file2 = 'tests/test_models/test_engine/test_file_storage.py'
        result = style.check_files([file1, file2])
        self.assertEqual(result.total_errors, 0,
                         "Found code style errors (and warning).")


class TestDocsB(unittest.TestCase):
    """ Check for documentation. """
    def test_module_doc(self):
        """ check for module documentation """
        self.assertTrue(len(file_storage.__doc__) > 0)

    def test_class_doc(self):
        """ Check for documentation """
        self.assertTrue(len(FileStorage.__doc__) > 0)

    def test_method_docs(self):
        """ Check for method documentation """
        for func in dir(FileStorage):
            self.assertTrue(len(func.__doc__) > 0)


class TestFileStorage(unittest.TestCase):
    """Class FileStorage """
    def setUp(self):
        """ Instance the FileStorage"""
        self.storage_1 = FileStorage()

    def check_instance(self):
        """ Check the existence of instance """
        self.assertIsInstance(self.storage_1, FileStorage)

    def check_all(self):
        """ Checks a correct dictionary """
        dic = self.storage_1.all()
        self.assertEqual(type(dic), dict)
        self.assertIs(dic, self.storage_1._FileStorage__objects)

    def test_permissions(self):
        """test read-write-execute permissions"""
        read = os.access('models/engine/file_storage.py', os.R_OK)
        self.assertTrue(read)
        write = os.access('models/engine/file_storage.py', os.W_OK)
        self.assertTrue(write)
        exe = os.access('models/engine/file_storage.py', os.X_OK)
        self.assertTrue(exe)


if __name__ == '__main__':
    unittest.main()
