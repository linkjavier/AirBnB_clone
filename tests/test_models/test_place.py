#!/usr/bin/python3
"""
    Test for class Place Model
"""
import unittest
import pep8
from datetime import datetime
from models import place
from models.place import Place


class TestPep8B(unittest.TestCase):
    """ Check for pep8 validation. """
    def test_pep8(self):
        """ test base and test_base for pep8 conformance """
        style = pep8.StyleGuide(quiet=True)
        file1 = 'models/place.py'
        file2 = 'tests/test_models/test_place.py'
        result = style.check_files([file1, file2])
        self.assertEqual(result.total_errors, 0,
                         "Found code style errors (and warning).")


class TestDocsB(unittest.TestCase):
    """ Check for documentation. """
    def test_module_doc(self):
        """ check for module documentation """
        self.assertTrue(len(place.__doc__) > 0)

    def test_class_doc(self):
        """ Check for documentation """
        self.assertTrue(len(place.__doc__) > 0)

    def test_method_docs(self):
        """ Check for method documentation """
        for func in dir(Place):
            self.assertTrue(len(func.__doc__) > 0)


class TestPlace(unittest.TestCase):
    """Class TestPlace """
    def setUp(self):
        self.place_1 = Place()
        self.place_2 = Place()

    def check_instance(self):
        """ Check the existence of instance """
        self.assertIsInstance(self.place_1, Place)
        self.assertIsInstance(self.place_2, Place)

    def check_attributes(self):
        """ Checks str type for attributes """
        self.assertEqual(type(self.place_1.city_id), str)
        self.assertEqual(type(self.place_1.user_id), str)
        self.assertEqual(type(self.place_1.name), str)
        self.assertEqual(type(self.place_1.description), str)
        self.assertEqual(type(self.place_1.number_rooms), int)
        self.assertEqual(type(self.place_1.number_bathrooms), int)
        self.assertEqual(type(self.place_1.max_guest), int)
        self.assertEqual(type(self.place_1.price_by_night), int)
        self.assertEqual(type(self.place_1.latitude), float)
        self.assertEqual(type(self.longitude), float)
        self.assertEqual(type(self.amenity_ids), list)

if __name__ == '__main__':
    unittest.main()
