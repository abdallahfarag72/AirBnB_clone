#!/usr/bin/python3
""" Test Place class
"""
import unittest
from models.place import Place

class TestPlace(unittest.TestCase):
    def test_place(self):
        place = Place()
        self.assertEqual(type(place.city_id), str)
        self.assertEqual(type(place.user_id), str)
        self.assertEqual(type(place.name), str)
        self.assertEqual(type(place.description), str)

        self.assertEqual(type(place.number_rooms), int)
        self.assertEqual(type(place.number_bathrooms), int)
        self.assertEqual(type(place.max_guest), int)
        self.assertEqual(type(place.price_by_night), int)

        self.assertEqual(type(place.latitude), float)
        self.assertEqual(type(place.longitude), float)
        self.assertEqual(type(place.amenity_ids), list)
