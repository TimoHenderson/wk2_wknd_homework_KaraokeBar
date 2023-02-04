class KaraokeBar:
    def __init__(self, name, rooms):
        self.name = name
        self.rooms = rooms
        self.total_cash = 0.00
        self.entry_fee = 5.00

    def find_room_by_name(self, name):
        return next((room for room in self.rooms if room.name == name), None)

    def check_in_guest(self, guest, room_name):
        desired_room = self.find_room_by_name(room_name)
        if desired_room.has_space():
            desired_room.check_in(guest)
            return f"{guest.name} checked in to {desired_room.name}"
        else:
            room_with_space = self.find_room_with_space()
            if room_with_space != None:
                room_with_space.check_in(guest)
                return f"No space in {desired_room.name}. {guest.name} checked into {room_with_space.name}"
            else:
                return "Sorry, there is no space in any rooms"

    def check_out_guest(self, guest, room_name):
        room = self.find_room_by_name(room_name)
        room.check_out(guest)

    def find_room_with_space(self):
        return next((room for room in self.rooms if room.has_space()), None)

    def charge_guest(self, guest, amount):
        if guest.pay_cash(amount):
            self.total_cash += amount
