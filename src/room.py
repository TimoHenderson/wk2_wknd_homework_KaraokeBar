class Room:
    def __init__(self, name, capacity, entry_fee=5.00):
        self.name = name
        self.capacity = capacity
        self.songs = []
        self.guests = []
        self.entry_fee = entry_fee

    def add_song(self, song):
        self.songs.append(song)

    def check_in(self, guest):
        if self.has_space():
            self.guests.append(guest)
            if self.favourite_song_in_room(guest):
                return "Woohoo"

    def check_out(self, guest):
        self.guests.remove(guest)

    def has_space(self):
        return len(self.guests) < self.capacity

    def favourite_song_in_room(self, guest):
        return guest.favourite_song in self.songs
