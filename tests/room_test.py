import unittest
from src.room import Room
from src.song import Song
from src.guest import Guest


class TestRoom(unittest.TestCase):
    def setUp(self):
        self.room = Room("Small Room", 1)

    def test_has_name(self):
        actual = self.room.name
        expected = "Small Room"
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

    def test_can_check_in_guest__has_space(self):
        guest = Guest("Fred Fudge")
        successful = self.room.check_in(guest)
        actual = self.room.guests[0]
        expected = guest
        self.assertEqual(actual, expected)
        self.assertTrue(successful)

    def test_can_check_in_guest__no_space(self):
        guest = Guest("Fred Fudge")
        guest2 = Guest("Arnold Clark")
        self.room.check_in(guest)
        successful = self.room.check_in(guest2)
        actual = self.room.guests[0]
        expected = guest
        self.assertEqual(actual, expected)
        self.assertFalse(successful)
        self.assertEqual(len(self.room.guests), 1)

    def test_can_check_out_guest(self):
        guest = Guest("Fred Fudge")
        self.room.check_in(guest)
        self.room.check_out(guest)
        actual = self.room.guests
        expected = []
        self.assertEqual(actual, expected)

    def test_has_capacity(self):
        actual = self.room.capacity
        expected = 1
        self.assertEqual(actual, expected)
