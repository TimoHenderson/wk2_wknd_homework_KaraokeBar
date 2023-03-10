import unittest
from src.room import Room
from src.song import Song
from src.guest import Guest


class TestRoom(unittest.TestCase):
    def setUp(self):
        self.room = Room("Small Room", 1)
        self.guest_1 = Guest("Fred Fudge", 15.00)
        self.guest_2 = Guest("Arnold Clark", 3.00)
        self.song_1 = Song("Walk", "Pantera")
        self.song_2 = Song("Tarkus", "ELP")
        self.guest_with_fav_song = Guest("Jenny", 12.00, self.song_1)

    def test_has_name(self):
        actual = self.room.name
        expected = "Small Room"
        self.assertEqual(actual, expected)

    def test_has_transactions(self):
        actual = self.room.transactions
        expected = []
        self.assertEqual(actual, expected)

    def test_has_entry_fee(self):
        actual = self.room.entry_fee
        expected = 5.00
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

    def test_can_check_in_guest__has_space_no_fav_song(self):
        message = self.room.check_in(self.guest_1)[1]
        actual = self.room.guests[0]
        expected = self.guest_1
        self.assertEqual(actual, expected)
        expected_message = "Fred Fudge checked in to Small Room. "
        self.assertEqual(message, expected_message)

    def test_can_check_in_guest__has_space_has_fav_song(self):
        guest = self.guest_with_fav_song
        self.room.add_song(self.song_1)
        message = self.room.check_in(guest)[1]
        actual = self.room.guests[0]
        expected = guest
        self.assertEqual(actual, expected)
        expected_message = (
            "Jenny checked in to Small Room. Their favourite song is in this room!"
        )
        self.assertEqual(message, expected_message)

    def test_can_check_in_guest__no_space(self):
        self.room.check_in(self.guest_1)
        self.room.check_in(self.guest_2)
        actual = self.room.guests[0]
        expected = self.guest_1
        self.assertEqual(actual, expected)

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

    def test_favourite_song_in_room__True(self):
        room = self.room
        song = self.song_1
        guest = self.guest_with_fav_song
        room.add_song(song)
        actual = room.favourite_song_in_room(guest)
        expected = True
        self.assertEqual(actual, expected)

    def test_favourite_song_in_room__False_guest_has_favourite(self):
        room = self.room
        song = self.song_1
        song_2 = self.song_2
        guest = self.guest_with_fav_song
        room.add_song(song_2)
        actual = room.favourite_song_in_room(guest)
        expected = False
        self.assertEqual(actual, expected)

    def test_favourite_song_in_room__False_guest_has_no_favourite(self):
        room = self.room
        song_2 = self.song_2
        guest = self.guest_1
        room.add_song(song_2)
        actual = room.favourite_song_in_room(guest)
        expected = False
        self.assertEqual(actual, expected)

    def test_charge_guest__can_afford(self):
        successful = self.room.charge_guest("anything", self.guest_1, 1.00)
        actual_guest_cash = self.guest_1.cash
        expected_guest_cash = 14.00
        self.assertEqual(actual_guest_cash, expected_guest_cash)
        actual_transactions_length = len(self.room.transactions)
        expected_transactions_length = 1
        self.assertEqual(actual_transactions_length, expected_transactions_length)
        self.assertTrue(successful)

    def test_charge_guest__can_not_afford(self):
        successful = self.room.charge_guest("anything", self.guest_2, 5.00)
        actual_guest_cash = self.guest_2.cash
        expected_guest_cash = 3.00
        self.assertEqual(actual_guest_cash, expected_guest_cash)
        actual_transactions_length = len(self.room.transactions)
        expected_transactions_length = 0
        self.assertEqual(actual_transactions_length, expected_transactions_length)
        self.assertFalse(successful)
