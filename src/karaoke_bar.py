class KaraokeBar:
    def __init__(self, name, rooms):
        self.name = name
        self.rooms = rooms

    def find_room_by_name(self, name):
        return next((room for room in self.rooms if room.name == name), None)
