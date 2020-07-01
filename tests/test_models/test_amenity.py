#!/usr/bin/python3
"""Unit test for the file storage class
"""
import unittest
# import json
import pep8
from models import amenity
from models.amenity import Amenity
from models.base_model import BaseModel
from models import storage
import os


class TestAmenityClass(unittest.TestCase):
    """TestAmenityClass test for the inheretit class
    Amenity, this tests that the output is as expected
    Args:
        unittest (): Propertys for unit testing
    """

    def tearDown(self):
        """ destroys created file """
        storage._FileStorage__file_path = "file.json"
        try:
            os.remove("test.json")
        except FileNotFoundError:
            pass

    def setUp(self):
        """Return to "" class attributes"""
        with open("test.json", 'w'):
            storage._FileStorage__file_path = "test.json"
            storage._FileStorage__objects = {}
        Amenity.name = ""

    def test_module_doc(self):
        """ check for module documentation """
        self.assertTrue(len(amenity.__doc__) > 0)

    def test_class_doc(self):
        """ check for documentation """
        self.assertTrue(len(Amenity.__doc__) > 0)

    def test_method_docs(self):
        """ check for method documentation """
        for func in dir(Amenity):
            self.assertTrue(len(func.__doc__) > 0)

    def test_pep8(self):
        """ test base and test_base for pep8 conformance """
        style = pep8.StyleGuide(quiet=True)
        file1 = 'models/amenity.py'
        file2 = 'tests/test_models/test_amenity.py'
        result = style.check_files([file1, file2])
        self.assertEqual(result.total_errors, 0,
                         "Found code style errors (and warning).")

    def test_is_instance(self):
        """ Test if user is instance of basemodel """
        my_Amenity = Amenity()
        self.assertTrue(isinstance(my_Amenity, BaseModel))

    def test_field_types(self):
        """ Test field attributes of user """
        my_Amenity = Amenity()
        self.assertTrue(type(my_Amenity.name) == str)


if __name__ == '__main__':
    unittest.main()
