#!/usr/bin/python3
"""Unit test for the base class base model
"""
import unittest
# import json
import pep8
from datetime import datetime
# from io import StringIO
# from unittest.mock import patch
from models import base_model
from models.base_model import BaseModel
from models.engine.file_storage import FileStorage
import os


class TestBaseClass(unittest.TestCase):
    """TestBaseClass Test the base class
    Args:
        unittest (): Propertys for unit testing
    """

    maxDiff = None

    def setUp(self):
        """ condition to test file saving """
        with open("test.json", 'w'):
            FileStorage._FileStorage__file_path = "test.json"
            FileStorage._FileStorage__objects = {}

    def tearDown(self):
        """ destroys created file """
        FileStorage._FileStorage__file_path = "file.json"
        try:
            os.remove("test.json")
        except FileNotFoundError:
            pass

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

    def test_pep8(self):
        """ test base and test_base for pep8 conformance """
        style = pep8.StyleGuide(quiet=True)
        file1 = 'models/base_model.py'
        file2 = 'tests/test_models/test_base_model.py'
        result = style.check_files([file1, file2])
        self.assertEqual(result.total_errors, 0,
                         "Found code style errors (and warning).")

    def test_id_type(self):
        """ Test id type"""
        my_third = BaseModel()
        self.assertTrue(type(my_third.id) == str)

    def test_datetime_type(self):
        """ Test datetime type """
        my_third = BaseModel()
        self.assertTrue(type(my_third.created_at) == datetime)

    def test_str(self):
        """ Test str output """
        test = BaseModel()
        self.assertEqual(test.__str__(), "[" + test.__class__.__name__ + "]"
                         " (" + test.id + ") " + str(test.__dict__))

    def test_id_creation(self):
        """ check for module documentation """
        my_first = BaseModel()
        my_second = BaseModel()
        my_third = BaseModel()
        self.assertTrue(my_first.id != my_second.id)
        self.assertTrue(my_third.id != my_second.id)
        self.assertTrue(my_first.id != my_third.id)

    def test_to_dict(self):
        """testing to dict function"""
        test = BaseModel()
        my_model = test.to_dict()
        self.assertTrue(type(my_model["created_at"] == str))
        self.assertTrue(type(my_model["updated_at"] == str))
        self.assertTrue(type(test.created_at) == datetime)
        self.assertTrue(type(test.updated_at) == datetime)
        self.assertEqual(my_model["created_at"], test.created_at.isoformat())
        self.assertEqual(my_model["updated_at"], test.updated_at.isoformat())

    def test_base_from_dict(self):
        """Testing task 4, with kwargs init"""
        my_model = BaseModel()
        my_model_json = my_model.to_dict()
        my_new_model = BaseModel(**my_model_json)
        self.assertEqual(my_model_json, my_new_model.to_dict())
        self.assertTrue(type(my_new_model.id) == str)
        self.assertTrue(type(my_new_model.created_at) == datetime)
        self.assertTrue(type(my_new_model.updated_at) == datetime)

    def test_base_from_emp_dict(self):
        """test with an empty dictionary"""
        my_dict = {}
        my_new_model = BaseModel(**my_dict)
        self.assertTrue(type(my_new_model.id) == str)
        self.assertTrue(type(my_new_model.created_at) == datetime)
        self.assertTrue(type(my_new_model.updated_at) == datetime)

    def test_base_from_non_dict(self):
        """test with a None dictionary"""
        my_new_model = BaseModel(None)
        self.assertTrue(type(my_new_model.id) == str)
        self.assertTrue(type(my_new_model.created_at) == datetime)
        self.assertTrue(type(my_new_model.updated_at) == datetime)

    def test_save(self):
        """ test save method of basemodel """
        my_new_model = BaseModel()
        previous = my_new_model.updated_at
        my_new_model.save()
        actual = my_new_model.updated_at
        self.assertTrue(actual > previous)

    def test_isinstance(self):
        """ Check if object is basemodel instance """
        obj = BaseModel()
        self.assertIsInstance(obj, BaseModel)

    def test_executable_file(self):
        """ Check if file have permissions to execute"""
        # Check for read access
        is_read_true = os.access('models/base_model.py', os.R_OK)
        self.assertTrue(is_read_true)
        # Check for write access
        is_write_true = os.access('models/base_model.py', os.W_OK)
        self.assertTrue(is_write_true)
        # Check for execution access
        is_exec_true = os.access('models/base_model.py', os.X_OK)
        self.assertTrue(is_exec_true)

if __name__ == '__main__':
    unittest.main()
