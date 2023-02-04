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

    def test_can_afford_to_pay__enough_cash(self):
        actual = self.guest.can_afford_to_pay(2.00)
        self.assertTrue(actual)

    def test_can_afford_to_pay__not_enough_cash(self):
        actual = self.guest.can_afford_to_pay(16.00)
        self.assertFalse(actual)
