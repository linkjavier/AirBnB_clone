#!/usr/bin/python3
"""
    Test for class City Model
"""
import unittest
import pep8
from datetime import datetime
from models import city
from models.city import City


class TestPep8B(unittest.TestCase):
    """ Check for pep8 validation. """
    def test_pep8(self):
        """ test base and test_base for pep8 conformance """
        style = pep8.StyleGuide(quiet=True)
        file1 = 'models/city.py'
        file2 = 'tests/test_models/test_city.py'
        result = style.check_files([file1, file2])
        self.assertEqual(result.total_errors, 0,
                         "Found code style errors (and warning).")


class TestDocsB(unittest.TestCase):
    """ Check for documentation. """
    def test_module_doc(self):
        """ check for module documentation """
        self.assertTrue(len(city.__doc__) > 0)

    def test_class_doc(self):
        """ Check for documentation """
        self.assertTrue(len(city.__doc__) > 0)

    def test_method_docs(self):
        """ Check for method documentation """
        for func in dir(City):
            self.assertTrue(len(func.__doc__) > 0)


class TestCity(unittest.TestCase):
    """Class TestCity """
    def setUp(self):
        self.city_1 = City()
        self.city_2 = City()

    def check_instance(self):
        """ Check the existence of instance """
        self.assertIsInstance(self.city_1, City)
        self.assertIsInstance(self.city_2, City)

    def check_attributes(self):
        """ Checks str type for attributes """
        self.assertEqual(type(self.city_1.name), str)
        self.assertEqual(type(self.city_1.state_id), str)

if __name__ == '__main__':
    unittest.main()
