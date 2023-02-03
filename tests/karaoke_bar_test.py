import unittest
from src.karaoke_bar import KaraokeBar
from src.room import Room


class TestKaraokeBar(unittest.TestCase):
    def setUp(self):
        self.rooms = [Room("Big Room"), Room("Medium Room"), Room("Small Room")]
        self.karaoke_bar = KaraokeBar("K Bar", self.rooms)

    def test_has_name(self):
        actual = self.karaoke_bar.name
        expected = "K Bar"
        self.assertEqual(actual, expected)

    def test_has_rooms(self):
        actual = self.karaoke_bar.rooms
        expected = self.rooms
        self.assertEqual(actual, expected)
