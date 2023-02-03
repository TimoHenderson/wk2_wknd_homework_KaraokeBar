import unittest
from src.karaoke_bar import KaraokeBar


class TestKaraokeBar(unittest.TestCase):
    def setUp(self):
        self.karaoke_bar = KaraokeBar("K Bar")

    def test_has_name(self):
        actual = self.karaoke_bar.name
        expected = "K Bar"
        self.assertEqual(actual, expected)
