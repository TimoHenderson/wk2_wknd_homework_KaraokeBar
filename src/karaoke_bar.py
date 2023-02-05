class KaraokeBar:
    def __init__(self, name, rooms):
        self.name = name
        self.rooms = rooms
        self.total_cash = 0.00
        self.entry_fee = 5.00

    def find_room_by_name(self, name):
        return next((room for room in self.rooms if room.name == name), None)

    def check_in_guest(self, guest, room_name):
        message = ""
        if self.get_rooms_guest_can_afford(guest) == []:
            message = "Sorry, you don't have enough cash"
        else:
            desired_room = self.find_room_by_name(room_name)
            is_checked_in, check_in_message = desired_room.check_in(guest)
            message += check_in_message

            if not is_checked_in:
                rooms_with_space = self.find_rooms_with_space()
                if rooms_with_space == []:
                    message = "Sorry, there is no space in any rooms"
                else:
                    for room in rooms_with_space:
                        is_checked_in, check_in_message = room.check_in(guest)
                        message += check_in_message
                        if is_checked_in:
                            break

        return message

    def check_out_guest(self, guest, room_name):
        room = self.find_room_by_name(room_name)
        room.check_out(guest)

    def find_rooms_with_space(self):
        return [room for room in self.rooms if room.has_space()]

    def charge_guest(self, guest, amount):
        if guest.pay_cash(amount):
            self.total_cash += amount

    def get_rooms_guest_can_afford(self, guest):
        return [room for room in self.rooms if guest.can_afford_to_pay(room.entry_fee)]
