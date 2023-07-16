#!/usr/bin/python3
""" Test Amenity class
"""
import unittest
from models.amenity import Amenity

class TestAmenity(unittest.TestCase):
    def test_amenity(self):
        amenity = Amenity()
        self.assertEqual(type(amenity.name), str)
