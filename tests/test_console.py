#!/usr/bin/python3
"""
    Test for console
"""
import console
from console import HBNBCommand
import unittest
import pep8
import os


class TestPep8B(unittest.TestCase):
    """ Check for pep8 validation. """
    def test_pep8(self):
        """ test base and test_base for pep8 conformance """
        style = pep8.StyleGuide(quiet=True)
        file1 = 'console.py'
        file2 = 'tests/test_console.py'
        result = style.check_files([file1, file2])
        self.assertEqual(result.total_errors, 0,
                         "Found code style errors (and warning).")


class TestDocsB(unittest.TestCase):
    """ Check for documentation. """
    def test_module_doc(self):
        """ check for module documentation """
        self.assertTrue(len(console.__doc__) > 0)

    def test_class_doc(self):
        """ check for documentation """
        self.assertTrue(len(HBNBCommand.__doc__) > 0)

    def test_method_docs(self):
        """ check for method documentation """
        for func in dir(HBNBCommand):
            self.assertTrue(len(func.__doc__) > 0)


class TestConsole(unittest.TestCase):
    """ Class TestConsole """

    def test_permissions(self):
        """test read-write-execute permissions"""
        read = os.access('console.py', os.R_OK)
        self.assertTrue(read)
        write = os.access('console.py', os.W_OK)
        self.assertTrue(write)
        exe = os.access('console.py', os.X_OK)
        self.assertTrue(exe)
