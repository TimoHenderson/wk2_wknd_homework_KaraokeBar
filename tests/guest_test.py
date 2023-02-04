import unittest
from src.guest import Guest


class TestGuest(unittest.TestCase):
    def setUp(self):
        self.guest = Guest("Fred", 15.00)

    def test_has_name(self):
        actual = self.guest.name
        expected = "Fred"
        self.assertEqual(actual, expected)

    def test_has_cash(self):
        actual = self.guest.cash
        expected = 15.00
        self.assertEqual(actual, expected)
