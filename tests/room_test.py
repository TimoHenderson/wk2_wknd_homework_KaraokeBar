import unittest
from src.room import Room
from src.song import Song


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

    def test_can_add_song(self):
        song = Song("Walk", "Pantera")
        self.room.add_song(song)
        actual = self.room.songs[0]
        expected = song
        self.assertEqual(actual, expected)
