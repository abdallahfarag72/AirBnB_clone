#!/usr/bin/python3
""" test FileStorage
"""
import unittest


class TestFileStorage(unittest.TestCase):
    """ Test FileStorage Class
    """
    def test_all_method(self):
        """Test the .all() method
        """
        storage = FileStorage()
        assertEqual(type(storage.all()), dict)
