#!/usr/bin/python3
""" Test User class
"""
import unittest
from models.user import User


class TestUser(unittest.TestCase):
    def test_user(self):
        user1 = User()
        self.assertEqual(type(user1.email), str)
        self.assertEqual(type(user1.password), str)
        self.assertEqual(type(user1.first_name), str)
        self.assertEqual(type(user1.last_name), str)
