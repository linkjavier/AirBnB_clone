#!/usr/bin/python3
"""
    Test for class Amenity Model
"""
import unittest
import pep8
from datetime import datetime
from models import amenity
from models.amenity import Amenity


class TestPep8B(unittest.TestCase):
    """ Check for pep8 validation. """
    def test_pep8(self):
        """ test base and test_base for pep8 conformance """
        style = pep8.StyleGuide(quiet=True)
        file1 = 'models/amenity.py'
        file2 = 'tests/test_models/test_amenity.py'
        result = style.check_files([file1, file2])
        self.assertEqual(result.total_errors, 0,
                         "Found code style errors (and warning).")


class TestDocsB(unittest.TestCase):
    """ Check for documentation. """
    def test_module_doc(self):
        """ check for module documentation """
        self.assertTrue(len(amenity.__doc__) > 0)

    def test_class_doc(self):
        """ Check for documentation """
        self.assertTrue(len(amenity.__doc__) > 0)

    def test_method_docs(self):
        """ Check for method documentation """
        for func in dir(Amenity):
            self.assertTrue(len(func.__doc__) > 0)


class TestAmenity(unittest.TestCase):
    """Class TestAmenity """
    def setUp(self):
        self.amenity_1 = Amenity()
        self.amenity_2 = Amenity()

    def check_instance(self):
        """ Check the existence of instance """
        self.assertIsInstance(self.amenity_1, amenity)
        self.assertIsInstance(self.amenity_2, amenity)

    def check_attributes(self):
        """ Checks str type for attributes """
        self.assertEqual(type(self.amenity_1.name), str)

if __name__ == '__main__':
    unittest.main()
