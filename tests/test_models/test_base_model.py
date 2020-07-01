#!/usr/bin/python3
"""
    Test for class Base Model
"""
import unittest
import pep8
from datetime import datetime
from models import base_model
from models.base_model import BaseModel
import os


class TestPep8B(unittest.TestCase):
    """ Check for pep8 validation. """
    def test_pep8(self):
        """ test base and test_base for pep8 conformance """
        style = pep8.StyleGuide(quiet=True)
        file1 = 'models/base_model.py'
        file2 = 'tests/test_models/test_base_model.py'
        result = style.check_files([file1, file2])
        self.assertEqual(result.total_errors, 0,
                         "Found code style errors (and warning).")


class TestDocsB(unittest.TestCase):
    """ Check for documentation. """
    def test_module_doc(self):
        """ check for module documentation """
        self.assertTrue(len(base_model.__doc__) > 0)

    def test_class_doc(self):
        """ check for documentation """
        self.assertTrue(len(BaseModel.__doc__) > 0)

    def test_method_docs(self):
        """ check for method documentation """
        for func in dir(BaseModel):
            self.assertTrue(len(func.__doc__) > 0)


class TestBaseModel(unittest.TestCase):
    """Class TestBaseModel """
    def setUp(self):
        """set up """
        self.basemodel = BaseModel()
        self.basemodel2 = BaseModel()
        self.model0 = BaseModel()

    def tearDown(self):
        """ . """
        del self.basemodel
        del self.basemodel2
        del self.model0

    def check_instance(self):
        """ Check the existence of instance """
        self.assertIsInstance(self.basemodel, BaseModel)
        self.assertIsInstance(self.basemodel2, BaseModel)

    def check_id(self):
        """ ID equal and ID type Comparison """
        self.assertNotEqual(self.basemodel.id, self.basemodel2.id)
        self.assertEqual(type(self.basemodel.id), str)

    def check_save(self):
        """ Check the save method"""
        old_created_at = self.model0.created_at
        old_updated_at = self.model0.updated_at
        self.model0.save()
        new_created_at = self.model0.created_at
        new_updated_at = self.model0.updated_at
        self.assertNotEqual(old_updated_at, new_updated_at)
        self.assertEqual(old_created_at, new_created_at)

    def check_dic(self):
        """ Checks a correct dictionary"""
        date = "%Y-%m-%dT%H:%M:%S.%f"
        test_dic = self.basemodel.to_dict()
        self.assertEqual(type(test_dic["created_at"]), str)
        self.assertEqual(test_dic["__class__"], "BaseModel")
        self.assertEqual(test_dic["created_at"],
                         self.basemodel.created_at.strftime(date))
        self.assertEqual(test_dic["updated_at"],
                         self.basemodel.updated_at.strftime(date))

    def test_permissions(self):
        """test read-write-execute permissions"""
        read = os.access('models/base_model.py', os.R_OK)
        self.assertTrue(read)
        write = os.access('models/base_model.py', os.W_OK)
        self.assertTrue(write)
        exe = os.access('models/base_model.py', os.X_OK)
        self.assertTrue(exe)

    if __name__ == '__main__':
        unittest.main()
