#!/usr/bin/python3
"""
    Test for class Review Model
"""
import unittest
import pep8
from datetime import datetime
from models import review
from models.review import Review


class TestPep8B(unittest.TestCase):
    """ Check for pep8 validation. """
    def test_pep8(self):
        """ test base and test_base for pep8 conformance """
        style = pep8.StyleGuide(quiet=True)
        file1 = 'models/review.py'
        file2 = 'tests/test_models/test_review.py'
        result = style.check_files([file1, file2])
        self.assertEqual(result.total_errors, 0,
                         "Found code style errors (and warning).")


class TestDocsB(unittest.TestCase):
    """ Check for documentation. """
    def test_module_doc(self):
        """ check for module documentation """
        self.assertTrue(len(review.__doc__) > 0)

    def test_class_doc(self):
        """ Check for documentation """
        self.assertTrue(len(review.__doc__) > 0)

    def test_method_docs(self):
        """ Check for method documentation """
        for func in dir(Review):
            self.assertTrue(len(func.__doc__) > 0)


class TestReview(unittest.TestCase):
    """Class TestReview """
    def setUp(self):
        self.review_1 = Review()
        self.review_2 = Review()

    def check_instance(self):
        """ Check the existence of instance """
        self.assertIsInstance(self.review_1, Review)
        self.assertIsInstance(self.review_2, Review)

    def check_attributes(self):
        """ Checks str type for attributes """
        self.assertEqual(type(self.review_1.place_id), str)
        self.assertEqual(type(self.review_1.user_id), str)
        self.assertEqual(type(self.review_1.text), str)

if __name__ == '__main__':
    unittest.main()
