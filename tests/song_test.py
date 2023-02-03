import unittest
from src.song import Song


class TestSong(unittest.TestCase):
    def setUp(self):
        self.song = Song("Walk", "Pantera")

    def test_has_name(self):
        actual = self.song.name
        expected = "Walk"
        self.assertEqual(actual, expected)

    def test_has_artist(self):
        actual = self.song.artist
        expected = "Pantera"
        self.assertEqual(actual, expected)
