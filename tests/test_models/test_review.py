#!/usr/bin/python3
""" Test Review class
"""
import unittest
from models.review import Review

class TestReview(unittest.TestCase):
    def test_review(self):
        review = Review()
        self.assertEqual(type(review.place_id), str)
        self.assertEqual(type(review.user_id), str)
        self.assertEqual(type(review.text), str)
