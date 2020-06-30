#!/usr/bin/python3
"""Unit test for the file storage class
"""
import unittest
# import json
import pep8
from models.city import City
from models.base_model import BaseModel


class TestUserClass(unittest.TestCase):
    """TestUserClass resume
    Args:
        unittest (): Propertys for unit testing
    """

    maxDiff = None

    def setUp(self):
        """Return to "" class attributes"""
        City.name = ""
        City.state_id = ""

    def test_module_doc(self):
        """ check for module documentation """
        self.assertTrue(len(City.__doc__) > 0)

    def test_class_doc(self):
        """ check for documentation """
        self.assertTrue(len(City.__doc__) > 0)

    def test_method_docs(self):
        """ check for method documentation """
        for func in dir(City):
            self.assertTrue(len(func.__doc__) > 0)

    def test_pep8(self):
        """ test base and test_base for pep8 conformance """
        style = pep8.StyleGuide(quiet=True)
        file1 = 'models/city.py'
        file2 = 'tests/test_models/test_city.py'
        result = style.check_files([file1, file2])
        self.assertEqual(result.total_errors, 0,
                         "Found code style errors (and warning).")

    def test_is_instance(self):
        """ Test if user is instance of basemodel """
        my_city = City()
        self.assertTrue(isinstance(my_city, BaseModel))

    def test_field_types(self):
        """ Test field attributes of user """
        my_city = City()
        self.assertTrue(type(my_city.name) == str)
        self.assertTrue(type(my_city.state_id) == str)


if __name__ == '__main__':
    unittest.main()
