import unittest
from src.room import Room
from src.song import Song
from src.guest import Guest


class TestRoom(unittest.TestCase):
    def setUp(self):
        self.room = Room("Small Room", 1)
        self.guest_1 = Guest("Fred Fudge", 15.00)
        self.guest_2 = Guest("Arnold Clark", 3.00)
        self.song = Song("Walk", "Pantera")
        self.guest_with_fav_song = Guest("Jenny", 12.00, self.song)

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
        successful = self.room.check_in(self.guest_1)
        actual = self.room.guests[0]
        expected = self.guest_1
        self.assertEqual(actual, expected)
        self.assertTrue(successful)

    def test_can_check_in_guest__no_space(self):
        self.room.check_in(self.guest_1)
        successful = self.room.check_in(self.guest_2)
        actual = self.room.guests[0]
        expected = self.guest_1
        self.assertEqual(actual, expected)
        self.assertFalse(successful)
        self.assertEqual(len(self.room.guests), 1)

    def test_can_check_out_guest(self):
        self.room.check_in(self.guest_1)
        self.room.check_out(self.guest_1)
        actual = self.room.guests
        expected = []
        self.assertEqual(actual, expected)

    def test_has_capacity(self):
        actual = self.room.capacity
        expected = 1
        self.assertEqual(actual, expected)

    def test_has_room__False(self):
        self.room.check_in(self.guest_1)
        has_space = self.room.has_space()
        self.assertFalse(has_space)

    def test_has_room__True(self):
        has_space = self.room.has_space()
        self.assertTrue(has_space)
