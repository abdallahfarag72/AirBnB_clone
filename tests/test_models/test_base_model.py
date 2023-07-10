#!/usr/bin/python3
"""test BaseModel class
"""
import unittest
from models.base_model import BaseModel

class TestBaseModel(unittest.TestCase):
    def test_id(self):
        x = BaseModel()
        y = BaseModel()
        self.assertIsInstance(x, BaseModel)
        self.assertTrue(hasattr(x, 'id'))
        self.assertIsInstance(x.id, str)
        self.assertNotEqual(x.id, y.id)

    def test_create_update_time(self):
        x = BaseModel()
        y = BaseModel()
        self.assertTrue(x.created_at < y.created_at)
        self.assertEqual(x.created_at, x.updated_at)
        self.assertTrue(x.updated_at < y.updated_at)

