import unittest
from src.room import Room


class TestRoom(unittest.TestCase):
    def setUp(self):
        self.room = Room("Big Room")

    def test_has_name(self):
        actual = self.room.name
        expected = "Big Room"
        self.assertEqual(actual, expected)

    def test_has_songs(self):
        actual = self.room.songs
        expected = []
        self.assertEqual(actual, expected)

    def test_has_guests(self):
        actual = self.room.guests
        expected = []
        self.assertEqual(actual, expected)
