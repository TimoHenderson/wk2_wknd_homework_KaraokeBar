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

        self.guest_1 = Guest("Fred Fudge", 15.00)
        self.guest_2 = Guest("Arnold Clark", 12.00)
        self.poor_guest = Guest("Ann Gloag", 4.00)

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

    def test_can_check_in_guest__enough_space_and_can_afford(self):
        actual_message = self.karaoke_bar.check_in_guest(self.guest_1, "Small Room")
        expected_message = "Fred Fudge checked in to Small Room. "
        actual = self.karaoke_bar.rooms[2].guests[0]
        expected = self.guest_1
        self.assertEqual(actual, expected)
        self.assertEqual(actual_message, expected_message)

    def test_can_check_in_guest__not_enough_space(self):
        self.karaoke_bar.check_in_guest(self.guest_1, "Small Room")
        actual_message = self.karaoke_bar.check_in_guest(self.guest_2, "Small Room")
        expected_message = (
            "There's no space in Small Room. Arnold Clark checked in to Big Room. "
        )
        actual = self.karaoke_bar.rooms[0].guests[0]
        expected = self.guest_2
        self.assertEqual(actual, expected)
        self.assertEqual(actual_message, expected_message)

    def test_can_check_in_guest__no_space(self):
        self.karaoke_bar.check_in_guest(Guest("A", 10.00), "Medium Room")
        self.karaoke_bar.check_in_guest(Guest("A", 10.00), "Medium Room")
        self.karaoke_bar.check_in_guest(Guest("A", 10.00), "Medium Room")
        self.karaoke_bar.check_in_guest(Guest("A", 10.00), "Medium Room")
        self.karaoke_bar.check_in_guest(Guest("A", 10.00), "Medium Room")
        self.karaoke_bar.check_in_guest(self.guest_1, "Medium Room")
        actual_message = self.karaoke_bar.check_in_guest(self.guest_2, "Small Room")
        expected_message = "Sorry, there is no space in any rooms"
        self.assertEqual(actual_message, expected_message)

    def test_can_check_out_guest(self):
        self.karaoke_bar.check_in_guest(self.guest_1, "Medium Room")
        self.karaoke_bar.check_out_guest(self.guest_1, "Medium Room")
        actual = self.karaoke_bar.rooms[1].guests
        expected = []
        self.assertEqual(actual, expected)

    def test_find_room_with_space(self):
        self.karaoke_bar.check_in_guest(Guest("A", 10.00), "Medium Room")
        self.karaoke_bar.check_in_guest(Guest("A", 10.00), "Medium Room")
        self.karaoke_bar.check_in_guest(Guest("A", 10.00), "Medium Room")
        self.karaoke_bar.check_in_guest(Guest("A", 10.00), "Medium Room")
        self.karaoke_bar.check_in_guest(self.guest_1, "Medium Room")
        actual = self.karaoke_bar.find_rooms_with_space()
        expected = [self.rooms[2]]
        self.assertEqual(actual, expected)

    def test_has_cash(self):
        actual = self.karaoke_bar.total_cash
        expected = 0.00
        self.assertEqual(actual, expected)

    def test_has_entry_fee(self):
        actual = self.karaoke_bar.entry_fee
        expected = 5.00
        self.assertEqual(actual, expected)

    def test_check_in_guest__can_afford(self):
        guest = self.guest_1
        actual_message = self.karaoke_bar.check_in_guest(guest, "Medium Room")
        expected_message = "Fred Fudge checked in to Medium Room. "
        self.assertEqual(actual_message, expected_message)
        actual_guest_cash = guest.cash
        expected_guest_cash = 10.00
        self.assertEqual(actual_guest_cash, expected_guest_cash)
        actual_guests_in_room = self.rooms[1].guests
        expected_guests_in_room = [guest]
        self.assertEqual(actual_guests_in_room, expected_guests_in_room)

    def test_check_in_guest__can_not_afford(self):
        guest = self.poor_guest
        actual_message = self.karaoke_bar.check_in_guest(guest, "Medium Room")
        expected_message = "Sorry, you don't have enough cash"
        self.assertEqual(actual_message, expected_message)
        actual_guest_cash = guest.cash
        expected_guest_cash = 4.00
        self.assertEqual(actual_guest_cash, expected_guest_cash)
        actual_guests_in_room = self.rooms[1].guests
        expected_guests_in_room = []
        self.assertEqual(actual_guests_in_room, expected_guests_in_room)

    def test_get_rooms_guest_can_afford__None(self):
        guest = self.poor_guest
        actual = self.karaoke_bar.get_rooms_guest_can_afford(guest)
        expected = []
        self.assertEqual(actual, expected)
