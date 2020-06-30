#!/usr/bin/python3
"""Unit test for the file storage class
"""
import unittest
# import json
import pep8
# from io import StringIO
# from unittest.mock import patch
from console import HBNBCommand


class TestBaseClass(unittest.TestCase):
    """TestBaseClass resume
    Args:
        unittest (): Propertys for unit testing
    """

    maxDiff = None

    def test_module_doc(self):
        """ check for module documentation """
        self.assertTrue(len(HBNBCommand.__doc__) > 0)

    def test_class_doc(self):
        """ check for documentation """
        self.assertTrue(len(HBNBCommand.__doc__) > 0)

    def test_method_docs(self):
        """ check for method documentation """
        for func in dir(HBNBCommand):
            self.assertTrue(len(func.__doc__) > 0)

    def test_pep8(self):
        """ test base and test_base for pep8 conformance """
        style = pep8.StyleGuide(quiet=True)
        file1 = 'console.py'
        file2 = 'tests/test_console.py'
        result = style.check_files([file1, file2])
        self.assertEqual(result.total_errors, 0,
                         "Found code style errors (and warning).")


if __name__ == '__main__':
    unittest.main()
