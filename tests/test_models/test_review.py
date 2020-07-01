#!/usr/bin/python3
"""Unit test for the file storage class
"""
import unittest
# import json
import pep8
from models import review
from models.review import Review
from models.base_model import BaseModel


class TestReviewClass(unittest.TestCase):
    """TestReviewClass test suite for the use
    of the review class
    Args:
        unittest (): Propertys for unit testing
    """

    maxDiff = None

    def setUp(self):
        """Return to "" class attributes"""
        Review.place_id = ""
        Review.user_id = ""
        Review.text = ""

    def test_module_doc(self):
        """ check for module documentation """
        self.assertTrue(len(review.__doc__) > 0)

    def test_class_doc(self):
        """ check for documentation """
        self.assertTrue(len(Review.__doc__) > 0)

    def test_method_docs(self):
        """ check for method documentation """
        for func in dir(Review):
            self.assertTrue(len(func.__doc__) > 0)

    def test_pep8(self):
        """ test base and test_base for pep8 conformance """
        style = pep8.StyleGuide(quiet=True)
        file1 = 'models/review.py'
        file2 = 'tests/test_models/test_review.py'
        result = style.check_files([file1, file2])
        self.assertEqual(result.total_errors, 0,
                         "Found code style errors (and warning).")

    def test_is_instance(self):
        """ Test if user is instance of basemodel """
        my_Review = Review()
        self.assertTrue(isinstance(my_Review, BaseModel))

    def test_field_types(self):
        """ Test field attributes of user """
        my_Review = Review()
        self.assertTrue(type(my_Review.place_id) == str)
        self.assertTrue(type(my_Review.user_id) == str)
        self.assertTrue(type(my_Review.text) == str)


if __name__ == '__main__':
    unittest.main()
