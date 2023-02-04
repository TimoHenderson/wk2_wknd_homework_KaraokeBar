import unittest
from src.guest import Guest
from src.song import Song


class TestGuest(unittest.TestCase):
    def setUp(self):
        self.guest = Guest("Fred", 15.00)
        self.song = Song("Walk", "Pantera")
        self.guest_with_fav_song = Guest("Jenny", 15.00, self.song)

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

    def test_pay_cash__enough_cash(self):
        success = self.guest.pay_cash(2.00)
        actual = self.guest.cash
        expected = 13.00
        self.assertEqual(actual, expected)
        self.assertTrue(success)

    def test_pay_cash__not_enough_cash(self):
        success = self.guest.pay_cash(16.00)
        actual = self.guest.cash
        expected = 15.00
        self.assertEqual(actual, expected)
        self.assertFalse(success)

    def test_has_favourite_song__default(self):
        actual = self.guest.favourite_song
        expected = None
        self.assertEqual(actual, expected)

    def test_has_favourite_song__initialised(self):
        actual = self.guest_with_fav_song.favourite_song
        expected = self.song
        self.assertEqual(actual, expected)
