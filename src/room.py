class Room:
    def __init__(self, name, capacity):
        self.name = name
        self.capacity = capacity
        self.songs = []
        self.guests = []

    def add_song(self, song):
        self.songs.append(song)

    def check_in(self, guest):
        if self.has_space():
            self.guests.append(guest)
            return True
        else:
            return False

    def check_out(self, guest):
        self.guests.remove(guest)

    def has_space(self):
        return len(self.guests) < self.capacity
