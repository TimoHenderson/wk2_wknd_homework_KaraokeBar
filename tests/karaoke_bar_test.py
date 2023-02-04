import unittest
from src.karaoke_bar import KaraokeBar
from src.room import Room
from src.guest import Guest


class TestKaraokeBar(unittest.TestCase):
    def setUp(self):
        self.rooms = [
            Room("Big Room", 3),
            Room("Medium Room", 2),
            Room("Small Room", 1),
        ]
        self.karaoke_bar = KaraokeBar("K Bar", self.rooms)

        self.guest_1 = Guest("Fred Fudge")
        self.guest_2 = Guest("Arnold Clark")

    def test_has_name(self):
        actual = self.karaoke_bar.name
        expected = "K Bar"
        self.assertEqual(actual, expected)

    def test_has_rooms(self):
        actual = self.karaoke_bar.rooms
        expected = self.rooms
        self.assertEqual(actual, expected)

    def test_can_find_room_by_name__exists(self):
        room = self.karaoke_bar.find_room_by_name("Medium Room")
        actual = room
        expected = self.rooms[1]
        self.assertEqual(actual, room)

    def test_can_find_room_by_name__does_not_exist(self):
        room = self.karaoke_bar.find_room_by_name("Fake Room")
        actual = room
        self.assertIsNone(actual)

    def test_can_check_in_guest__enough_space(self):
        actual_message = self.karaoke_bar.check_in_guest(self.guest_1, "Small Room")
        expected_message = "Fred Fudge checked in to Small Room"
        actual = self.karaoke_bar.rooms[2].guests[0]
        expected = self.guest_1
        self.assertEqual(actual, expected)
        self.assertEqual(actual_message, expected_message)

    def test_can_check_in_guest__not_enough_space(self):
        self.karaoke_bar.check_in_guest(self.guest_1, "Small Room")
        actual_message = self.karaoke_bar.check_in_guest(self.guest_2, "Small Room")
        expected_message = "No space in Small Room. Arnold Clark checked into Big Room"
        actual = self.karaoke_bar.rooms[0].guests[0]
        expected = self.guest_2
        self.assertEqual(actual, expected)
        self.assertEqual(actual_message, expected_message)

    def test_can_check_out_guest(self):
        self.karaoke_bar.check_in_guest(self.guest_1, "Medium Room")
        self.karaoke_bar.check_out_guest(self.guest_1, "Medium Room")
        actual = self.karaoke_bar.rooms[1].guests
        expected = []
        self.assertEqual(actual, expected)

    def test_find_room_with_space(self):
        self.karaoke_bar.check_in_guest(self.guest_1, "Medium Room")
        self.karaoke_bar.check_in_guest(self.guest_1, "Medium Room")
        self.karaoke_bar.check_in_guest(self.guest_1, "Medium Room")
        self.karaoke_bar.check_in_guest(self.guest_1, "Medium Room")
        self.karaoke_bar.check_in_guest(self.guest_1, "Medium Room")
        actual = self.karaoke_bar.find_room_with_space()
        expected = self.rooms[2]
        self.assertEqual(actual, expected)
