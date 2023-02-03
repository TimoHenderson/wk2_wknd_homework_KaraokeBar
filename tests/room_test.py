import unittest
from src.room import Room


class TestRoom(unittest.TestCase):
    def setUp(self):
        self.room = Room("Big Room")

    def test_has_name(self):
        actual = self.room.name
        expected = "Big Room"
        self.assertEqual(actual, expected)
