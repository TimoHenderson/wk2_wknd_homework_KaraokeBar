class Room:
    def __init__(self, name):
        self.name = name
        self.songs = []
        self.guests = []

    def add_song(self, song):
        self.songs.append(song)
