import unittest
from src.song import Song


class TestSong(unittest.TestCase):
    def setUp(self):
        self.song = Song("Walk")

    def test_has_name(self):
        actual = self.song.name
        expected = "Walk"
        self.assertEqual(actual, expected)
