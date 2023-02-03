class Room:
    def __init__(self, name, capacity):
        self.name = name
        self.capacity = capacity
        self.songs = []
        self.guests = []

    def add_song(self, song):
        self.songs.append(song)

    def check_in(self, guest):
        self.guests.append(guest)

    def check_out(self, guest):
        self.guests.remove(guest)
