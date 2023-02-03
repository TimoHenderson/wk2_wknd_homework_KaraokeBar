import unittest
from src.room import Room
from src.song import Song
from src.guest import Guest


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

    def test_can_check_in_guest(self):
        guest = Guest("Fred Fudge")
        self.room.check_in(guest)
        actual = self.room.guests[0]
        expected = guest
        self.assertEqual(actual, expected)

    def test_can_check_out_guest(self):
        guest = Guest("Fred Fudge")
        self.room.check_in(guest)
        self.room.check_out(guest)
        actual = self.room.guests
        expected = []
        self.assertEqual(actual, expected)
