import unittest
from src.guest import Guest


class TestGuest(unittest.TestCase):
    def setUp(self):
        self.guest = Guest("Fred")

    def test_has_name(self):
        actual = self.guest.name
        expected = "Fred"
        self.assertEqual(actual, expected)
