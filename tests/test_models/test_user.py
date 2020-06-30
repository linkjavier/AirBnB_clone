#!/usr/bin/python3
"""
    Test for class User Model
"""
import unittest
import pep8
from datetime import datetime
from models import user
from models.user import User


class TestPep8B(unittest.TestCase):
    """ Check for pep8 validation. """
    def test_pep8(self):
        """ test base and test_base for pep8 conformance """
        style = pep8.StyleGuide(quiet=True)
        file1 = 'models/user.py'
        file2 = 'tests/test_models/test_user.py'
        result = style.check_files([file1, file2])
        self.assertEqual(result.total_errors, 0,
                         "Found code style errors (and warning).")


class TestDocsB(unittest.TestCase):
    """ Check for documentation. """
    def test_module_doc(self):
        """ check for module documentation """
        self.assertTrue(len(user.__doc__) > 0)

    def test_class_doc(self):
        """ check for documentation """
        self.assertTrue(len(user.__doc__) > 0)

    def test_method_docs(self):
        """ check for method documentation """
        for func in dir(User):
            self.assertTrue(len(func.__doc__) > 0)


class TestUser(unittest.TestCase):
    """Class TestBaseModel """
    def setUp(self):
        self.user_1 = User()
        self.user_2 = User()

    def check_instance(self):
        """ Check the existence of instance """
        self.assertIsInstance(self.user_1, User)
        self.assertIsInstance(self.user_2, User)

    def check_attributes(self):
        """ Checks str type for attributes """
        self.assertEqual(type(self.user_1.email), str)
        self.assertEqual(type(self.user_1.password), str)
        self.assertEqual(type(self.user_1.first_name), str)
        self.assertEqual(type(self.user_1.last_name), str)

if __name__ == '__main__':
    unittest.main()
