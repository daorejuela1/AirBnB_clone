#!/usr/bin/python3
"""Unit test for the class Place
"""
import unittest
# import json
import pep8
from models import place
from models.place import Place
from models.base_model import BaseModel


class TestPlaceClass(unittest.TestCase):
    """TestPlaceClass test suit for the place class
    Args:
        unittest (): Propertys for unit testing
    """

    maxDiff = None

    def setUp(self):
        """Return to "" class attributes"""
        Place.city_id = ""
        Place.user_id = ""
        Place.name = ""
        Place.description = ""
        Place.number_rooms = 0
        Place.number_bathrooms = 0
        Place.max_guest = 0
        Place.price_by_night = 0
        Place.latitude = 0.0
        Place.longitude = 0.0
        Place.amenity_ids = []

    def test_module_doc(self):
        """ check for module documentation """
        self.assertTrue(len(place.__doc__) > 0)

    def test_class_doc(self):
        """ check for documentation """
        self.assertTrue(len(Place.__doc__) > 0)

    def test_method_docs(self):
        """ check for method documentation """
        for func in dir(Place):
            self.assertTrue(len(func.__doc__) > 0)

    def test_pep8(self):
        """ test base and test_base for pep8 conformance """
        style = pep8.StyleGuide(quiet=True)
        file1 = 'models/place.py'
        file2 = 'tests/test_models/test_place.py'
        result = style.check_files([file1, file2])
        self.assertEqual(result.total_errors, 0,
                         "Found code style errors (and warning).")

    def test_is_instance(self):
        """ Test if user is instance of basemodel """
        my_place = Place()
        self.assertTrue(isinstance(my_place, BaseModel))

    def test_field_types(self):
        """ Test field attributes of user """
        self.assertTrue(type(Place.city_id) == str)
        self.assertTrue(type(Place.user_id) == str)
        self.assertTrue(type(Place.name) == str)
        self.assertTrue(type(Place.description) == str)
        self.assertTrue(type(Place.number_rooms) == int)
        self.assertTrue(type(Place.number_bathrooms) == int)
        self.assertTrue(type(Place.max_guest) == int)
        self.assertTrue(type(Place.price_by_night) == int)
        self.assertTrue(type(Place.latitude) == float)
        self.assertTrue(type(Place.longitude) == float)
        self.assertTrue(type(Place.amenity_ids) == list)


if __name__ == '__main__':
    unittest.main()
