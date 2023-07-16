#!/usr/bin/python3
""" Test City class
"""
import unittest
from models.city import City

class TestCity(unittest.TestCase):
    def test_city(self):
        city = City()
        self.assertEqual(type(city.state_id), str)
        self.assertEqual(type(city.name), str)
